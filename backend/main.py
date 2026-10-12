from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import get_db
from models import WorkoutSet as WorkoutSetModel

from datetime import date

app = FastAPI()





@app.get("/")
def home():
    return {"message": "Welcome to GymOS!"}


@app.get("/hello")
def hello():
    return {"message": "GymOS API is working!"}


class WorkoutSet(BaseModel):
    workout_date: date
    exercise: str
    set_number: int
    weight: float
    reps: int
    rir: int | None = None
    notes: str | None = None

@app.post("/sets")
def create_set(
    workout_set: WorkoutSet,
    db: Session = Depends(get_db)
):
    new_set = WorkoutSetModel(
    workout_date=workout_set.workout_date,
    exercise=workout_set.exercise,
    set_number=workout_set.set_number,
    weight=workout_set.weight,
    reps=workout_set.reps,
    rir=workout_set.rir,
    notes=workout_set.notes
)

    db.add(new_set)
    db.commit()
    db.refresh(new_set)

    return {
        "message": "Workout set saved!",
        "data": new_set
    }


class WorkoutSetResponse(BaseModel):
    id: int
    workout_date: date
    exercise: str
    set_number: int
    weight: float
    reps: int
    rir: int | None
    notes: str | None
    class Config:
        from_attributes = True

@app.get("/sets", response_model=list[WorkoutSetResponse])
def get_sets(db: Session = Depends(get_db)):
    return db.query(WorkoutSetModel).all()
