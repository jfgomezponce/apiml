from fastapi import APIRouter, HTTPException, status
# from models import Prediction_Input, Prediction_Output

from fastapi import FastAPI, File, UploadFile
from starlette.responses import JSONResponse
# import csv

import pickle
import pandas as pd
# import numpy
# from sklearn.ensemble import GradientBoostingClassifier
# from sklearn.preprocessing import StandardScaler

# Load 
MODELO = 'best_model.pkl'
ESCALER = 'normalizador.pkl'

model = pickle.load(open(MODELO, 'rb'))
normalizador = pickle.load(open(ESCALER, 'rb'))

router = APIRouter()
# preds = []


# @router.get('/ml')
# def get_preds():
#     return preds

# @router.post("/ml", status_code=status.HTTP_201_CREATED, response_model=Prediction_Output)
# def predict(pred_input: Prediction_Input): # Esto capta el texto
#     prediction_f = model.predict(normalizador())

@router.post("/uploadfile/")
async def upload_file(file: UploadFile): #, columns: str):
    selected_columns = ['EK', 'SD_DMSNR_Curve', 'Skewness_DMSNR_Curve']
    if file.filename.endswith(".csv"):
        # Leer el archivo CSV y procesarlo con pandas
        df = pd.read_csv(file.file)

        # Obtener las columnas especificadas (suponiendo que se proporcionan como una cadena separada por comas)
        # selected_columns = columns.split(",")
        selected_data = df[selected_columns]

        # Generar predicciones con el modelo
        predictions = model.predict(normalizador.transform(selected_data))

        # Las predicciones pueden ser una lista de números (dependiendo del tipo de problema)
        # Aquí puedes procesar las predicciones como desees
        # En este ejemplo, simplemente las devolvemos como JSON
        return JSONResponse(content={"predictions": predictions.tolist()}, status_code=200)
    else:
        return JSONResponse(content={"error": "El archivo debe ser un archivo CSV"}, status_code=400)