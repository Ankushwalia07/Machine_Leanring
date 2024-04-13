import numpy as np
import pickle
load_model = pickle.load(open('/Users/ankushwalia/Documents/ML-ALL/Diabeties_ML_model.sav','rb'))
#feeding the data here
input_data =(5,166,72,19,175,25.8,0.587,51)

#making it as a numpy array
input_data_num = np.asarray(input_data)

#reshapping the array
input_reshape = input_data_num.reshape(1,-1)

#we cannot feed the data as it is as we have to standardize it
#making prediciton
prediction = load_model.predict(input_reshape)
print(prediction)

if (prediction[0]==0):
    print("The person is not Diabetic")
else:
    print("The Person is Diabetic")