import numpy as np

neighbourhood_rev_index = {'Blmngtn': 0,
                            'Blueste': 1,
                            'BrDale': 2,
                            'BrkSide': 3,
                            'ClearCr': 4,
                            'CollgCr': 5,
                            'Crawfor': 6,
                            'Edwards': 7,
                            'Gilbert': 8,
                            'IDOTRR': 9,
                            'MeadowV': 10,
                            'Mitchel': 11,
                            'NAmes': 12,
                            'NPkVill': 13,
                            'NWAmes': 14,
                            'NoRidge': 15,
                            'NridgHt': 16,
                            'OldTown': 17,
                            'SWISU': 18,
                            'Sawyer': 19,
                            'SawyerW': 20,
                            'Somerst': 21,
                            'StoneBr': 22,
                            'Timber': 23,
                            'Veenker': 24}

def dummify(HouseStyle:float,OverallQual:int,GrLivArea:int,GarageArea:int,Neighbourhood:str):
    temp_list=list(np.zeros(25,dtype=int))
    temp_list[neighbourhood_rev_index[Neighbourhood]]=1

    return [HouseStyle,OverallQual,GrLivArea,GarageArea]+temp_list

