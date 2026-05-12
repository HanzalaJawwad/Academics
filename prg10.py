!pip install sentence-transformers faiss-cpu langchain-community langchain-text-splitters pypdf 
from langchain_community.document_loaders import PyPDFLoader 
from langchain_text_splitters import CharacterTextSplitter 
from langchain_community.vectorstores import FAISS 
from langchain_community.embeddings import HuggingFaceEmbeddings 
import re 
import os 
!pip install pypdf 
import sys 
!{sys.executable} -m pip install pypdf 
import pypdf 
print("Working ") 
pdf_path = "ipc.pdf"   # make sure file is in same directory 
loader = PyPDFLoader("C:/Users/Staff/Desktop/JN/ipc.pdf") 
docs = loader.load() 
print("Pages loaded:", len(docs)) 
splitter = CharacterTextSplitter(chunk_size=1200, chunk_overlap=200) 
documents = splitter.split_documents(docs) 
print("Total chunks created:", len(documents)) 
import sys 
!{sys.executable} -m pip install sentence-transformers 
import sentence_transformers 
print("Installed ") 
embeddings = HuggingFaceEmbeddings( 
model_name="sentence-transformers/all-MiniLM-L6-v2" 
) 
import sys 
!{sys.executable} -m pip install faiss-cpu 
db = FAISS.from_documents(documents, embeddings) 
29 
 
30  
 
retriever = db.as_retriever(search_kwargs={"k": 5}) 
 
print("IPC Chatbot Ready!") 
 
full_text = "\n".join([doc.page_content for doc in documents]) 
 
 
print("\nType 'exit' to stop.\n") 
 
while True: 
    query = input("Ask about IPC: ") 
 
    if query.lower() == "exit": 
        print("Chatbot stopped.") 
        break 
 
    match = re.search(r"\b\d+\b", query) 
 
    if match: 
        section_number = match.group() 
        print(f"\n Extracting Section {section_number}...\n") 
 
        # Extract section using regex (captures full section content) 
        pattern = re.compile( 
            rf"{section_number}\..*?(?=\n\d+\.)", 
            re.DOTALL 
        ) 
 
        result = pattern.search(full_text) 
 
        if result: 
            section_text = result.group() 
            print(" Section Content:\n") 
            print(section_text[:1000])  # limit output 
        else: 
            print(" Section not found, using fallback search...\n") 
            results = retriever.invoke(query) 
 
            for i, doc in enumerate(results[:3]): 
                print(f"Result {i+1}:\n") 
                print(doc.page_content[:500]) 
                print("\n-----------------------------\n") 
 
    else: 
        results = retriever.invoke(query) 
 
        print("\n Top Relevant IPC Content:\n") 
for i, doc in enumerate(results[:3]): 
print(f"Result {i+1}:\n") 
print(doc.page_content[:500]) 
print("\n-----------------------------\n")
