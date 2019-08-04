import json
import requests
import pymongo
import urllib.parse
import pymysql

#Get Weather conditions
api_token = '8af2fc6096188a91c85c8417aaaa8f74'
api_url = 'api.openweathermap.org/data/2.5/'
api_param = 'q=Ibiuna,br'

request = 'https://' + api_url + 'weather?' + api_param + '&appid=' + api_token
response = requests.get(request)

data = response.json()

main = data['main']
temp = str(main['temp'] - 273.15)
humi = str(main['humidity'])

#Insert MySql - Local and Remote
sql = 'INSERT INTO `Weather` (`Date`, `Temperature`, `Humidity`) VALUES (SYSDATE(), ' + temp + ', ' + humi +');'

#Local Mysql
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='marcelo',
                       password='',
                       db='Chale')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()

#Remote Mysql
conn = pymysql.connect(host='remotemysql.com',
                       port=3306,
                       user='1nfP179WJX',
                       password='DEBCENlorl',
                       db='1nfP179WJX')
cursor = conn.cursor()
cursor.execute(sql)
conn.commit()
conn.close()

#Insert MongoDB
myclient = pymongo.MongoClient("mongodb+srv://chale:ch1234@cluster0-do4dm.azure.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["Chale"]
mycol = mydb["Weather"]

x = mycol.insert_one(data)
