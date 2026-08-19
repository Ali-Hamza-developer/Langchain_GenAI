# LLM (Large Language Models)

This folder contains examples of working with **Large Language Models (LLMs)** using LangChain.

## What is an LLM?

A Large Language Model is an AI model that can understand and generate human-like text.

Examples of LLMs include:

- OpenAI models
- Anthropic Claude
- Google Gemini
- Hugging Face models
- Locally running open-source models

## Files in this Folder

### `llm_demo.py`

A basic example of creating an LLM and sending a prompt to it.

The general flow is:

```text
User Prompt
    ↓
LLM
    ↓
Generated Response
```

Example:

```python
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is LangChain?")

print(result)
```

## LLM vs Chat Model

An **LLM** traditionally works with plain text:

```text
Prompt → LLM → Text Response
```

A **Chat Model** works with messages and conversations:

```text
System Message
      +
Human Message
      +
AI Message
      ↓
Chat Model
      ↓
Response
```

Chat models are covered separately in the `2_ChatModels` folder.

## Environment Variables

If you are using OpenAI, create a `.env` file in your project and add:

```text
OPENAI_API_KEY=your_api_key
```

Load the environment variables using:

```python
from dotenv import load_dotenv

load_dotenv()
```

## Main Concept

The important LangChain operation is:

```python
llm.invoke("Your prompt")
```

`invoke()` sends the input to the model and returns the model's response.

## Learning Goals

After completing this folder, you should understand:

- What an LLM is
- How to initialize an LLM
- How to provide a prompt
- How to call an LLM using `invoke()`
- How environment variables are used for API keys
- The basic difference between LLMs and Chat Models