from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
import os
import openai
os.environ['OPENAI_API_KEY'] = " put your openai api key here "
openai.api_key = os.environ['OPENAI_API_KEY']
vector_index = FAISS.load_local("index_stores", OpenAIEmbeddings())
retriever = vector_index.as_retriever(search_type="similarity",search_kwargs={"k":4})
qa_interface = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(),
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=False,
)
query = input("enter your query :") + ".Please provide a response based on the information presented in the context. Ensure that your response strictly adheres to the details in the context and refrains from introducing any information not mentioned in the context. The response should address questions, whether they are asked in one word or in long sentences, as long as the response aligns with the information available in the context. Additionally, use generative text to elaborate on or provide further context when necessary."
response = qa_interface(
   f"{query}"
)
print(response)
