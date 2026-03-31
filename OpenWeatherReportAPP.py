import requests

city = input("Enter the City name: ")
api_key = "23c7abd85fd57c0868a9f281f80e8911"


def get_weather_report(city: str, api_key: str) -> str:
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    data = response.json()
    res = f"{city} temperature is - {round(data["main"]["temp"])}"
    return res

print(get_weather_report(city, api_key))
    
    