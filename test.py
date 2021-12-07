pt = "Document2.txt"
def my_function():


  with open(pt,'r') as f, open('output.txt','w') as fw:
      text = f.read()
      result_string = '<paper id ='+pt[-5]+'><Extractive Summary>'
          
      words = ["Table 1","Table 2"]
      text2 = text.split(".")
      for itemIndex in range(len(text2)):
          for word in words:
              if word in text2[itemIndex]:
                  if text2[itemIndex][0] ==' ':
                      print(text2[itemIndex][1:])
                      result_string += text2[itemIndex][1:]+'. '
                      break
                  else:
                      print(text2[itemIndex])
                      result_string += text2[itemIndex]
                      break
      result_string += '</Extractive Summary></paper id ='+pt[-5]+'>'
      print(result_string)
      fw.write(result_string)

my_function()