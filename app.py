from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as ai
import sqlite3

# Load the environment variables
load_dotenv()

#  Confifure the google ai
ai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Google Gemini model
def get_gemini_response(question, prompt):
    model = ai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrive query from the sql database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.close()
    for row in rows:
        print(row)
    return rows    

# Define your prompt

prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)