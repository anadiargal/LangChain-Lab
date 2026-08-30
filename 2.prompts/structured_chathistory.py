from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

chat_history = [
    SystemMessage(content="you are great AI helpful assistant")
]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

while True:
    user_input = input("please enter: ")

    if user_input == "exit":
        break

    chat_history.append(
        HumanMessage(content=user_input)
    )

    result = model.invoke(chat_history)

    chat_history.append(
        AIMessage(content=result.content)
    )

    print("AI:", result.content)

print(chat_history)


"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage


load_dotenv()

chat_history = [
    SystemMessage(content="you are great AI helpful assistant")
]

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)



while True:
    user_input = input("please enter:")
    chat_history.append(HumanMessage(content=user_input))
    
    if user_input == "exit":
        break
    
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
    
print(chat_history)
"""