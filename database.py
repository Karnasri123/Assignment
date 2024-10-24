import sqlite3
from datetime import datetime

DB_NAME = 'weather_data.db'

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    # Create weather data table
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temp REAL,
            feels_like REAL,
            weather TEXT,
            timestamp INTEGER
        )
    ''')
    
    # Create daily summary table
    c.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            date TEXT,
            avg_temp REAL,
            min_temp REAL,
            max_temp REAL,
            dominant_weather TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def add_weather_data(city, weather_data):
    """Add weather data to the database."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute('''
        INSERT INTO weather_data (city, temp, feels_like, weather, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (city, weather_data['temp'], weather_data['feels_like'], weather_data['weather'], weather_data['dt']))
    
    conn.commit()
    conn.close()

def get_daily_summary(city):
    """Get the daily weather summary for a city."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    c.execute('''
        SELECT AVG(temp), MIN(temp), MAX(temp), weather, date(timestamp, 'unixepoch')
        FROM weather_data
        WHERE city = ?
        GROUP BY date(timestamp, 'unixepoch')
        ORDER BY date(timestamp, 'unixepoch') DESC
        LIMIT 1
    ''', (city,))
    
    row = c.fetchone()
    conn.close()
    
    if row:
        return {
            'city': city,
            'avg_temp': row[0],
            'min_temp': row[1],
            'max_temp': row[2],
            'dominant_weather': row[3]
        }
    else:
        return None
