from operator import index
from dotenv import load_dotenv, find_dotenv
from openai import embeddings

load_dotenv(find_dotenv())
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs():
    loader = ReadTheDocsLoader("api.python.langchain.com/en/latest")

    raw_documents = loader.load()
    print(f'loaded {len(raw_documents)} documents')

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split(raw_documents)
    for doc in documents:
        new_url = doc.metadata['source']
        new_url = new_url.replace("api.python.langchain.com", "https://api.python.langchain.com/en/latest")
        doc.metadata.update({'source': new_url})

    print(f'Going to embed {len(documents)} documents to Pinecone')
    PineconeVectorStore.from_documents(documents, embeddings=embeddings, index_name="langchain-docs-index")

print("******* Loading to vectorstore done ****")

if __name__=='__main__':
    ingest_docs()

