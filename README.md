Configuration:
# OpenWeatherMap API Key
API_KEY = 'your_openweathermap_api_key'

# Threshold for temperature alerts (in Celsius)
TEMP_THRESHOLD = 35
////////////////////////////////////////////////////////REQUIREMENTS
# Weather Monitoring System

## Overview
This is a real-time weather monitoring system that fetches data from the OpenWeatherMap API, processes the data, stores daily summaries, and raises alerts based on user-defined thresholds.

## Prerequisites
- Python 3.8+
- Flask
- SQLite
- Docker (optional)

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/Karnasri123/Assignment
    cd weather-monitoring-system
    ```

2. Create a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Add your OpenWeatherMap API key in `config.py`:

    ```python
    API_KEY = 'your_openweathermap_api_key'
    ```

4. Run the application:

    ```bash
    python app.py
    ```

5. Access the application at [http://localhost:5000](http://localhost:5000).

## Docker Setup

1. Build the Docker image:

    ```bash
    docker build -t weather-monitoring-system .
    ```

2. Run the container:

    ```bash
    docker run -d -p 5000:5000 weather-monitoring-system
    ```

## API Endpoints

- `/daily-summary/<city>`: Returns the daily weather summary for the specified city.
