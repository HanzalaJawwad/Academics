import nltk
from nltk.util import ngrams
from collections import defaultdict

# Define the sentences
sentences = [
    "The cat sat on the mat",
    "The dog sat on the floor"
]

# Tokenize the sentences
tokenized_sentences = [sentence.split() for sentence in sentences]

# Create a dictionary to store N-gram frequencies
freq_dict = defaultdict(int)
total_grams = 0

# Calculate N-gram frequencies
for sentence in tokenized_sentences:
    for n in range(1, 4):
        grams = list(ngrams(sentence, n))
        for gram in grams:
            freq_dict[gram] += 1
            total_grams += 1

# Define a function to calculate N-gram probabilities
def calculate_probability(sentence, n):
    tokens = sentence.split()
    prob = 1.0

    if n == 1:
        for token in tokens:
            prob *= freq_dict[(token,)] / sum([v for k, v in freq_dict.items() if len(k) == 1])
    else:
        for i in range(len(tokens) - n + 1):
            gram = tuple(tokens[i:i+n])
            context = tuple(tokens[i:i+n-1])

            if n == 2:
                prob *= freq_dict[gram] / freq_dict[context]
            elif n == 3:
                prob *= freq_dict[gram] / freq_dict[context]

    return prob

# Calculate probabilities for the sentences
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")
    for n in range(1, 4):
        prob = calculate_probability(sentence, n)
        print(f"{n}-gram probability: {prob}")
    print()
