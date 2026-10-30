from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

prompt = PromptTemplate(
    template="Write a summary for the following poem - {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

loader = TextLoader("cricket.txt", encoding="utf-8")

document = loader.load()

print(type(document))
print(document)
print(document[0].page_content)
print(len(document))
print(type(document[0]))
print(document[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem': document[0].page_content}))