from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.1-flash-lite"
)

chat_history = []

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    chat_history.append(user_input)

    result = model.invoke(chat_history)

    chat_history.append(result)

    print("AI:", result.text)

print(chat_history)