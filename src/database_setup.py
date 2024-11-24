import psycopg2
from psycopg2 import sql

# Database connection settings
conn = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "weather_data",
    user = "myuser",
    password = "mypassword"
)

# Cursor to execute SQL commands
cur = conn.cursor()

# Create a table
create_table = '''
CREATE TABLE IF NOT EXISTS weather (
id SERIAL PRIMARY KEY,
city VARCHAR(50),
temperature REAL,
description VARCHAR(100),
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
'''

cur.execute(create_table)

conn.commit()
cur.close()
conn.close()