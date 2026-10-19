from langchain_community.document_loaders import PyPDFLoader
data = PyPDFLoader("/Users/jiteshtomar/Documents/RAG/documents_loaders/GRU.pdf")

docs = data.load()

print(docs[0].page_content)