import pdfplumber as pp
import re


data=''

with pp.open("Project.pdf") as pdf:
    for page in pdf.pages:
        data=page.extract_text()

# print(data.split(' '))

c_data=[]


for token in data.split():
     c_data.append(re.sub(r'[^a-zA-z0-9]','',token.lower()))


print(c_data)