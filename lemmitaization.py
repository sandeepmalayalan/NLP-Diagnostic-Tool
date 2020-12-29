import nltk
from nltk.stem import WordNetLemmatizer 
lemmatizer = WordNetLemmatizer()
lemmatize1=[]
for word in list2:
  l=""
  word=word.split(" ")
  for i in word:
    l=l+(lemmatizer.lemmatize(i))+" "
  lemmatize1.append(l)
print(lemmatize1[0:3])
