import certifi
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
#Lembrar de instalar certificados localizado na pasta do Python


#Servidor remoto
#uri = "mongodb+srv://fabiominghetti:FMmongodb7619@cluster0.kq8httq.mongodb.net/?retryWrites=true&w=majority:27017)"
#Servidor local
uri = "mongodb://localhost:27017"

# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'), ssl_ca_certs=certifi.where())
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

import pandas as pd

db = client.Contatos
collection = db.get_collection("DadosBasicos")
df = pd.read_csv('https://raw.githubusercontent.com/fabiominghetti/coleta/main/world-happiness-report-2021.csv')

#Outra fonte de informações
#df = pd.read_csv('https://media.githubusercontent.com/media/datablist/sample-csv-files/main/files/people/people-1000.csv')

data = df.to_dict(orient = "records")
collection.insert_many(data)

filtro = {"Generosity": {"$gt": 0}}
#filtro para arquivo de pessoas
#filtro = {"Sex": "Male"}
response = collection.find(filtro)
for dado in response: print(dado)