import nltk
nltk.download('punkt')
nltk.download('punkt_tab')

def count_tokens_nltk(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        tokens = nltk.word_tokenize(text)
        return len(tokens)

print(count_tokens_nltk("./book.txt"))