import numpy as np
from keras.models import load_model
from keras.preprocessing import sequence
import json
import keras


def predict_score(test_sequence):
   max_sequence_length = 200
   model = load_model('./my_model.h5')
   with open('./word_integer_map.json') as f:
      word_to_id = json.load(f)

   temp = []
   for word in test_sequence.split(" "):
      temp.append(word_to_id[word])
   temp_padded = sequence.pad_sequences([temp], maxlen=max_sequence_length)
   pred_score = model.predict(np.array([temp_padded][0]))[0][0]
   return pred_score * 100
