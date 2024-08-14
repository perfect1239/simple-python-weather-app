import requests
from tkinter import *

# Function to get weather data
def get_weather():
    city = city_entry.get()
    api_key = "adc4741eaf2385f295b4791499220444"  # Your API key
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        weather_data = response.json()

        if weather_data['cod'] == 200:
            city_name = weather_data['name']
            country = weather_data['sys']['country']
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            result_label.config(text=f"City: {city_name}, {country}\nTemperature: {temperature}°C\n"
                                     f"Description: {description.capitalize()}\nHumidity: {humidity}%\n"
                                     f"Wind Speed: {wind_speed} m/s")
        else:
            result_label.config(text="City not found. Please try again.")
    except Exception as e:
        result_label.config(text="Error retrieving data. Please check your connection and try again.")

# Setting up the GUI
root = Tk()
root.title("Weather App")
root.geometry("400x300")

city_label = Label(root, text="Enter City Name:", font=("Helvetica", 12))
city_label.pack(pady=10)

city_entry = Entry(root, width=30, font=("Helvetica", 12))
city_entry.pack(pady=5)

get_weather_button = Button(root, text="Get Weather", command=get_weather, font=("Helvetica", 12))
get_weather_button.pack(pady=20)

result_label = Label(root, text="", font=("Helvetica", 12), justify=LEFT)
result_label.pack(pady=10)

# Run the application
root.mainloop()
