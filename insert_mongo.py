import pymongo
import urllib.parse

#with open("/home/marcelo/Imagens/20190708/images/T19070816133000.jpg","rb") as imagefile:
#    str = base64.b64encode(imagefile.read())
#bstr = bson.BSON.encode(str)

with open("/home/marcelo/Imagens/vscode.jpeg","rb") as imagem:
    bstr = {"imagem" : imagem.read()}

myclient = pymongo.MongoClient("mongodb+srv://chale:ch1234@cluster0-do4dm.azure.mongodb.net/test?retryWrites=true&w=majority")
mydb = myclient["Chale"]
mycol = mydb["Camera"]

x = mycol.insert_one(bstr)

