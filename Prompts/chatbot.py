from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="openai/gpt-oss-120b", task="text-generation", max_new_tokens=4096)

model = ChatHuggingFace(llm=llm)

chat_history = [
    SystemMessage(content="You are a useful chat assistant")
]

while True:
    user = input('You: ')
    chat_history.append(HumanMessage(content=user))
    if user == 'exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(chat_history)


