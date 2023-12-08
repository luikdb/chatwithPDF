# **PDF Chatbot using LangChain, OpenAI, and Streamlit**



## Summary :hourglass_flowing_sand:



1. **Text Extraction-** Parses text content from uploaded PDF files.
2. **Chunking-** Divides extracted text into manageable chunks for better processing.
3. **Embedding-** Utilizes OpenAI's embeddings to convert text into numerical representations, aiding in semantic understanding.
4. **Vector Store (FAISS)-** Creates a vector store using FAISS to efficiently index and retrieve chunks of text for quick information retrieval.
5. **Semantic Search-** Employs semantic search techniques to understand user queries and retrieve relevant information from the stored text chunks.

The chatbot, powered by Streamlit for the user interface, leverages these technologies to enable users to upload PDFs, ask questions, and receive accurate answers based on the content within the PDF files. OpenAI's language understanding and the underlying technical processes enable effective information retrieval and response generation.





## Setup & Run :wrench:

### Installation
1. Clone/download the repository.
2. Install required packages: `pip install -r requirements.txt`
3. Obtain an OpenAI API key and create a `.env` file: `OPENAI_API_KEY=your_api_key_here`

### Usage
- Upload a PDF and ask questions about its content.
- Extracts text, splits it into chunks, and uses LangChain & OpenAI to process queries.


### References
- Streamlit: [Documentation](https://docs.streamlit.io/)
- OpenAI: [Documentation](https://platform.openai.com/docs/introduction)
- LangChain: [Documentation](https://python.langchain.com/docs/get_started/introduction)
- FAISS: [Documentation](https://github.com/facebookresearch/faiss)



