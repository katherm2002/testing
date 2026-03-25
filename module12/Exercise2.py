import requests
municipality = (input("Enter municipality name: "))
api_key = "96f4c282452a4145006acec57ac7d020"
request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}"
response = requests.get(request).json()
# print(response)

description = response["weather"][0]["description"]
temperature_kelvin = response["main"]["temp"]
temperature_celsius = temperature_kelvin - 273.15

print(f"Weather: {description}")
print(f"Temperature: {temperature_celsius:.1f} °C")

