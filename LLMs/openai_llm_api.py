from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-4o-mini')

prompt = "Who is Virat Kohli? Give a short factual answer."
result = llm.invoke(prompt)

print(result)