import os
from langchain_community.document_loaders import TextLoader

notes_path = os.path.join(os.path.dirname(__file__), "notes.txt")
loader = TextLoader(notes_path)
documents = loader.load()
print (documents[0].page_content)