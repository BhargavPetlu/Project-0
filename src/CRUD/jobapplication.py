import sqlite3
from model.schemas import *
from fastapi import HTTPException


def create_job_application(job_application: JobApplication):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBAPPLICATION (job_id, user_id, resume, skills) VALUES (?, ?, ?, ?)", (job_application.job_id, job_application.user_id, job_application.resume, job_application.skills))

        conn.commit()
        conn.close()

        return "Job application Sent successfully!"
    except:
        return HTTPException(status_code=500, detail="failed to Apply a Job")


def get_job_application(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))
        job_application = cursor.fetchone()

        conn.close()

        return job_application
    except:
        return  "No job applications found for that ID."

def update_job_application(job_id: int, job_application: JobApplication):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBAPPLICATION SET user_id = ?, resume = ?, skills = ? WHERE job_id = ?", (job_application.user_id, job_application.resume, job_application.skills, job_id))

        conn.commit()
        conn.close()

        return "Job application updated successfully!"
    except:
        return "Error updating job application."

def delete_job_application(job_id: int):
    try:
        conn = sqlite3.connect("../revhire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return "Job application deleted successfully"
    except:
        return "Error deleting job application."