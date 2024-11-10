pip install requests
import requests

# Your OpenWeatherMap API key
API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# Function to fetch weather data
def get_weather(city_name):
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"]

        # Basic Weather Information
        temperature = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]
        wind_speed = wind["speed"]
        description = weather[0]["description"]

        # Display the basic weather information
        print(f"Weather in {city_name.capitalize()}:")
        print(f"Temperature: {temperature}K")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description.capitalize()}\n")

        # Call function to check for severe weather alerts
        check_severe_weather_alerts(description, temperature, wind_speed)

    else:
        print("City not found. Please check the city name and try again.")

# Function to check for severe weather alerts
def check_severe_weather_alerts(description, temperature, wind_speed):
    alerts = []

    # Conditions for Severe Weather Alerts
    if "storm" in description.lower() or "thunder" in description.lower():
        alerts.append("⚠️ Storm Alert! Thunderstorms or severe storms expected.")
    if temperature < 273.15:  # Below 0°C
        alerts.append("⚠️ Extreme Cold Alert! Temperatures below freezing point.")
    if temperature > 310.15:  # Above 37°C
        alerts.append("⚠️ Heat Alert! Extremely high temperatures.")
    if wind_speed > 15:  # High wind speed in m/s
        alerts.append("⚠️ High Wind Alert! Strong winds detected.")

    # Print alerts if any severe weather conditions are met
    if alerts:
        print("Severe Weather Alerts:")
        for alert in alerts:
            print(alert)
    else:
        print("No severe weather alerts for your location.")

# Main function to run the weather forecast app
def main():
    city_name = input("Enter city name: ")
    get_weather(city_name)

# Run the app
if __name__ == "__main__":
    main()
