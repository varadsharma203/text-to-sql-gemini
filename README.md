# Natural Language to SQL Query App

An interactive web application built with Python and Streamlit that allows users to query a database using plain English. The app uses the Google GenAI SDK (Gemini) to translate natural language questions into valid SQL queries, executes them against a local SQLite database, and displays the results.

## 🚀 Features

* **Natural Language Processing:** Ask questions in plain English (e.g., "How many students are in the Data Science class?").
* **AI-Powered SQL Generation:** Utilizes Google's Gemini model to accurately convert English prompts into SQL commands.
* **Local Database Execution:** Queries are executed in real-time against a local SQLite database (`student.db`).
* **Interactive UI:** Built with Streamlit for a clean, responsive, and easy-to-use web interface.
* **Error Handling:** Built-in safeguards to clean up AI formatting and catch SQL execution errors gracefully.

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend:** Streamlit
* **Database:** SQLite3
* **AI Integration:** Google GenAI SDK (`google-genai`)
* **Environment Management:** `python-dotenv`

## 📁 Project Structure

* `setup_db.py`: Script to initialize the SQLite database (`student.db`), create the `STUDENT` table, and populate it with dummy data.
* `SQL.py`: The main Streamlit application containing the UI and the Gemini AI integration logic.
* `.env`: Environment variable file storing the Google API key (you will need to create this).

## ⚙️ Installation and Setup

**1. Clone the repository**
Open your terminal and clone this repository to your local machine:
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
