import requests
from dotenv import load_dotenv
import os
import psycopg2
from psycopg2 import sql

load_dotenv()

# Database connection settings
DB_settings = {
    "host": "localhost",
    "port": "5432",
    "database": "weather_data",
    "user": "myuser",
    "password": "mypassword"
}

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)
        return None

# Insert data into database
def insert_weather_data(city, temperature, description):
    try:
        conn = psycopg2.connect(**DB_settings)
        cur = conn.cursor()
        insert_query = '''
        INSERT INTO weather (city, temperature, description)
        VALUES (%s, %s, %s);
        '''
        cur.execute(insert_query, (city, temperature, description))
        conn.commit()
        cur.close()
        print(f"Weather data for {city} inserted successfully!")
    except psycopg2.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    city = "London"
    weather_data = get_weather(city)
    print(weather_data)