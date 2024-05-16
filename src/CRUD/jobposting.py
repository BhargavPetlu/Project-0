import sqlite3
from fastapi import HTTPException
from src.model.schemas import *


def create_job_posting(job_posting: JobPosting):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBPOSTING (job_id, role, company, email, emp_id) VALUES (?, ?, ?, ?, ?)", (job_posting.job_id, job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id))

        conn.commit()
        conn.close()

        return "Job posting created successfully"
    except:
        return HTTPException(status_code=500, detail="failed to Create a Job Post")

def job_posting_details(job_id: int):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBPOSTING WHERE job_id = ?", (job_id,))
        job_posting = cursor.fetchone()

        conn.close()

        return {"job_posting": job_posting}
    except:
        return "Error getting job posting details."

def update_job_posting(job_id: int, job_posting: JobPosting):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBPOSTING SET role = ?, company = ?, email = ?, emp_id = ? WHERE job_id = ?", (job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id, job_id))

        conn.commit()
        conn.close()

        return "Job posting updated successfully"
    except:
        return "Error updating job posting."

def delete_job_posting(job_id: int):
    try:
        conn = sqlite3.connect("revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBPOSTING WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return "Job posting deleted successfully"
    except:
        return "Error deleting job posting."