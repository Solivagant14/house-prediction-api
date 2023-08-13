import pickle
import warnings
warnings.filterwarnings('ignore')

from tools import dummify

# load model
filename = "model/houese_predict_model.pickle"
loaded_model = pickle.load(open(filename, "rb"))

def get_prediction(HouseStyle:float,OverallQual:int,GrLivArea:int,GarageArea:int,Neighbourhood:str):
    output = loaded_model.predict([dummify(HouseStyle,OverallQual,GrLivArea,GarageArea,Neighbourhood)])
    return output[0]