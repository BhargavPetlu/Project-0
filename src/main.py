import sqlite3
from fastapi import FastAPI, HTTPException
from model.shemas import User, Employee, JobApplication, JobPosting

app = FastAPI()


@app.post("/users")
def create_user(user: User):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO USER(user_id, name, email, password, mobile) VALUES (?, ?, ?, ?, ?)""", 
                       (user.user_id, user.name, user.email, user.password, user.mobile)
                       )

        conn.commit()
        conn.close()

        return {"message": "User created successfully"}
    except:
        raise HTTPException(status_code=500, detail="failed to create user")

@app.get("/users/user_id")
def get_user(user_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("""SELECT * FROM USER WHERE user_id = ?""", (user_id,))
        user = cursor.fetchone()

        conn.close()

        return {"user": user}
    except:
        return "No user found with that ID."

@app.put("/users/user_id")
def update_user(user_id: int, user: User):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE USER SET name = ?, email = ?, password = ?, mobile = ? WHERE user_id = ?", 
                       (user.name, user.email, user.password, user.mobile, user_id))

        conn.commit()
        conn.close()

        return {"message": "User updated successfully"}
    except:
        return "Error updating the user."

@app.delete("/users/user_id")
def delete_user(user_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM USER WHERE user_id = ?", (user_id,))

        conn.commit()
        conn.close()

        return {"message": "User deleted successfully"}
    except:
        return "Error deleting the user."


@app.post("/employeers")
def create_employeer(employeer: Employee):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO EMPLOYEER (emp_id, job_id, name, email, phone, password) VALUES (?, ?, ?, ?, ?, ?)", (employeer.emp_id, employeer.job_id, employeer.name, employeer.email, employeer.phone, employeer.password))

        conn.commit()
        conn.close()

        return {"message": "Employeer created successfully"}
    except:
        return "Error creating employeer."

@app.get("/employeers/emp_id")
def get_employeer(emp_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM EMPLOYEER WHERE emp_id = ?", (emp_id,))
        employeer = cursor.fetchone()

        conn.close()

        return {"employeer": employeer}
    except:
        return "Employee not found"

@app.put("/employeers/emp_id")
def update_employeer(emp_id: int, employeer: Employee):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE EMPLOYEER SET job_id = ?, name = ?, email = ?, phone = ?, password = ? WHERE emp_id = ?", (employeer.job_id, employeer.name, employeer.email, employeer.phone, employeer.password, emp_id))

        conn.commit()
        conn.close()

        return {"message": "Employeer updated successfully"}
    except:
        return "Error updating employee."

@app.delete("/employeers/emp_id")
def delete_employeer(emp_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM EMPLOYEER WHERE emp_id = ?", (emp_id,))

        conn.commit()
        conn.close()

        return {"message": "Employeer deleted successfully"}
    except:
        return "Error deleting employee."



@app.post("/job_postings")
def create_job_posting(job_posting: JobPosting):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBPOSTING (job_id, role, company, email, emp_id) VALUES (?, ?, ?, ?, ?)", (job_posting.job_id, job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id))

        conn.commit()
        conn.close()

        return {"message": "Job posting created successfully"}
    except:
        return "Error creating job posting."

@app.get("/job_postings/job_id")
def get_job_posting(job_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBPOSTING WHERE job_id = ?", (job_id,))
        job_posting = cursor.fetchone()

        conn.close()

        return {"job_posting": job_posting}
    except:
        return "Error getting job posting."

@app.put("/job_postings/job_id")
def update_job_posting(job_id: int, job_posting: JobPosting):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBPOSTING SET role = ?, company = ?, email = ?, emp_id = ? WHERE job_id = ?", (job_posting.role, job_posting.company, job_posting.email, job_posting.emp_id, job_id))

        conn.commit()
        conn.close()

        return {"message": "Job posting updated successfully"}
    except:
        return "Error updating job posting."

@app.delete("/job_postings/job_id")
def delete_job_posting(job_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBPOSTING WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return {"message": "Job posting deleted successfully"}
    except:
        return "Error deleting job posting."


@app.post("/job_applications")
def create_job_application(job_application: JobApplication):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO JOBAPPLICATION (job_id, user_id, resume, skills) VALUES (?, ?, ?, ?)", (job_application.job_id, job_application.user_id, job_application.resume, job_application.skills))

        conn.commit()
        conn.close()

        return {"message": "Job application created successfully"}
    except:
        return "Error creating job application."

@app.get("/job_applications/job_id")
def get_job_application(job_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))
        job_application = cursor.fetchone()

        conn.close()

        return {"job_application": job_application}
    except:
        return  "No job applications found for that ID."

@app.put("/job_applications/job_id")
def update_job_application(job_id: int, job_application: JobApplication):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("UPDATE JOBAPPLICATION SET user_id = ?, resume = ?, skills = ? WHERE job_id = ?", (job_application.user_id, job_application.resume, job_application.skills, job_id))

        conn.commit()
        conn.close()

        return {"message": "Job application updated successfully"}
    except:
        return "Error updating job application."

@app.delete("/job_applications/job_id")
def delete_job_application(job_id: int):
    try:
        conn = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM JOBAPPLICATION WHERE job_id = ?", (job_id,))

        conn.commit()
        conn.close()

        return {"message": "Job application deleted successfully"}
    except:
        return "Error deleting job application."