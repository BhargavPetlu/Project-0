from fastapi import FastAPI
from model.schemas import *
from CRUD import employer, jobapplication, jobposting, users
from Authentication import encoding_decoding_jwt


app = FastAPI()


@app.post("/users/signup")
def create_user(user: User):
    res = users.create_user(user)
    
    return res

@app.post("/users/login")
def user_login(user:Login):
    if users.login_user(user.email, user.password):
        return encoding_decoding_jwt.encode_jwt(user.email, user.password)
    else:
        return "Invalid Login Details! Please try again with correct credentials."

@app.get("/users/get")
def get_user(user_id: int):
    res = users.get_user(user_id)
    
    return res

@app.put("/users/update")
def update_user(user_id: int, user: User):
    res = users.update_user(user_id, user)
    
    return res

@app.delete("/users/delete")
def delete_user(user_id: int):
    res = users.delete_user(user_id)
    
    return res


"""This is for CRUD Operations for Employer Table"""


@app.post("/employers/signup")
def create_employer(employers: Employer):
    res = employer.create_employer(employers)
    
    return res

@app.post("/employers/login")
def employer_login(employers:Login):
    if employer.verify_employer(employers.email, employers.password):
        return encoding_decoding_jwt.encode_jwt(employers.email, employers.password)
    else:
        return "Invalid Login Details! Please try again with correct credentials."

@app.get("/employers/get")
def get_employeer(emp_id: int):
    res = employer.employer_details(emp_id)
    
    return res

@app.put("/employers/update")
def update_employer(emp_id: int, employers: Employer):
    res = employer.employer_update(emp_id, employers)
    
    return res

@app.delete("/employees/delete")
def delete_employer(emp_id: int):
    res = employer.employer_delete(emp_id)

    return res


"""This is for CRUD Operations for JobPosting"""


@app.post("/job_postings/create")
def create_job_posting(job_posting: JobPosting):
    res = jobposting.create_job_posting(job_posting)
    
    return res

@app.get("/job_postings/get")
def get_job_posting(job_id: int):
    res = jobposting.job_posting_details(job_id)
    
    return res

@app.put("/job_postings/update")
def update_job_posting(job_id: int, job_posting: JobPosting):
    res = jobposting.update_job_posting(job_id, job_posting)
    
    return res

@app.delete("/job_postings/delete")
def delete_job_posting(job_id: int):
    res = jobposting.delete_job_posting(job_id)
    
    return res


"""This is for CRUD Operations for JobApplication"""


@app.post("/job_applications/create")
def create_job_application(job_application: JobApplication):
    res = jobapplication.create_job_application(job_application)
    
    return res

@app.get("/job_applications/get")
def get_job_application(job_id: int):
    res = jobapplication.get_job_application(job_id)
    
    return res

@app.put("/job_applications/update")
def update_job_application(job_id: int, job_application: JobApplication):
    res = jobapplication.update_job_application(job_id, job_application)
    
    return res

@app.delete("/job_applications/delete")
def delete_job_application(job_id: int):
    res = jobapplication.delete_job_application(job_id)
    
    return res