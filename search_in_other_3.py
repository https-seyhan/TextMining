import pandas as pd
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data for tokenization (if not already installed)
nltk.download('punkt')

# Load the datasets
tokens_df = pd.read_csv('tokens.csv')
texts_df = pd.read_csv('texts.csv')

# Tokenize the search tokens
search_tokens = set(tokens_df['token'].str.lower())

# Function to find matching tokens in the text
def find_tokens_in_text(text, tokens):
    # Tokenize the text
    text_tokens = set(word_tokenize(text.lower()))
    # Find intersection of tokens
    found_tokens = tokens.intersection(text_tokens)
    return ', '.join(found_tokens) if found_tokens else 'None'

# Apply the function to the texts dataset
texts_df['found_tokens'] = texts_df['text'].apply(lambda text: find_tokens_in_text(text, search_tokens))

# Save the result to a new CSV file
texts_df.to_csv('texts_with_found_tokens.csv', index=False)

# Display the result
print(texts_df)
