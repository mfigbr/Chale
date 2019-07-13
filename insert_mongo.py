import base64
import bson
import pymongo
import urllib.parse

with open("/home/marcelo/Imagens/20190708/images/T19070816133000.jpg","rb") as imagefile:
    str = base64.b64encode(imagefile.read())
bstr = bson.BSON.encode(str)

myclient = pymongo.MongoClient("mongodb+srv://marcelo:" + urllib.parse.quote("3:s@N<a4ho@K") + "@cluster0-do4dm.azure.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["Chale"]
mycol = mydb["Camera"]

x = mycol.insert_one(bstr)

