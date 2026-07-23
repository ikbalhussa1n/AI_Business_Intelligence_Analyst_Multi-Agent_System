import os
import psycopg2
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
def get_connection():

    try:
        # 1. Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )
        return connection

    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None

@tool
def get_schema():
    """
    Returns database tables, columns, and data types.
    Use this before writing SQL queries.
    """

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            table_name,
            column_name,
            data_type
        FROM information_schema.columns
        WHERE table_schema='public'
        ORDER BY table_name, ordinal_position;
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    schema = ""

    for table, column, dtype in rows:
        schema += f"{table}.{column} ({dtype})\n"

    return schema


@tool
def execute_query(sql: str):
    """
    Executes SQL query and returns results.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(sql)
        result = cursor.fetchall()

        cursor.close()
        conn.close()

        return result

    except Exception as e:
        return f"SQL Error: {str(e)}"