from langchain_community.document_loaders import WebBaseLoader

urls = ["https://www.andhbhakt.org",
        "https://www.andhbhakt.org/2023/06/andhra-pradesh-assembly-election-2024.html",
        "https://www.andhbhakt.org/past-75-years",
        "https://www.andhbhakt.org/state-facts",
        "https://www.andhbhakt.org/scams",
        "https://www.andhbhakt.org/pin",
        "https://www.andhbhakt.org/schemes",
        "https://www.andhbhakt.org/reports",
        "https://www.andhbhakt.org/mp-mla",
        "https://www.andhbhakt.org/funding",
        "https://www.andhbhakt.org/development-index",
        "https://www.andhbhakt.org/where-is-my-tax",
        "https://www.andhbhakt.org/my-rights"]
data = WebBaseLoader(urls)

docs = data.load()

print(len(docs))