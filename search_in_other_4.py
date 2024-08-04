import pandas as pd
import spacy

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Load the datasets
words_df = pd.read_csv('words.csv')
texts_df = pd.read_csv('texts.csv')

# Tokenize words from the words dataset
words_list = words_df['word'].tolist()
tokenized_words = set([token.text.lower() for token in nlp(' '.join(words_list)).ents])

# Function to find tokens in text across multiple columns
def find_tokens_in_row(row, tokenized_words):
    found_vars = []
    for col_name, text in row.iteritems():
        if col_name != 'id':  # Skip the 'id' column
            doc = nlp(text)
            tokens = set([token.text.lower() for token in doc])
            if tokenized_words.intersection(tokens):
                found_vars.append(col_name)
    return ', '.join(found_vars) if found_vars else 'None'

# Apply the function to each row in the texts DataFrame
texts_df['found_variables'] = texts_df.apply(lambda row: find_tokens_in_row(row, tokenized_words), axis=1)

# Save the result to a new CSV file
texts_df.to_csv('texts_with_found_variables.csv', index=False)

# Display the result
print(texts_df)
