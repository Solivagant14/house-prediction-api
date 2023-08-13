from pydantic import BaseModel

class HouseDetail(BaseModel):
    HouseStyle:float
    OverallQual:int
    GrLivArea:int
    GarageArea:int
    Neighbourhood:str