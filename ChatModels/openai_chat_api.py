from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0.2,max_completion_tokens=50)

prompt = "list of brances in enginnering in india"
result = model.invoke(prompt)

print(result.content) 