from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-...",
    temperature=0.2,
    max_tokens=1000
)

### 1. `temperature`
#`temperature` controls **how random or creative the model's output is**.

#- `temperature = 0` → very predictable and consistent
#- `temperature = 0.5` → balanced
#- `temperature = 1` → more creative and random


#### 2. `max_completion_tokens`
#This controls the **maximum number of tokens the AI is allowed to generate in its response**.

