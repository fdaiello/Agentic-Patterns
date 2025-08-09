# Database Query Agent (`main.py`)

This module demonstrates how to build a conversational agent that can answer questions about your SQL database using natural language and OpenAI's GPT models.

## How It Works
- **Loads environment variables** from `.env` for API keys and database credentials.
- **Connects to your SQL database** using the URI provided in the `DB_URI` environment variable.
- **Initializes a language model** (e.g., GPT-4o) via LangChain's `ChatOpenAI`.
- **Creates a SQL agent** using LangChain's `create_sql_agent` and a toolkit for database interaction.
- **Runs an interactive loop** where you can type questions about your database, and the agent will generate and execute SQL queries to answer them.

## Usage
1. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
2. **Set up your `.env` file** with the following variables:
   ```env
   OPENAI_API_KEY=sk-...
   DB_URI=postgresql+psycopg2://username:password@host:port/dbname
   ```
   Replace with your actual OpenAI key and database connection string.

   **For testing purposes, you can use a local SQLite database:**
   ```env
   DB_URI="sqlite:///example.db"
   ```
3. **Run the agent:**
   ```sh
   python main.py
   ```
4. **Ask questions!**
   - Type natural language questions about your database (e.g., "How many users signed up last month?").
   - Type `exit` or `quit` to stop.

## Example
```
💬 Ask me questions about your database! (type 'exit' to quit)

❓ Your question: What is the average order value?
📊 Answer: The average order value is $42.50.
```

## Notes
- The agent uses the ReAct pattern to reason about your question and generate SQL queries.
- Works with any SQL database supported by SQLAlchemy (PostgreSQL, MySQL, SQLite, etc.).
- Make sure your database is accessible from your environment.
- For more advanced usage, see the LangChain documentation.
