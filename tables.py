import sqlite3

con = sqlite3.connect("revhire.db")

cursor = con.cursor()

# User's Table

cursor.execute(
   """CREATE TABLE USER(
       user_id INTEGER(10) PRIMARY KEY,
       name VARCHAR NOT NULL,
       email VARCHAR UNIQUE,
       password VARCHAR(20) NOT NULL,
       Mobile INTEGER(10) UNIQUE
   )""")

# Employer Table

cursor.execute(
    """
    CREATE TABLE EMPLOYEER(
        emp_id INTEGER(10) PRIMARY KEY,
        job_id INTEGER(10) REFERENCES JOBAPPLICATION(job_id),
        name VARCHAR NOT NULL, 
        email VARCHAR UNIQUE,
        phone INTEGER UNIQUE,
        password VARCHAR NOT NULL
    )""")


# JobPosting Table

cursor.execute(
    """
    CREATE TABLE JOBPOSTING(
        job_id INTEGER(10) PRIMARY KEY, 
        role VARCHAR NOT NULL,
        company VARCHAR NOT NULL,
        email VARCHAR NOT NULL UNIQUE,
        emp_id INTEGER(10) NOT NULL REFERENCES EMPLOYEER(emp_id)
    )""")

# JobAplication Table

cursor.execute(
    """
    CREATE TABLE JOBAPPLICATION(
        job_id INTEGER(10) PRIMARY KEY, 
        user_id INTEGER(10) REFERENCES USER(user_id),
        resume VARCHAR NOT NULL UNIQUE,
        skills VARCHAR NOT NULL
    )""")

con.commit()

con.close()
