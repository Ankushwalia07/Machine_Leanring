import numpy as np
import pickle
import streamlit

load_model = pickle.load(open('/Users/ankushwalia/Documents/ML-ALL/Diabeties_ML_model.sav','rb'))
#feeding the data here

#creating a fucntion for prediction
def diabetes_prediction(input_data):
    input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

    # making it as a numpy array
    input_data_num = np.asarray(input_data)

    # reshapping the array
    input_reshape = input_data_num.reshape(1, -1)

    # we cannot feed the data as it is as we have to standardize it
    # making prediciton
    prediction = load_model.predict(input_reshape)
    print(prediction)

    if (prediction[0] == 0):
        return "The person is not Diabetic"
    else:
        return "The Person is Diabetic"

def main():
    streamlit.title("Diabeties Prediction Interface")

    Pregnancies = streamlit.text_input("Number of Pregnancies")
    Glucose = streamlit.text_input("Glucose Level")
    BloodPressure = streamlit.text_input("Blood Pressure Value")
    SkinThickness = streamlit.text_input("Skin Thickenss")
    InsulinLevel = streamlit.text_input("Insulin Level")
    BMI = streamlit.text_input("BMI Value")
    DiabeticPedigree = streamlit.text_input("Diabetic Pedigree Function Value")
    Age = streamlit.text_input("Age of the Women")


    dignosis = ""

    if streamlit.button('Diabetes Test Result'):
        dignosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,InsulinLevel,BMI,DiabeticPedigree,Age])

    streamlit.success(dignosis)

if __name__ == '__main__':
    main()
