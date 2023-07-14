import requests
import json
import os 

if __name__ == '__main__':
    print("Welcome to Climate App Created by Ayushman")

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=ce955959b6b14aabb75152328231407&q={city}"

r = requests.get(url)
# print(r.text)

wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]

os.system(f"say 'The current weather in {city} is {w} degrees'")