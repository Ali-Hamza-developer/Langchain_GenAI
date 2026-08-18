from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

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

query = 'tell me about Pakistan'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

print(query)
print(documents[index])
print("similarity score is:", score)