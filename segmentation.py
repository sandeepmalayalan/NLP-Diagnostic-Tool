#making words for pos and neg seg
def process_data(k,a):
  text_phrases=[]
  p = pd.DataFrame(columns=["word"])
  n = pd.DataFrame(columns=["word"])
  bigrams = nltk.collocations.BigramAssocMeasures()
  for i in k["word"].values:
    k=i.split()
    text_phrases.extend(k)
    bigramFinder = nltk.collocations.BigramCollocationFinder.from_words(text_phrases)
  bigramFinder.apply_freq_filter(0)
  bigram_freq = bigramFinder.ngram_fd.items()
  if a==1:
    bigramFreqTable = pd.DataFrame(list(bigram_freq), columns=['bigram','freq']).sort_values(by='freq', ascending=False)
    positive = bigramFreqTable[bigramFreqTable.bigram.map(lambda x: Bigram(x))]
    pos_list=[]
    s=""
    if len(positive["bigram"])>0:
      for i in positive["bigram"].values:
        s=i[0]+"_"+i[1]
        pos_list.append(s)
    return pos_list
  elif a==0:
    bigramFreqTable1 = pd.DataFrame(list(bigram_freq), columns=['bigram','freq']).sort_values(by='freq', ascending=False)
    negative = bigramFreqTable1[bigramFreqTable1.bigram.map(lambda x: Bigram(x))]
    neg_list=[]
    s=""
    if len(negative["bigram"])>0:
      for i in negative["bigram"].values:
        s=i[0]+"_"+i[1]
        neg_list.append(s)
    return neg_list
#function to filter for ADJ/NN bigrams
def Bigram(word):
    acceptable_types = ('JJ', 'JJR', 'JJS')
    second_type = ('NN', 'NNS', 'NNP', 'NNPS')
    tags = nltk.pos_tag(word)
    if (tags[0][1] in acceptable_types and tags[1][1] in second_type) or (tags[0][1] in second_type and tags[1][1] in acceptable_types):
      if (tags[0][1] != tags[1][1]):
        return True
      else:
        return False
    else:
        return False
#for training data
pos_list=process_data(pos,1)
neg_list=process_data(neg,0)
#for testing data
pos1_list=process_data(pos1,1)
neg1_list=process_data(neg1,0)
#combining both data
all_pos=pos_list+pos1_list
all_neg=neg_list+neg1_list
print("PosBigram",all_pos[0:2])
print("NegBigram",all_neg[0:2])
