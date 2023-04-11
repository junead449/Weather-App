import requests

city=input("Enter the name of your city:\n ")

url=f"https://api.weatherapi.com/v1/current.json?key=9a240881621042cc81f195142232903 &q={city}"

r=requests.get(url)
print(r.text)