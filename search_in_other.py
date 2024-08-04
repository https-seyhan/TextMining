import pandas as pd

id,word
1,apple
2,banana
3,grape


id,text
1,I have an apple and a banana.
2,Grapes are sour.
3,Apple pie is delicious.


# Load the datasets
words_df = pd.read_csv('words.csv')
texts_df = pd.read_csv('texts.csv')

# Create a function to check for the presence of words in the text
def find_words_in_text(text, words):
    found_words = [word for word in words if word.lower() in text.lower()]
    return ', '.join(found_words) if found_words else 'None'

# Apply the function to the texts dataset
words_list = words_df['word'].tolist()
texts_df['found_words'] = texts_df['text'].apply(lambda text: find_words_in_text(text, words_list))

# Save the result to a new CSV file
texts_df.to_csv('texts_with_found_words.csv', index=False)

# Display the result
print(texts_df)


   id                        text      found_words
0   1  I have an apple and a banana.  apple, banana
1   2             Grapes are sour.           grape
2   3        Apple pie is delicious.           apple
