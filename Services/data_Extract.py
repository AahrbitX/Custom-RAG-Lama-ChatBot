import pdfplumber as pp  # Handle the PDF file
import re

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
            clean_sentence=re.sub(' +',' ', clean_sentence)
            clean_sentence=clean_sentence.strip()
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



if __name__=="__main__":
    path="/home/ghost/Documents/My_projects/Business_Projects/Products/Custom-RAG-Lama-ChatBot/Services/Project.pdf"

    obj= DataExtractor(path)

    print(obj.get_sentences())