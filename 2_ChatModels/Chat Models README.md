# Chat Models

This folder contains examples of using different **Chat Models** with LangChain.

## What is a Chat Model?

A Chat Model is an LLM designed to work with **messages and conversations**.

Instead of simply providing one text prompt, we can provide different types of messages:

- `SystemMessage` — defines the behavior or role of the AI
- `HumanMessage` — represents the user's input
- `AIMessage` — represents the AI's response

The basic flow is:

```text
System Message
      ↓
Human Message
      ↓
Chat Model
      ↓
AI Message
```

## Files in this Folder

### `1_chatmodel_openai.py`

Example of using an OpenAI Chat Model.

### `2_chatmodel_anthropic.py`

Example of using an Anthropic Chat Model.

### `3_chatmodel_google.py`

Example of using a Google Chat Model.

### `4_chatmodel_hf_api.py`

Example of using a Hugging Face model through an API.

### `5_chatmodel_hf_local.py`

Example of running a Hugging Face model locally.

## Basic Example

A typical LangChain Chat Model looks like:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")

response = model.invoke("What is LangChain?")

print(response.content)
```

## Working with Messages

Chat models can also work with structured messages:

```python
from langchain_core.messages import SystemMessage, HumanMessage

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Explain LangChain.")
]

response = model.invoke(messages)

print(response.content)
```

## Different Providers

This folder demonstrates how LangChain provides a common interface for different model providers.

```text
OpenAI
Anthropic
Google
Hugging Face
Local Models
   ↓
LangChain Chat Model Interface
```

This allows you to learn the common LangChain pattern while changing the underlying model provider.

## Environment Variables

API-based models generally require API keys.

For example, your `.env` file may contain:

```text
OPENAI_API_KEY=your_api_key
ANTHROPIC_API_KEY=your_api_key
GOOGLE_API_KEY=your_api_key
HUGGINGFACEHUB_API_TOKEN=your_token
```

Do not commit your `.env` file to GitHub.

## Important Method

The main method used to call a Chat Model is:

```python
model.invoke(messages)
```

For a simple prompt:

```python
model.invoke("Hello")
```

For a conversation:

```python
model.invoke([
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello")
])
```

## Learning Goals

After completing this folder, you should understand:

- What a Chat Model is
- The difference between LLMs and Chat Models
- System, Human, and AI messages
- How to use `invoke()`
- How to work with different model providers
- How to use API-based and local Hugging Face models