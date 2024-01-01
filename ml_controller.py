from fastapi import APIRouter, HTTPException, status
from models import Prediction_Input
from models import Prediction_Output
import pickle
import warnings
warnings.filterwarnings("ignore")


with open('model_pickle','rb') as file:
    mp = pickle.load(file)


router = APIRouter()

preds = []

@router.get('/ml')
def get_preds():
    return preds

@router.post('/ml', status_code=status.HTTP_201_CREATED, response_model=Prediction_Output)
def predict(pred_input: Prediction_Input):

    prediction = mp.predict([[pred_input.area]])
    
    prediction_dict = {"id": str(pred_input.id) ,"area": float(pred_input.area) ,"price": float(prediction)}
    preds.append(prediction_dict)

    

    return prediction_dict



