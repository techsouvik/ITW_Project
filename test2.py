import re
pt = 'Document2.txt'
text = ''
with open(pt,'r') as f, open('output.txt','w') as fw:
     text = f.read()
patt = re.compile(r'Table \d')

matches = patt.finder(text)

for match in matches:
     print(match)