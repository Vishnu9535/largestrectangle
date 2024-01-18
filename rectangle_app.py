from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uvicorn

from largestrectangle import largest_rectangle

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    matrix = Column(String) 
    max_number = Column(Integer)
    max_area = Column(Integer)
    start_time = Column(DateTime)
    end_time = Column(DateTime)

Base.metadata.create_all(bind=engine)

class MatrixRequest(BaseModel):
    matrix: List[List[int]]

class LargestRectangleResponse(BaseModel):
    max_number: int
    max_area: int

@app.post("/largest_rectangle", response_model=LargestRectangleResponse)
def get_largest_rectangle(matrix_request: MatrixRequest):
    start_time = datetime.now()
    matrix = matrix_request.matrix
    max_number, max_area = largest_rectangle(matrix)
    end_time = datetime.now()

    log_request_and_response(matrix, max_number, max_area, start_time, end_time)

    return {"max_number": max_number, "max_area": max_area}

def log_request_and_response(matrix, max_number, max_area, start_time, end_time):
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()

    try:
        log_entry = Log(
            matrix=str(matrix),
            max_number=max_number,
            max_area=max_area,
            start_time=start_time,
            end_time=end_time
        )

        db.add(log_entry)
        db.commit()
    except Exception as e:
        print("Error inserting in database:", e)
        db.rollback()
    finally:
        db.close()
@app.get("/")
def read_root():
    return {"Welcome to the application"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
