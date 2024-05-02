import pandas as pd
import nltk
nltk.download('punkt')

# STOPWORDS
nltk.download("stopwords")

from nltk.corpus import stopwords

stop_words = stopwords.words("english")

stop_words

# STEMING
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

stemmer = PorterStemmer()
str1= "There are so many players in ground"
str2= nltk.word_tokenize(str1)
str1

# LAMITIZATION
nltk.download("wordnet")

from nltk.stem import WordNetLemmatizer

from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

str1 = "Playing cricket and Singing songs and in that corner there are so many mice."

str1 = nltk.word_tokenize(str1)

str1

for word in str1:
    print(lemmatizer.lemmatize(word))


