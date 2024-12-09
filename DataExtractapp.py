import pdfplumber as pp

with pp.open("Project.pdf") as pdf:
    for page in pdf.pages:
        print(page.extract_text())