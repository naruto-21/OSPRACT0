# using NLTK
import nltk
nltk.download('punkt')
text="this ia an example"
token=nltk.word_tokenize(text)
print(token)


# using simple python

text="What is largest animal"
print(text.split())