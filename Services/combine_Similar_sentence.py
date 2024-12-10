from sentence_transformers import SentenceTransformer, util
import spacy
from data_Extract import DataExtractor

model =SentenceTransformer("all-MiniLM-L6-v2")
nlp = spacy.load("en_core_web_sm")

topics =["About HTML","About CSS","About JavaScript","About To-Do Application","About Portfolio Application"]

path="/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project.pdf"

dataLoder=DataExtractor(path)

sentences= dataLoder.get_sentences()

def combine_sentences(sentences, threshold=0.6):
    combined_paragraphs =[]
    current_paragraph =sentence =[0]

    for i in range(1,len(sentences)):
        sim = util.cos_sim(model.encode(sentences[i]), model.encode(current_paragraph.split('\n')[-1]))[0][0].item()
    if sim >= threshold:
        current_paragraph+=" "+sentence[i]

    else:
        combined_paragraphs.append(current_paragraph)
        current_paragraph=sentences[i]
    combined_paragraphs.append(current_paragraph)


    return combined_paragraphs

combined_paragraphs =combine_sentences(sentences)

print(combined_paragraphs)