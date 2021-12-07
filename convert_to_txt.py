import PyPDF2

yearacl = input("enter a year")

def PDFtoTXT(i):
    pdf = open(f'./'+yearacl+'/PDFs/Document{i}.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    print(pdfReader.numPages)
    for pageno in range(pdfReader.numPages):
        page = pdfReader.getPage(pageno)
        with open(f"./"+yearacl+"/TXTs/Document{i}.txt", "a") as txt:
            try:
                txt.write(page.extractText())
            except UnicodeEncodeError:
                pass

for pdf in range(5):
    PDFtoTXT(pdf)