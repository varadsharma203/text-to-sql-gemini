import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sqlite3
import streamlit as st

load_dotenv()

# Assuming your .env uses GOOGLE_API_KEY (all caps)
my_api_key = os.getenv("GOOGLE_API_KEY")

# Function to load google gemini model and provide queries as response
def get_gemini_response(question, prompt): # Fixed the typo in the name
    client = genai.Client(api_key=my_api_key)
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=question,
        config=types.GenerateContentConfig(
            system_instruction=prompt
        )
    )
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    
    return rows

## DEFINING THE PROMPT (Removed the list brackets `[]` so it's a pure string)
system_prompt = """You are an expert in converting English questions to SQL queries.
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION.

For Example:
Example 1 - How many entries of records are present? 
The SQL command will be something like this: SELECT COUNT(*) FROM STUDENT; 

CRITICAL: The SQL command should NOT have ``` at the beginning or the end, and do not include the word 'sql' in the output. Just return the raw query."""


# STREAMLIT APP
st.set_page_config(page_title="RETRIEVE ANY SQL QUERY")
st.header("GEMINI APP TO RETRIEVE ANY SQL DATA")

question = st.text_input("INPUT:", key="input")
submit = st.button("Ask the question")

# If submit is clicked 
if submit:
    # 1. Get the raw string response from Gemini
    generated_sql = get_gemini_response(question, system_prompt)
    print("AI Generated:", generated_sql)
    
    # 2. Safety Catch: Clean up any markdown blocks just in case Gemini ignores the prompt
    cleaned_sql = generated_sql.replace("```sql", "").replace("```", "").strip()
    
    # 3. Try to execute the cleaned query
    try:
        query_results = read_sql_query(cleaned_sql, "student.db")
        
        st.subheader("The response is:")
        for row in query_results:
            print(row)
            st.write(row) # Changed to st.write so it doesn't print as massive headers!
            
    except sqlite3.Error as e:
        # This will catch any SQL errors and display them nicely in Streamlit instead of crashing
        st.error(f"Database Error: {e}")