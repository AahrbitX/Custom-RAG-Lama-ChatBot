import pdfplumber as pp  # Handle the PDF file
import re  # Handle regular expressions
import nltk  # Natural Language Toolkit for text processing
from nltk.corpus import stopwords  # To remove stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download("stopwords")  # Required internet connection
nltk.download("wordnet")

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Read PDF and extract text
data = ''
with pp.open("Project.pdf") as pdf:
    for page in pdf.pages:
        data += page.extract_text()

# Preprocessing: Split into sentences
sentences = data.split('.')  # Split on periods to get individual sentences

# Remove stopwords, special characters, and lemmatize
stop_words = set(stopwords.words('english'))  # Use a set for faster lookup
filtered_tokens = []

for sentence in sentences:
    # Remove special characters using regex
    clean_sentence = re.sub(r'[^a-zA-Z0-9\s]', '', sentence)  # Keep only alphanumeric and spaces
    # Tokenize the cleaned sentence into words
    tokens = clean_sentence.split()
    lemmatized_sen=[]
    # Filter out stopwords and lemmatize
    for token in tokens:
        if token.lower() not in stop_words:  # Convert to lowercase for uniformity
            lemmatized_word = lemmatizer.lemmatize(token.lower())  # Lemmatize the token
            lemmatized_sen.append(lemmatized_word)
    filtered_tokens.append(lemmatized_sen)

# Print the filtered tokens
print(filtered_tokens)
