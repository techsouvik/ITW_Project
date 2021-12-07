import PyPDF2

yearacl = input("enter a year")

if yearacl == '2007':
    yearc = 207
elif yearacl == '2008':
    yearc = 219
elif yearacl == '2009':
    yearc = 248

# yearc = [207,219,248]
def PDFtoTXT(i,acl):
    pdf = open(f'./'+acl+'/PDFs/Document'+str(i)+'.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdf)
    print(pdfReader.numPages)
    for pageno in range(pdfReader.numPages):
        page = pdfReader.getPage(pageno)
        with open(f"./"+acl+"/TXTs/Document"+str(i)+".txt", "a") as txt:
            try:
                txt.write(page.extractText())
            except UnicodeEncodeError:
                pass

for pdf in range(1,int(yearc)+1):
    PDFtoTXT(pdf,yearacl)