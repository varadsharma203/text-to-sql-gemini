import sqlite3

# Connect to SQLite (this creates the file in your current folder)
connection = sqlite3.connect('student.db')
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT(
    NAME VARCHAR(20),
    CLASS VARCHAR(20),
    SECTION VARCHAR(20)
);
"""
cursor.execute(table_info)

# Insert some dummy records
student_records = [
    ('Hippo', 'Data Science', 'A'),
    ('Alice', 'Web Dev', 'B'),
    ('Bob', 'Data Science', 'A'),
    ('Charlie', 'Networking', 'C'),
    ('Diana', 'Machine Learning', 'A')
]

# Use executemany to insert multiple rows at once
cursor.executemany("INSERT INTO STUDENT (NAME, CLASS, SECTION) VALUES (?, ?, ?)", student_records)

# Save and close
connection.commit()
print("Database 'student.db' created and populated successfully!")
connection.close()