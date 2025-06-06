import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# -------------------------------
# Replace with your actual API key
API_KEY = "d2142d45ed1f124d56195c1e32f83ac2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# -------------------------------

def get_weather_data(city):
    """Fetch weather data from OpenWeatherMap API for the given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def create_weather_dashboard(data):
    """Create a dashboard-style visualization of weather data."""
    if data is None or data.get("cod") != 200:
        print("Invalid data or city not found.")
        return

    # Extract necessary values
    city = data["name"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    pressure = data["main"]["pressure"]
    description = data["weather"][0]["description"].capitalize()

    # Create DataFrame for visualization
    df = pd.DataFrame({
        "Parameter": ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)", "Pressure (hPa)"],
        "Value": [temp, humidity, wind, pressure]
    })

    # Create dashboard layout
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # Bar chart
    sns.barplot(x="Parameter", y="Value", data=df, ax=axes[0], palette="coolwarm")
    axes[0].set_title(f"Weather Parameters in {city}")
    axes[0].tick_params(axis='x', rotation=20)

    # Table
    axes[1].axis('off')
    axes[1].table(cellText=df.values, colLabels=df.columns, loc='center')
    axes[1].set_title("Summary Table")

    # Main Title
    plt.suptitle(f"Weather Dashboard: {city} - {description}", fontsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    weather_data = get_weather_data(city_name)
    create_weather_dashboard(weather_data)