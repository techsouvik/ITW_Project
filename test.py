from tika import parser # pip install tika

raw = parser.from_file('Document8.pdf')
print(raw['content'])