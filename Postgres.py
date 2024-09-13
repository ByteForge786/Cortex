import os
import psycopg2
from urllib.parse import urlparse

# Database connection parameters
db_url = os.getenv("DATABASE_URL")
db_username = os.getenv("DB_USERNAME")
db_password = os.getenv("DB_PASSWORD")

# Parse the database URL
parsed_url = urlparse(db_url)

# Sample SQL query
sample_query = """
SELECT column1, column2
FROM your_table
WHERE condition = 'value'
LIMIT 10;
"""

def run_query(query):
    try:
        # Establish a connection to the database
        conn = psycopg2.connect(
            dbname=parsed_url.path[1:],
            user=db_username,
            password=db_password,
            host=parsed_url.hostname,
            port=parsed_url.port
        )
        
        # Create a cursor object
        cur = conn.cursor()
        
        # Execute the query
        cur.execute(query)
        
        # Fetch all results
        rows = cur.fetchall()
        
        # Print the results
        for row in rows:
            print(row)
        
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    finally:
        # Close the cursor and connection
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    run_query(sample_query)
