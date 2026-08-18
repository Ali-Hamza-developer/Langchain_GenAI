from langchain_huggingface import HuggingFaceEmbeddings

# Hugging Face embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Pakistan-related documents
documents = [
    "Islamabad is the capital of Pakistan.",
    "Karachi is the largest city of Pakistan.",
    "Lahore is the capital of Punjab province.",
    "Peshawar is the capital of Khyber Pakhtunkhwa province.",
    "Quetta is the capital of Balochistan province.",
    "Multan is a major city in Punjab, Pakistan.",
    "Faisalabad is an important industrial city in Punjab, Pakistan.",
    "Rawalpindi is a major city located near Islamabad.",
    "Pakistan is located in South Asia.",
    "Pakistan shares borders with India, Afghanistan, Iran, and China.",
    "Urdu is the national language of Pakistan.",
    "English is widely used in government and education in Pakistan.",
    "The currency of Pakistan is the Pakistani Rupee.",
    "The Indus River is one of the major rivers of Pakistan.",
    "The Pakistan Monument is located in Islamabad.",
    "The Badshahi Mosque is located in Lahore.",
    "Minar-e-Pakistan is a famous monument in Lahore.",
    "The Faisal Mosque is located in Islamabad.",
    "K2 is the second-highest mountain in the world and is located in Pakistan.",
    "Pakistan became independent on 14 August 1947."
]

# Convert documents into embedding vectors
vector = embedding.embed_documents(documents)

# Information about embeddings
print("Number of documents:", len(vector))
print("Vector dimensions:", len(vector[0]))

# Print first document and its vector
print("\nFirst document:")
print(documents[0])

print("\nFirst embedding:")
print(vector[0])