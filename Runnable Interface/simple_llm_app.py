from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate

# Initialisation of model
model = OpenAI(model="openai/gpt-oss-120b", temperature=0.7)

# create a prompt
prompt = PromptTemplate(
    template="Suggest me a catchy blog title about {topic}.",
    input_variables=['topic']
)

# input from user
topic = input("Enter a topic")

# format the prompt
formatted_prompt = prompt.format(topic=topic)

# call the LLM directly
blog_title = model.predict(formatted_prompt)

# print the output
print("Generated Blog title: ", blog_title)