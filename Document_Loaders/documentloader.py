from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# Load objects loads the whole document at a time

# documents = loader.load()

# print(len(documents))
# print(documents[0].page_content)
# print(documents[0].metadata)

# Lazy load loads every objkect on demand

documents = loader.lazy_load()

for docs in documents:
    print(docs.metadata)