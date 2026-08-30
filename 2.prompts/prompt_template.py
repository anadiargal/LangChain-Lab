from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# prompt = PromptTemplate(
#     template="""
# You are an expert teacher.

# Explain {topic} to a {level} student.

# Give:
# 1. Simple explanation
# 2. Real-world example
# 3. Small code example
# """,
#     input_variables=["topic", "level"]
# )

prompt = PromptTemplate(
    template = """
you are a ai researcher .

Explain {topic} and give markdown example to the {level} intern .

Give : 
1. simple explanation and use little hindi also 
2. small diagram 
3. pure mathematical representation 


""",
input_variables=["topic" , "level"]
)




final_prompt = prompt.invoke({
    "topic": "deepLearning",
    "level": "beginner"
})

result = model.invoke(final_prompt)

print(result.content)