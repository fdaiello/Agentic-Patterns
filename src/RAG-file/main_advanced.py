
import os
from dotenv import load_dotenv
import csv
from typing import Dict, List, Optional
from pydantic import BaseModel, Field
from langchain_community.vectorstores import Qdrant
from langchain_community.document_loaders.base import BaseLoader
from langchain_community.document_loaders import CSVLoader as CommunityCSVLoader
from langchain.docstore.document import Document
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from qdrant_client.http import models as rest


# Load environment variables
load_dotenv()


class BookSearch(BaseModel):
    year: str = Field(description="year book was written")
    genre: str = Field(description="genre of book")


parser = PydanticOutputParser(pydantic_object=BookSearch)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()},
)


loader = CommunityCSVLoader(
    file_path="./src/RAG-file/dataset_small.csv",
    source_column="title",
    metadata_columns=["categories", "published_year"]
)



def get_parsed_result(book_request):
    _input = prompt.format_prompt(query=book_request)
    model = ChatOpenAI()
    output = model.invoke(_input.to_string())
    content = output.content
    # Ensure content is a string for parser.parse
    if isinstance(content, list):
        content_str = "\n".join(str(x) for x in content)
    elif isinstance(content, dict):
        content_str = str(content)
    else:
        content_str = str(content)
    parsed = parser.parse(content_str)
    return parsed


def create_filter(parsed):
    qdrant_filter = rest.Filter(
        must=[
            rest.FieldCondition(
                key="metadata.categories",
                match=rest.MatchValue(value=parsed.genre),
            ),
            rest.FieldCondition(
                key="metadata.published_year",
                match=rest.MatchValue(value=parsed.year),
            )
        ]
    )
    return qdrant_filter



data = loader.load()

embeddings = OpenAIEmbeddings()

qdrant_docsearch = Qdrant.from_documents(
    data,
    embeddings,
    location=":memory:",
    collection_name="book"
)


while True:
    user_input = input("Hi im an AI librarian what can I help you with?\n")
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    parsed_result = get_parsed_result(user_input)
    book_request = "You are a librarian. Help the user answer their question. Do not provide the ISBN." +\
        f"\nUser:{user_input}"

    qa = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(),
        chain_type="stuff",
        retriever=qdrant_docsearch.as_retriever(
            search_kwargs={'filter': create_filter(parsed_result)}),
        return_source_documents=True
    )

    result = qa({"query": book_request})
    print(len(result['source_documents']))
    print(result["result"])
