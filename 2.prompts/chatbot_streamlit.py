#CHATBOT USING STREAM-LIT
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

st.write("🤖CHAT BOT")


user_question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if user_question.strip() == "":
        st.warning("Please enter a question first.")
    else:
        with st.spinner("AI is thinking..."):
            result = model.invoke(user_question)

        st.subheader("Answer:")
        st.write(result.content)