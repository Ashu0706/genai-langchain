from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

load_dotenv()

messages = [
    SystemMessage(content='You are helpful AI assistence')
]

model = ChatOpenAI(model= 'gpt-4',temperature=0.2,max_completion_tokens=50)

user_inp = input()
while user_inp:
    messages.append(HumanMessage(content=user_inp))
    result = model.invoke(messages)
    print(result.content)
    messages.append(AIMessage(content=result.content))
    user_inp = input()
    if user_inp in [0,'exit','0']:
        print("Thanks ")
        break
        
