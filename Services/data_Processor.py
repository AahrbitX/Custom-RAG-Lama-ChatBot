
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from data_Extract import DataExtractor

nltk.download("stopwords")
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
                if token.lower() not in self.stop_words:
                    lemmatized_word = self.Lemmatizer.lemmatize(token.lower())
                    lemmatized_sen.append(lemmatized_word)
            self.filtered_tokens.append(lemmatized_sen)

        return self.filtered_tokens

# path="/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project.pdf"





