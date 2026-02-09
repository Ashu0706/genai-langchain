from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

prompt = "list of brances in enginnering in india"
result = model.invoke(prompt)

print(result.content) 