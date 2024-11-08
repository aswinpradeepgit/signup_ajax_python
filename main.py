from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
from mysql.connector import Error

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# data model for the form
class SignupData(BaseModel):
    firstname: str
    lastname: str
    email: str
    company: str

# Database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Done",
            password="nurburgring",
            database="done_database"
        )
        return connection
    except Error as e:
        print("Error while connecting to MySQL", e)
        return None


# API endpoint to receive signup data
@app.post("/signup")
async def signup(data: SignupData):
    connection = None
    cursor = None
    try:
        connection = get_db_connection()
        if connection is None:
            raise HTTPException(status_code=500, detail="Could not connect to the database")

        cursor = connection.cursor()

        # Insert data into your MySQL table
        query = "INSERT INTO users (firstname, lastname, email, company) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (data.firstname, data.lastname, data.email, data.company))
        connection.commit()
        
        return {"message": "Signup successful!"}
    except Error as e:
        raise HTTPException(status_code=500, detail="Signup failed")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

