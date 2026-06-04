import requests
from datetime import datetime

API_KEY = "2b241436a6dedfcd2f5c31d791cd37a1"


def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("\n❌ City not found!")
            return

        sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.fromtimestamp(data["sys"]["sunset"])

        print("\n===== WEATHER REPORT =====")
        print(f"🌍 City: {data['name']}")
        print(f"🏳️ Country: {data['sys']['country']}")
        print(f"🌡 Temperature: {data['main']['temp']}°C")
        print(f"🤗 Feels Like: {data['main']['feels_like']}°C")
        print(f"☁️ Condition: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬 Wind Speed: {data['wind']['speed']} m/s")
        print(f"🌅 Sunrise: {sunrise.strftime('%H:%M:%S')}")
        print(f"🌇 Sunset: {sunset.strftime('%H:%M:%S')}")

    except Exception as e:
        print("Error:", e)


def main():
    print("🌦 WEATHER APP")
    print("=" * 30)

    while True:
        city = input("\nEnter city name: ")

        get_weather(city)

        choice = input("\nSearch another city? (y/n): ").lower()

        if choice != "y":
            print("\n👋 Thank you for using Weather App!")
            break


if __name__ == "__main__":
    main()