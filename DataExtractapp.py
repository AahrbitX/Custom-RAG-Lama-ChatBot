import pdfplumber as pp # --> handle the pdf file 
import re #--> handle the regular expression 
import nltk #---> natural langiuage tool kit for text processing
from nltk.corpus import stopwords # to rmove sopwords from the image
from nltk.stem import WordNetLemmatizer

nltk.download("stopwords") #----> rquired internet connection
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
data=''

with pp.open("Project.pdf") as pdf:
    for page in pdf.pages:
        data=page.extract_text()

# print(data.split(' '))

c_data=[]


for token in data.split():
     c_data.append(re.sub(r'[^a-zA-z0-9]','',token.lower()))

# print(c_data)


stop_words = stopwords.words('english')


filter_tokens = [w for w in c_data if w not in stop_words]

lemmatized_words = [lemmatizer.lemmatize(w) for w in filter_tokens]

print(lemmatized_words)


