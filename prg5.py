import random 
import gensim.downloader as api 
# Load pre-trained word embedding model 
model = api.load("glove-wiki-gigaword-50") 
def get_similar_words(seed_word, top_n=5): 
"""Retrieve similar words for the given seed word.""" 
try: 
similar_words = [word for word, _ in model.most_similar(seed_word, topn=top_n)] 
return similar_words 
except KeyError: 
return [] 
def create_paragraph(seed_word): 
"""Generate a short paragraph using the seed word and its similar words.""" 
similar_words = get_similar_words(seed_word) 
if not similar_words: 
return f"Could not find similar words for '{seed_word}'. Try another word!" 
paragraph = ( 
f"Once upon a time, a {seed_word} embarked on a journey. Along the way, it 
encountered " 
f"a {random.choice(similar_words)}, which led it to a hidden 
{random.choice(similar_words)}. " 
f"Despite the challenges, it found {random.choice(similar_words)} and embraced the " 
f"adventure with {random.choice(similar_words)}. In the end, the journey was a tale of 
" 
f"{random.choice(similar_words)} and discovery." 
) 
return paragraph 
seed_word = input("Enter a seed word: ").strip().lower() 
print("\nGenerated Story:\n") 
print(create_paragraph(seed_word)) 
21 
Output: 
Enter a seed word:  forest 
Generated Story: 
Once upon a time, a forest embarked on a journey. Along the way, it encountered a wildlife, 
which led it to a hidden woodland. Despite the challenges, it found woodland and embraced 
the adventure with wildlife. In the end, the journey was a tale of woodlands and discovery. 
