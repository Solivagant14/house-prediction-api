import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from HouseDetail import HouseDetail

from model import get_prediction

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def index():
    return {'message': "Hello,Dev Nishant"}

@app.get('/{name}')
def get_name(name: str):
    return {'message': f"Hello,Dev {name}"}

@app.post('/predict')
def predict(data:HouseDetail):
    data=data.model_dump()
    output = get_prediction(data['HouseStyle'],data['OverallQual'],data['GrLivArea'],data['GarageArea'],data['Neighbourhood'])
    return {'price':f"{output}"}

if __name__=='__main__':
    uvicorn.run(app,host='127.0,0,1',port=8000)