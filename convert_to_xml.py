import pdftables_api

yearacl = input("enter a year")

if yearacl == '2007':
    yearc = 207
elif yearacl == '2008':
    yearc = 219
elif yearacl == '2009':
    yearc = 248

for i in range(1,int(yearc)+1):
     c = pdftables_api.Client('zgj4kmh68dbj')
     c.xml('./'+str(yearacl)+'/PDFs/Document'+str(i)+'.pdf', './'+str(yearacl)+'/XMLs/Document'+str(i)) 
