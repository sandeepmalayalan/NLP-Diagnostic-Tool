# Save lstm model to json file
from keras.models import model_from_json

# Writing weights to json file
model_json = model.to_json()
with open("model.json", "w") as file:
    file.write(model_json)
model.save_weights("weight.h5")
print("model has been saved to disk")

# load weights into new model from the json file
json = open('model.json', 'r')
json_read = json.read()
json.close()
loaded_model = model_from_json(json_read)
loaded_model.load_weights("weight.h5")
print("Model has loaded from the disk",loaded_model.summary())
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
score,acc = loaded_model.evaluate(X_test1, Y_test1, verbose=1)
print(acc*100)
