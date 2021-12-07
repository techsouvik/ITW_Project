from tika import parser # pip install tika
from pathlib import Path
import re

yearacl = input("enter a year")

if yearacl == '2007':
    yearc = 207
elif yearacl == '2008':
    yearc = 219
elif yearacl == '2009':
    yearc = 248


for i in range(1,yearc):
     raw = parser.from_file('./'+yearacl+'/PDFs/Document'+str(i)+'.pdf')
     a = raw['content']
     with Path('./'+yearacl+'/TXTs/Document'+str(i)+'.txt').open(mode='w') as output_file:
          output_file.write(a)