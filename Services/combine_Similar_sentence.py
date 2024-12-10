from sentence_transformers import SentenceTransformer, util
import spacy
from data_Extract import DataExtractor

# Load models
model = SentenceTransformer("all-MiniLM-L6-v2")
nlp = spacy.load("en_core_web_sm")

# Topics and file path
topics = ["About HTML", "About CSS", "About JavaScript", "About To-Do Application", "About Portfolio Application"]
path = "/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project_srm.pdf"

# Load data
dataLoader = DataExtractor(path)
sentences = dataLoader.get_sentences()

# Function to combine similar sentences
def combine_sentences(sentences, threshold=0.4):
    combined_paragraphs = []  # Initialize as a list
    current_paragraph = ""  # Initialize as an empty string

    for i in range(len(sentences)):
        if not current_paragraph:  # If the current paragraph is empty
            current_paragraph = sentences[i]
        else:
            # Calculate similarity between the current sentence and the last sentence in the paragraph
            last_sentence = current_paragraph.split('\n')[-1]  # Get the last sentence
            sim = util.cos_sim(model.encode(sentences[i]), model.encode(last_sentence))[0][0].item()

            if sim >= threshold:
                current_paragraph += " " + sentences[i]  # Append the sentence to the current paragraph
            else:
                combined_paragraphs.append(current_paragraph.strip())  # Save the current paragraph
                current_paragraph = sentences[i]  # Start a new paragraph

    # Add the last paragraph
    if current_paragraph:
        combined_paragraphs.append(current_paragraph.strip())

    return combined_paragraphs

# Combine sentences
combined_paragraphs = combine_sentences(sentences)

# Print the combined paragraphs
print(combined_paragraphs)
