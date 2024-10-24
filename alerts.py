from config import TEMP_THRESHOLD

def check_alerts(city, weather_data):
    """Check if the current weather data exceeds the threshold and trigger alert."""
    temp_in_celsius = weather_data['temp'] - 273.15  # Convert from Kelvin to Celsius
    
    if temp_in_celsius > TEMP_THRESHOLD:
        print(f"ALERT: Temperature in {city} exceeded {TEMP_THRESHOLD}°C. Current temp: {temp_in_celsius:.2f}°C")
