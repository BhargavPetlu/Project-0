import sqlite3
from fastapi import  FastAPI, HTTPException
from src.model.schemas import *
from src.Authentication import *


"""This is for CRUD Operations for Employee Table"""


def create_employer(employer: Employer):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO EMPLOYEER (emp_id, job_id, name, email, phone, password) VALUES (?, ?, ?, ?, ?, ?)", (employer.emp_id, employer.job_id, employer.name, employer.email, employer.phone, employer.password))

        conn.commit()
        conn.close()

        return "Employeer created successfully"
    except:
        return HTTPException(status_code=500, detail="failed to create employer")

def verify_employer(email:str, password:str):
    conn = sqlite3.connect("revhire.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT email, password FROM EMPLOYEER WHERE email=?", (email,))
    employer = cursor.fetchone()
    conn.close()
    
    return (employer[0] == email) and (employer[1] == password)


def employer_details(emp_id:int):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM EMPLOYEER WHERE emp_id = ?""", (emp_id, ))
        employer = cursor.fetchone()

        conn.commit()
        conn.close()

        return employer
    except:
        return "Employer not found"

def employer_update(emp_id: int, employer: Employer):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE EMPLOYEER SET job_id = ?, name = ?, email = ?, phone = ?, password = ? WHERE emp_id = ?", (employer.job_id, employer.name, employer.email, employer.phone, employer.password, emp_id))

        conn.commit()
        conn.close()

        return "Employer details updated successfully!"
    except:
        return "Error when updating employer."

def employer_delete(emp_id: int):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM EMPLOYEER WHERE emp_id = ?", (emp_id,))

        conn.commit()
        conn.close()

        return "Employer deleted successfully!"
    except:
        return "Error when deleting the employer"