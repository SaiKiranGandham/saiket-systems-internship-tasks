 # Fetch Data from an API and Display It(Task 2)
import requests
city = input("Enter city name: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    temp = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]
    print("\n----- WEATHER DETAILS -----")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)
else:
    print("Unable to fetch weather data.")