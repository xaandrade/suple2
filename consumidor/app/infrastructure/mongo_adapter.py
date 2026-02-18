from pymongo import MongoClient

class MongoAdapter:
    def __init__(self):
        self.client = MongoClient("mongodb://mongodb:27017")
        self.db = self.client.examen_db
        self.collection = self.db.mensajes_recibidos

    def save_data(self, data):
        self.collection.insert_one(data)
        print(f"--- [DB] Guardado con éxito: {data}")