import psycopg2
import pandas as pd

# Database connection details
DB_CONFIG = {
    "dbname": "ediss7db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": "5436",
}


def execute_query(query, as_dataframe=False):
    conn = None
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        cursor.execute(query)

        col_names = [desc[0] for desc in cursor.description]

        rows = cursor.fetchall()

        results = [dict(zip(col_names, row)) for row in rows]

        cursor.close()

        return pd.DataFrame(results) if as_dataframe else results

    except Exception as e:
        print(f"Error: {e}")
        return None

    finally:
        if conn:
            conn.close()