from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Setup a basic logger
logging.basicConfig(level=logging.INFO)

@app.route('/weather/kosomak', methods=['GET'])
def get_weather():
    try:
        # Get the ZIP code from the query parameter
        zip_code = request.args.get('zip')
        if not zip_code:
            # If no ZIP code is provided, return an error
            app.logger.error("No ZIP code provided")
            return jsonify({"error": "No zip code provided"}), 400

        # For simplicity, let's pretend we can directly turn ZIP -> coordinates
        # In reality, you'd use a geocoding service to find lat/long from ZIP
        # We'll just hardcode some logic or call a geocoding API.

        # Let's do a quick mock approach for demonstration:
        # (In real life, you'd do something more precise)
        fake_lat, fake_lon = zip_to_lat_lon(zip_code)
        
        # Call Open-Meteo API
        # (We add "current_weather=true" to get the current weather)
        weather_url = (
          f"https://api.open-meteo.com/v1/forecast?latitude={fake_lat}&longitude={fake_lon}&current_weather=true"
        )
        
        weather_response = requests.get(weather_url)
        
        if weather_response.status_code != 200:
            app.logger.error(f"Open-Meteo API error. Status code: {weather_response.status_code}")
            return jsonify({"error": "Failed to fetch weather data from external API"}), 500
        
        weather_data = weather_response.json()
        
        # Extract data from the weather_data JSON
        current_weather = weather_data.get("current_weather", {})
        temperature_c = current_weather.get("temperature")
        windspeed = current_weather.get("windspeed")
        weather_code = current_weather.get("weathercode")

        # Convert Celsius to Fahrenheit (if needed)
        temperature_f = (temperature_c * 9/5) + 32 if temperature_c is not None else None
        
        # For "condition", we can interpret weather_code or just display it
        # Let's do a simple mapping
        condition = interpret_weather_code(weather_code)

        # Return the data as JSON
        return jsonify({
            "temperature": round(temperature_f, 2) if temperature_f else None,
            "condition": condition,
            "windspeed": windspeed,
        }), 200

    except Exception as e:
        app.logger.exception("Unexpected error:")
        return jsonify({"error": "Something went wrong"}), 500


def zip_to_lat_lon(zip_code):
    """
    Simple mock function that returns a made-up lat/lon
    for demonstration purposes.
    In a real app, you would use a geocoding API.
    """
    # This is just a silly example.
    # You could do if statements or call a geocoding service.
    if zip_code == "12345":
        return (42.81, -73.94)  # near Schenectady, NY
    elif zip_code == "90210":
        return (34.09, -118.41) # Beverly Hills, CA
    else:
        return (40.0, -75.0)    # some default lat/lon

def interpret_weather_code(code):
    """
    Convert the Open-Meteo weather code into a simple text description
    """
    if code is None:
        return "Unknown"

    # This is a small subset of codes for example purposes
    mapping = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        61: "Rain",
        71: "Snowfall",
    }
    return mapping.get(code, "Not sure")
    
if __name__ == '__main__':
    app.run(port=3000, debug=True)
