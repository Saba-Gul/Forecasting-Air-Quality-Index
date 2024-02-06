"""
Created on Wed Dec 15 10:16:47 2021

@author: HP PC
"""

from numpy import array
import tensorflow
from sklearn import preprocessing
import pandas as pd 
import numpy as np
from numpy.random import seed
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
seed(1)
np.random.seed(1)
tensorflow.random.set_seed(1)
import matplotlib.pyplot as plt
# split a univariate sequence into samples
def split_sequence(sequence, n_steps):
	X, y = list(), list()
	for i in range(len(sequence)):
		# find the end of this pattern
		end_ix = i + n_steps
		# check if we are beyond the sequence
		if end_ix > len(sequence)-1:
			break
		# gather input and output parts of the pattern
		seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
		X.append(seq_x)
		y.append(seq_y)
	return array(X), array(y)

"#Reading old data"
"5 previous values"
dataset=
"#Reading real time data"
"#reading current values 
real_time_dataset=
"#combing both"

combined_data=np.append(dataset,real_time_dataset)
combined_data=combined_data.reshape(-1,1)


"#Reshaping in compatible format for LSTM"
test= X.reshape((X.shape[0], X.shape[1], n_features))

"#Loadng saved model"
reconstructed_model = tensorflow.keras.models.load_model("D:/Mehreen/Flood Testing/Flood models/new/brooklyn 6 in 1 out")

"#Making Predictions"
yhat = reconstructed_model .predict(test,verbose=0)

