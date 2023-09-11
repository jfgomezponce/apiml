from pydantic import BaseModel

class Task(BaseModel):
    id : int
    task : str
    completed : bool

class Prediction_Input(BaseModel):
    id : int
    text_input : str # Este es el texto del caso del profe

class Prediction_Output(BaseModel):
    id : int
    text_input : str
    pred : float
