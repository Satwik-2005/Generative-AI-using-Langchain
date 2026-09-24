from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b", task="text-generation")

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)