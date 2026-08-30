#Static prompt code 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

st.write("🤖 CHAT BOT")

static_prompt = """
You are a helpful AI teacher.

Always:
- Explain in very simple language.
- Give a real-world example.
- Give a small example.
"""

user_question = st.text_input("Enter your question:")

if st.button("Ask AI"):

    if user_question.strip() == "":
        st.warning("Please enter a question first.")

    else:
        with st.spinner("AI is thinking..."):

            prompt = static_prompt + "\nUser Question: " + user_question

            result = model.invoke(prompt)

        st.subheader("Answer:")
        st.write(result.content)