from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()

# Create Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Streamlit UI
st.title("🤖 Dynamic AI Teacher")

st.write("Ask AI to explain any topic according to your level!")

# Select student level
level = st.selectbox(
    "Select your level:",
    ["Beginner", "Intermediate", "Advanced"]
)

# Enter topic
topic = st.text_input(
    "Enter topic:",
    placeholder="Example: Python Decorators"
)

# Ask AI button
if st.button("Ask AI 🚀"):

    # Check if topic is empty
    if topic.strip() == "":
        st.warning("Please enter a topic first.")

    else:

        # Dynamic Prompt
        prompt = f"""
You are an expert teacher.

Student level:
{level}

Topic:
{topic}

Explain the topic according to the student's level.

Give:
1. A simple explanation
2. A real-world example
3. A small code example
4. Important points to remember
"""

        # Show loading message
        with st.spinner("🤖 AI is thinking..."):

            # Send prompt to Gemini
            result = model.invoke(prompt)

        # Display result
        st.subheader("📚 AI Teacher's Answer")

        st.write(result.content)