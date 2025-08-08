# 🤖 AWS Bedrock Claude Example

This example demonstrates how to use Amazon Bedrock to interact with Anthropic's Claude model from Python. It shows how to authenticate with AWS, send a prompt, and print the model's response.

---

## 📂 What does this script do?

1. **Loads AWS credentials** from a `.env` file.
2. **Initializes a Bedrock client** using `boto3`.
3. **Prepares a request** for Claude (Anthropic) with a user message.
4. **Sends the request** to the Claude model via Bedrock.
5. **Parses and prints** the model's response.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install boto3 python-dotenv
   ```
2. **Set your AWS credentials** in a `.env` file:
   ```env
   AWS_ACCESS_KEY_ID=your-access-key
   AWS_SECRET_ACCESS_KEY=your-secret-key
   AWS_REGION=us-east-1
   ```
3. **Run the script:**
   ```bash
   python main.py
   ```

---

## 🧑‍💻 Code Walkthrough

### 1. **Setup and Authentication**
- Loads AWS credentials from `.env` using `python-dotenv`.
- Initializes a Bedrock client with `boto3`.

### 2. **Prepare the Request**
- Sets up the request payload for Claude, specifying the prompt, temperature, and max tokens.

### 3. **Invoke the Model**
- Sends the request to the Claude model using `invoke_model`.

### 4. **Parse and Print the Response**
- Reads and parses the response, then prints the model's reply.

---

## 📝 Example Output

```
Hello world
```

---

## 🧠 Concepts Learned
- **AWS Bedrock:** A fully managed service for accessing foundation models (like Claude) via API.
- **boto3:** AWS SDK for Python.
- **.env for secrets:** Keeps credentials out of your code.
- **Prompting Claude:** Sending a message and receiving a response.

---

## 📚 Resources
- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/)
- [Anthropic Claude API](https://docs.anthropic.com/claude/docs)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

Happy prompting! 🚀
