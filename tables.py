import sqlite3

con = sqlite3.connect("C:/Users/bharg/OneDrive/Desktop/Project-0/rev_hire.db")

cursor = con.cursor()

# User Table

cursor.execute(
   """CREATE TABLE USER(
       user_id INTEGER PRIMARY KEY,
       name VARCHAR(20),
       email VARCHAR(20) UNIQUE,
       password VARCHAR(20) UNIQUE,
       Mobile INTEGER UNIQUE
   )""")

# Employee Table

cursor.execute(
    """
    CREATE TABLE EMPLOYEER(
        emp_id INTEGER(10) PRIMARY KEY,
        job_id INTEGER(10) REFERENCES JOBAPPLICATION(job_id),
        name VARCHAR(25), 
        email VARCHAR UNIQUE,
        phone INTEGER UNIQUE, 
        password VARCHAR UNIQUE
    )""")

# JobPosting Table

cursor.execute(
    """
    CREATE TABLE JOBPOSTING(
        job_id INTEGER(10) PRIMARY KEY, 
        role VARCHAR NOT NULL,
        company VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL UNIQUE,
        emp_id INTEGER(10) NOT NULL REFERENCES EMPLOYEER(emp_id)
    )""")

# JobAplication Table

cursor.execute(
    """
    CREATE TABLE JOBAPPLICATION(
        job_id INTEGER(10) PRIMARY KEY, 
        user_id INTEGER(10) REFERENCES USER(user_id),
        resume VARCHAR(50) NOT NULL UNIQUE,
        skills VARCHAR(400) NOT NULL
    )""")

con.commit()

con.close()


# def Database():
#     conn = sqlite3.connect("rev_hire.db")
#     cursor = conn.cursor()

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS USER (
#         user_id INTEGER PRIMARY KEY,
#         name TEXT,
#         email TEXT UNIQUE,
#         password TEXT,
#         mobile INTEGER UNIQUE
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS EMPLOYEER (
#         emp_id INTEGER PRIMARY KEY,
#         job_id INTEGER REFERENCES JOBAPPLICATION(job_id),
#         name TEXT,
#         email TEXT UNIQUE,
#         phone INTEGER UNIQUE,
#         password TEXT
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS JOBPOSTING (
#         job_id INTEGER PRIMARY KEY,
#         role TEXT NOT NULL,
#         company TEXT NOT NULL,
#         email TEXT NOT NULL UNIQUE,
#         emp_id INTEGER NOT NULL REFERENCES EMPLOYEER(emp_id)
#     )
#     """)

#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS JOBAPPLICATION (
#         job_id INTEGER PRIMARY KEY,
#         user_id INTEGER REFERENCES USER(user_id),
#         resume TEXT NOT NULL UNIQUE,
#         skills TEXT NOT NULL
#     )
#     """)

#     conn.commit()
#     conn.close()

# Database()