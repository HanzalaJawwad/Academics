import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('punkt_tab')
import re

nltk.download('punkt')
nltk.download('stopwords')

def preprocess_text(text):

    # Tokenization
    tokens = word_tokenize(text)
    print("Tokens:", tokens)

    # Filtration
    filtered_tokens = [token for token in tokens if re.match('^[a-zA-Z]+$', token)]
    print("Filtered Tokens:", filtered_tokens)

    # Script Validation (assuming English script)
    validated_tokens = [token for token in filtered_tokens if token.isalpha()]
    print("Validated Tokens:", validated_tokens)

    # Stop Word Removal
    stop_words = set(stopwords.words('english'))
    stop_words_removed = [token for token in validated_tokens if token.lower() not in stop_words]
    print("Stop Words Removed:", stop_words_removed)

    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in stop_words_removed]
    print("Stemmed Tokens:", stemmed_tokens)

    return stemmed_tokens


# Example usage
text = "Hello AIML Students! How are you, Welcome to VTU University which was established in the year 2008, @ Belgaum, Karnataka, India"

preprocessed_text = preprocess_text(text)
print("Preprocessed Text:", preprocessed_text)
