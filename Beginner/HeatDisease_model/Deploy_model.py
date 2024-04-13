from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()
#age
# sex
# cp
# trestbps
# chol
# fbs
# restecg
# thalach
# exang
# oldpeak
# slope
# ca
# thal
# target
class model_input(BaseModel):
    age =  int
    cp = int
    trestbps = int
    chol =int
    fbs= int
    restecg= int
    thalach= int
    exang= int
    oldpeak= float
    slope= int
    ca = int
    thal= int


heart_model = pickle.load(open("/Users/ankushwalia/Documents/ML-ALL/HeatDisease_model/Heart_dis_model.sav",'rb'))

@app.post('/heartDis_prediction')
def heartDis_predict(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dic = json.loads(input_data)







