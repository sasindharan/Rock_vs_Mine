
import numpy as np
import pandas as pd
import pickle

loaded_model = pickle.load(open('C:/Users/sasin/Downloads/machine learning projects/trained_model.sav', 'rb'))

input_data = (0.0453,0.0523,0.0843,0.0689,0.1183,0.2583,	0.2156,	0.3481,	0.3337,	0.2872,	0.4918,	0.6552,	0.6919,0.7797,0.7464,	0.9444,1,	0.8874,0.8024,0.7818,0.5212,	0.4052,	0.3957,	0.3914,	0.325,	0.32,	0.3271,	0.2767,	0.4423,	0.2028,	0.3788,0.2947,	0.1984,	0.2341,	0.1306,	0.4182,	0.3835,	0.1057,	0.184,	0.197,	0.1674,	0.0583,	0.1401,	0.1628,	0.0621,	0.0203,	0.053,	0.0742,	0.0409,	0.0061,	0.0125,	0.0084,	0.0089,	0.0048,	0.0094,	0.0191,	0.014,	0.0049,	0.0052,	0.0044)

input_data_as_numpy = np.asarray(input_data)

input_reshape = input_data_as_numpy.reshape(1, -1)

prediction = loaded_model.predict(input_reshape)

print(prediction)

if (prediction[0]=='R'):
  print("The object is rock")
else:
  print("The object is mine")