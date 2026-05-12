from transformers import BartTokenizer, BartForConditionalGeneration 
# Load tokenizer and model 
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn") 
model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn") 
# Take input text 
text = input("Enter the passage to summarize:\n") 
# Tokenize input (max 1024 tokens for BART) 
inputs = tokenizer(text, max_length=1024, return_tensors="pt", truncation=True) 
# Generate summary 
summary_ids = model.generate( 
inputs["input_ids"], 
max_length=150, 
min_length=40, 
length_penalty=2.0, 
num_beams=4, 
early_stopping=True 
) 
# Decode summary 
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True) 
print("\nSummarized Text:") 
print(summary) 
Output: 
Enter the passage to summarize: 
Artificial Intelligence (AI) is transforming industries by enabling machines to perform tasks that 
typically require human intelligence. It is widely used in healthcare for disease prediction, in finance 
for fraud detection, and in education for personalized learning. AI systems use techniques such as 
machine learning and deep learning to analyze large amounts of data and make intelligent decisions. As 
technology advances, AI continues to improve efficiency, accuracy, and productivity across various 
sectors. 
Summarized Text: 
Artificial Intelligence (AI) is transforming industries by enabling machines to perform tasks that 
typically require human intelligence. It is widely used in healthcare for disease prediction, in finance 
for fraud detection, and in education for personalized learning.
