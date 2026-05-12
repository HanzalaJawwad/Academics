pip install langchain 
pip install langchain-community 
pip install cohere 
!pip install -U langchain-cohere 
To create API Key follow the below steps: 
Go to  https://dashboard.cohere.com/ 
1. Login 
2. Click API Keys 
3. Click Create API Key 
4. Copy the key 
from langchain_core.prompts import PromptTemplate 
from langchain_cohere import ChatCohere 
import os 
# Step 1: Set your Cohere API key 
os.environ["COHERE_API_KEY"] = "paste the API key here" 
# Step 2: Load text document 
file_path = "Artificial_Intelligence.txt" 
with open(file_path, "r", encoding="utf-8") as file: 
document_text = file.read() 
print("File loaded successfully!") 
# Step 3: Create Prompt Template 
prompt_template = PromptTemplate( 
input_variables=["text"], 
template=""" 
You are an AI assistant. 
Summarize the following text in simple and clear language. 
Keep the summary short and meaningful. 
Text: 
{text} 
""" 
) 
# Step 4: Initialize Cohere Chat Model 
llm = ChatCohere(model="command-r-08-2024") 
# Step 5: Generate Output 
response = llm.invoke(prompt_template.format(text=document_text)) 
25 
print("\nSummary:\n") 
print(response.content) 
Output: 
File loaded successfully! 
Summary: 
Artificial Intelligence (AI) is a field of computer science that aims to develop intelligent machines 
capable of performing complex tasks typically associated with human intelligence. These tasks involve 
learning, problem-solving, language understanding, image and speech recognition, and decision
making.
