import json
import requests

api_token = '8af2fc6096188a91c85c8417aaaa8f74'
api_url = 'api.openweathermap.org/data/2.5/'
api_param = 'q=Ibiuna,br'

request = 'https://' + api_url + 'weather?' + api_param + '&appid=' + api_token
print(request)

response = requests.get(request)
data = response.json()

main = data['main']
temp = main['temp']
humitity = main['humidity']

print(temp)
print(humidity)
