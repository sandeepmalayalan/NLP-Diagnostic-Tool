list2=[]
l5=[]
for (i,j) in zip(list1,fin["name"]):
  if i!=" " and i!="":
    if detect(i)=="en":
      list2.append(i)
      l5.append(j)
print(len(list2),"total reviews after language detection")
print(len(l5))
