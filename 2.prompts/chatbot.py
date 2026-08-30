#CHATBOT
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite",
    temperature=0
)

print("🤖 CHATBOT")
print("Type 'exit' to stop the chatbot.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("Bot: Goodbye! 👋")
        break

    if user_question.strip() == "":
        print("Bot: Please enter a question.")
        continue

    result = model.invoke(user_question)

    print("Bot:", result.text)


"""
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

print("🤖 AI")
print("Type 'exit' to stop the chatbot.\n")

while True:
    user_question = input("You: ")

    if user_question.lower() == "exit":
        print("AI: Goodbye! 👋")
        break

    if user_question.strip() == "":
        print("AI: Please enter a question.")
        continue

    result = model.invoke(user_question)

    print("AI:", result.content)
    
"""