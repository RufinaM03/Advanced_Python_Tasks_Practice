from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask Weather App!\n\nUse /weather?city=YourCity to get weather info."

@app.route('/weather')
def weather():
    city = request.args.get('city', 'Unknown')
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Stormy", "Clear Night"]
    condition = random.choice(conditions)
    temp = random.randint(20, 38)
    humidity = random.randint(40, 90)
    wind = round(random.uniform(2.0, 12.0), 1)

    return (
        f"Weather Report for {city}\n"
        f"Condition: {condition}\n"
        f"Temperature: {temp}°C\n"
        f"Humidity: {humidity}%\n"
        f"Wind Speed: {wind} km/h\n"
    )

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5005, debug=True)