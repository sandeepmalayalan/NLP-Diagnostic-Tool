#tokenize the word to sequence and doing pad sequence for proper dimension
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.models import Model, Input, Sequential, load_model
from keras.preprocessing.sequence import pad_sequences
data1=data["review"].values
data2=data["label"].values
tokenizer = Tokenizer(num_words=1000)
tokenizer.fit_on_texts(data1)
X = tokenizer.texts_to_sequences(data['review'].values)
X = pad_sequences(X)
