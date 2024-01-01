from pydantic import BaseModel

class Task(BaseModel):
    id: int
    task: str
    completed: bool


class Prediction_Input(BaseModel):
    id: int
    area: int

class Prediction_Output(BaseModel):
    id: int
    area: int
    price: float