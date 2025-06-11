import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter


os.environ["OPENAI_API_KEY"] = "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"
docs = [
    "The Colossus of Rhodes was a statue of the Greek sun-god Helios, erected in the city of Rhodes by Chares of Lindos in 280 BC.",
    "The Eiffel Tower is located in Paris, France."
]

text_splitter = CharacterTextSplitter(chunk_size=200, chunk_overlap=0)
split_docs = []
for doc in docs:
    split_docs.extend(text_splitter.split_text(doc))

embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_texts(split_docs, embeddings)

retriever = vectorstore.as_retriever()
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

query = "Who built the Colossus of Rhodes?"
result = qa_chain.run(query)
print(result)