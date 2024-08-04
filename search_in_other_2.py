import pandas as pd
import itertools

# Load the datasets
words_df = pd.read_csv('words.csv')
texts_df = pd.read_csv('texts.csv')

# Create a function to generate permutations of words in a phrase
def generate_permutations(phrase):
    words = phrase.split()
    permutations = [' '.join(p) for p in itertools.permutations(words)]
    return permutations

# Create a function to check for the presence of permutations in the text
def find_permutations_in_text(text, phrases):
    found_phrases = []
    for phrase in phrases:
        permutations = generate_permutations(phrase)
        for perm in permutations:
            if perm.lower() in text.lower():
                found_phrases.append(perm)
                break  # If one permutation is found, no need to check others
    return ', '.join(found_phrases) if found_phrases else 'None'

# Apply the function to the texts dataset
phrases_list = words_df['word'].tolist()
texts_df['found_permutations'] = texts_df['text'].apply(lambda text: find_permutations_in_text(text, phrases_list))

# Save the result to a new CSV file
texts_df.to_csv('texts_with_found_permutations.csv', index=False)

# Display the result
print(texts_df)
