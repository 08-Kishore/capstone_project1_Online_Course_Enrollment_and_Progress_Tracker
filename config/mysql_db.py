import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

load_dotenv()

def get_mysql_connection():
    """Establishes and returns a connection to the MySQL database."""
    try:
        connection = connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "password123"),
            database=os.getenv("DB_NAME", "online_course_db")
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None