Use a pre-trained Hugging Face model to analyze sentiment in text. Assume a real-world 
application. Load the sentiment analysis pipeline. Analyze the sentiment by giving 
sentences to input. 
from transformers import pipeline  
sentiment_analyzer=pipeline("sentiment-analysis") 
def analyze_sentiment(text): 
"""Analyze sentiment of the input text using Hugging Face pipeline""" 
result=sentiment_analyzer(text) 
label=result[0]['label'] 
score=result[0]['score'] 
return f"Sentiment: {label} (Confidence: {score:.2f})" 
while True: 
user_input=input("Enter a sentence for sentiment analysis( or 'exit' to quit):").strip() 
if user_input.lower()=='exit': 
break 
print(analyze_sentiment(user_input)) 
Output: 
Enter a sentence for sentiment analysis( or 'exit' to quit): I love this product! It's amazing 
Sentiment: POSITIVE (Confidence: 1.00) 
Enter a sentence for sentiment analysis( or 'exit' to quit): This is the worst experience ever 
Sentiment: NEGATIVE (Confidence: 1.00) 
Enter a sentence for sentiment analysis( or 'exit' to quit): The service was okay, nothing special 
Sentiment: NEGATIVE (Confidence: 0.99)
