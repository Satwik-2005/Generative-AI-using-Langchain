from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'cricket'})

print(result) 

chain.get_graph().print_ascii()