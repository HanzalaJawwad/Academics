Program 2: Use dimensionality reduction(e.d., PCA or t-SNE) to visulaize word embeddings for Q 1. Select 10 words from a specific domain (e.g., sports, technology) and visulaize their embeddings. Analyze clusters and relationships. Generate contextually rich outputs using embeddings. Write a program to generate 5 semantically similar words for a given input>

import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import PCA
from sklearn.metrics.pairwise import cosine_similarity

# Sample sports sentences
corpus = [
    "basketball is a sport played with a ball",
    "soccer is played by two teams on a field",
    "football involves a lot of physical contact",
    "athletes train hard to improve their performance",
    "coaching is an important part of every sport",
    "basketball players need good coordination",
    "a team consists of players and a coach",
    "training and exercise are important for health",
    "soccer players score goals to win games",
    "football teams compete in leagues and tournaments"
]

# Step 1: Convert text to word vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus).toarray()
words = vectorizer.get_feature_names_out()

# Step 2: Apply PCA to reduce to 2D
pca = PCA(n_components=2)
word_vectors_2d = pca.fit_transform(X.T)

# Step 3: Plot the words
plt.figure(figsize=(8, 8))
plt.scatter(word_vectors_2d[:, 0], word_vectors_2d[:, 1])

for i, word in enumerate(words):
    plt.text(word_vectors_2d[i, 0], word_vectors_2d[i, 1], word, fontsize=10)

plt.title("2D Visualization of Sports Word Embeddings (PCA)")
plt.show()

# Step 4: Find 5 similar words
def find_similar_words(target_word, words, vectors, top_n=5):
    if target_word not in words:
        print("Word not found!")
        return
    
    idx = list(words).index(target_word)
    target_vector = vectors[idx].reshape(1, -1)
    
    similarities = cosine_similarity(target_vector, vectors)[0]
    
    # Get top similar words (excluding itself)
    similar_indices = similarities.argsort()[::-1][1:top_n+1]
    
    print(f"\nTop {top_n} words similar to '{target_word}':")
    for i in similar_indices:
        print(words[i])

# Example usage
find_similar_words("soccer", words, X.T, top_n=5)

Output:
Matplotlib is building the font cache; this may take a moment.



A graph plot while executing


Top 5 words similar to 'soccer':
games
win
on
goals
score

