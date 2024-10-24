from flask import Flask, jsonify
from weather_api import get_weather_data
from database import init_db, add_weather_data, get_daily_summary
from alerts import check_alerts
import time
import threading

app = Flask(__name__)

# Initialize the database
init_db()

# Configurable cities
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']

# Interval between API calls (in seconds)
INTERVAL = 300  # 5 minutes


def fetch_and_store_weather():
    """Fetch weather data for cities and store in database."""
    while True:
        for city in CITIES:
            weather_data = get_weather_data(city)
            if weather_data:
                add_weather_data(city, weather_data)
                check_alerts(city, weather_data)
        time.sleep(INTERVAL)


@app.route('/')
def index():
    return "Weather Monitoring System Running"

@app.route('/daily-summary/<city>', methods=['GET'])
def daily_summary(city):
    """Return daily summary for a city."""
    summary = get_daily_summary(city)
    return jsonify(summary)


if __name__ == '__main__':
    # Start the background thread to fetch weather data
    threading.Thread(target=fetch_and_store_weather, daemon=True).start()
    
    # Run the Flask application
    app.run(debug=True, port=5000)
