import pdfplumber as pp  # Handle the PDF file
import re

  # Handle regular expressions
# import nltk  # Natural Language Toolkit for text processing
# from nltk.corpus import stopwords  # To remove stopwords
# from nltk.stem import WordNetLemmatizer
# # 
# # Download necessary NLTK data
# nltk.download("stopwords")  # Required internet connection
# nltk.download("wordnet")

# # Initialize lemmatizer
# lemmatizer = WordNetLemmatizer()

# # Read PDF and extract text
# data = ''
# with pp.open("Project.pdf") as pdf:
#     for page in pdf.pages:
#         data += page.extract_text()

# # Preprocessing: Split into sentences
# sentences = data.split('.')  # Split on periods to get individual sentences

# # Remove stopwords, special characters, and lemmatize
# stop_words = set(stopwords.words('english'))  # Use a set for faster lookup
# filtered_tokens = []

# for sentence in sentences:
#     # Remove special characters using regex
#     clean_sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)  # Keep only alphanumeric and spaces
#     # Tokenize the cleaned sentence into words
#     tokens = clean_sentence.split()
#     lemmatized_sen=[]
#     # Filter out stopwords and lemmatize
#     for token in tokens:
#         if token.lower() not in stop_words:  # Convert to lowercase for uniformity
#             lemmatized_word = lemmatizer.lemmatize(token.lower())  # Lemmatize the token
#             lemmatized_sen.append(lemmatized_word)
#     filtered_tokens.append(lemmatized_sen)

# # Print the filtered tokens
# # print(filtered_tokens)





class DataExtractor:

    def __init__(self, file_path):
        self.file_path = file_path
        self.__data =''
    
    def __extract_Pdf_Data(self):
        try:
            with pp.open(self.file_path) as pdf:
                for page in pdf.pages:
                    self.__data += page.extract_text()
            return self.__data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self.file_path}' was not found")
        # except pp.exception.PDFSyntaxError:
        #     raise ValueError(f"unable to process '{self.file_path}'. It may not be a vaild PDF.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occured while reading the PDF:{str(e)}")
    
    def __clean_Paragraph(self,sentence):
        try:
            clean_sentence = re.sub(r'[^a-zA-Z0-9]', ' ',sentence)
            return clean_sentence
        except Exception as e:
            raise RuntimeError(f"An error occures while cleaning the paragraph:{str(e)}")

    def get_sentences(self):
        try: 
            self.__data = self.__extract_Pdf_Data()
            sentences = self.__data.split('.')
            cleaned_sentences = [self.__clean_Paragraph(sentence) for sentence in sentences]
            return cleaned_sentences
        except Exception as e:
            raise RuntimeError(f"An error occured while processing Sentence:{str(e)} ")


path="/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project.pdf"

obj= DataExtractor(path)

data= obj.get_sentences()

print(data)





