from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#Chat template
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name="chat_history"),
    ('human', "{query}")
])

chat_history = []

# load the chat history
with open('ChatHistory.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

prompt = chat_template.invoke({'chat_history': chat_history, 'query': "Where is my refund"})
print(prompt)