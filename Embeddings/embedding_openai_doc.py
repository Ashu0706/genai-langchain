from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large',dimensions=50)

doc = [
    'what is the name of rivers',
    'whos is virat kohli'
]

result = embedding.embed_documents(doc)

print(str(result))

