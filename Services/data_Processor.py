
import nltk  # Natural Language Toolkit for text processing
from nltk.corpus import stopwords  # To remove stopwords
from nltk.stem import WordNetLemmatizer
from data_Extract import DataExtractor
# 
# Download necessary NLTK data
nltk.download("stopwords")  # Required internet connection
nltk.download("wordnet")

class DataProcessor:
    def __init__(self,path):
        self.Extractor=DataExtractor(path)
        self.data= self.Extractor.get_sentences()
        self.Lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.filtered_tokens = []

    def Get_Filtered_tokens(self):
        for sentence in self.data:
            lemmatized_sen=[]
            for token in sentence:
                if token.lower() not in self.stop_words:  # Convert to lowercase for uniformity
                    lemmatized_word = self.Lemmatizer.lemmatize(token.lower())  # Lemmatize the token
                    lemmatized_sen.append(lemmatized_word)
            self.filtered_tokens.append(lemmatized_sen)

        return self.filtered_tokens

# path="/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project.pdf"





