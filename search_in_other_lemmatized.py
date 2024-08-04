import pandas as pd
import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Load datasets
words_df = pd.read_csv('words.csv')
texts_df = pd.read_csv('texts.csv')

# Function to lemmatize words using SpaCy
def lemmatize_words(text):
    doc = nlp(text)
    return [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_stop]

# Tokenize and lemmatize words in words_df
words_df['lemmatized_word'] = words_df['word'].apply(lambda x: lemmatize_words(x)[0] if lemmatize_words(x) else x)

# Flatten the list of lemmatized words into a set for quick lookup
lemmatized_words_set = set(words_df['lemmatized_word'])

# Function to find matches in a given row
def find_lemmatized_words_in_row(row, lemmatized_words_set):
    found_words = set()
    for col in row.index:
        text = row[col]
        if isinstance(text, str):
            doc = nlp(text)
            tokens = [token.lemma_.lower() for token in doc if not token.is_punct and not token.is_stop]
            found_words.update(set(tokens) & lemmatized_words_set)
    return ', '.join(found_words) if found_words else 'None'

# Apply the function to each row in texts_df
texts_df['found_words'] = texts_df.apply(lambda row: find_lemmatized_words_in_row(row, lemmatized_words_set), axis=1)

# Save results to a new CSV file
texts_df.to_csv('texts_with_found_words.csv', index=False)

# Display the result
print(texts_df)
