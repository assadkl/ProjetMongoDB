from tkinter import *
from scripts.models.mongo_db_singleton import MongoDBSingleton

class UIMethods:
    def __init__(self):
        pass
    #Définition de méthodes statiques
    @staticmethod
    #Méthode qui reccupère les données en appellant une fonction du singleton
    def get_bdd_data(current_page: int):
        db = MongoDBSingleton.get_instance().db['complete_profiles']
        #Ici le pipline permettant de réccupérer les 10 premieres lignes des données
        query = [{'$sort' : {'_id': 1}},
                 {'$skip': (current_page*10)},
                 {'$limit' : 10}]
        results = db.aggregate(query)
        method_result = []
        #Boucle qui range les résultats
        for result in results:
            method_result.append(result)
        return method_result
    
    @staticmethod
    #Ici la méthode qui réccupére les 10 lignes précédentes par rapport aux lignes de la page actuelle
    def previous_page(current_page: int):
        if(int(current_page.get())>0):
            UIMethods.get_bdd_data(current_page-1)
    
    @staticmethod
    #Ici la méthode qui reccupére les 10 lignes suivantes par rapport aux lignes de la page actuelle
    def next_page(current_page: int):
        UIMethods.get_bdd_data(current_page+1)