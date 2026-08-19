from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

from dotenv import load_dotenv
import os

load_dotenv()


# ==========================================
# HUGGING FACE MODEL
# ==========================================

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv(
        "HUGGINGFACEHUB_API_TOKEN"
    )
)

model = ChatHuggingFace(llm=llm)


# ==========================================
# CHAT HISTORY
# ==========================================

chat_history = [
    SystemMessage(
        content="You are a helpful AI assistant"
    )
]


# ==========================================
# CHAT LOOP
# ==========================================

while True:

    user_input = input("You: ")

    # Exit before adding "exit" to history
    if user_input.lower() == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    result = model.invoke(chat_history)

    chat_history.append(
        AIMessage(content=result.content)
    )

    print("AI:", result.content)


# ==========================================
# FINAL CHAT HISTORY
# ==========================================

print("\nChat History:")
print(chat_history)