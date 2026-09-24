from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain me in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain': 'cricket', 'topic': 'googly'})

print(prompt)