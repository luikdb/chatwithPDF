from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import os



load_dotenv()
def main():
    openai_api_key = os.getenv("OPENAI_API_KEY")
    st.image("logo.png", width=100)
    st.title("Chat with :red[PDF] :)")
    st.subheader("_by Lui KDB_")
    
    #UPLOADING THE FILE
    pdf = st.file_uploader("Upload your PDF", type="pdf")
    user_question = st.text_input("Ask anything about your PDF:")


    #TEXT EXTRACTION
    if pdf is not None:
      pdf_reader = PdfReader(pdf)
      text = ""
      for page in pdf_reader.pages:
        text += page.extract_text()
     
    #SPLITTING INTO CHUNKS
      text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
      )
      chunks = text_splitter.split_text(text)
      
    #EMBEDDING 

      embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
      knowledge_base = FAISS.from_texts(chunks, embeddings)
      
    #TAKING INPUTS FROM USER
      
      if user_question:
        docs = knowledge_base.similarity_search(user_question)
        
        llm = OpenAI(model="text-davinci-003")
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
          response = chain.run(input_documents=docs, question=user_question)
          print(cb)
           
        st.write(response)
    

if __name__ == '__main__':
    main()
