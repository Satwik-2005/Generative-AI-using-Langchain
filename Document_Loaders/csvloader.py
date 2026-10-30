from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Social_Network_Ads.csv", encoding="latin-1")
docs = loader.load()

print(len(docs))
print(docs[0].page_content)