from scripts.models.mongo_db_singleton import MongoDBSingleton
from scripts.models.EduLevel import EduLevel

#Création de la class ProblemSolver permettant de résoudre les différentes problématiques 
class ProblemSolver:
    def __init__(self):
        print('''Je sais répondre à plusieurs problématiques : 
        SalaryByGenderByEduLevel, 
        SalaryByGenderByYearsOfXp, 
        Top100Salaries,
        Bottom100Salaries, 
        Top50SalariesByGender.''')
    
    #Définition de plusieurs méthodes permettant chacune de répondre à une problématique spécifique 
    def solveSalaryByGenderByEduLevel(self):
        returned_data = []
        #Récupération des données de notre collection via le Singleton
        db = MongoDBSingleton.get_instance().db["complete_profiles"]
        #Requête permettant de filtrer les données relatives aux hommes, de calculer la moyenne des 
        # salaires et de les regrouper par niveau d'éducation, trier par ordre croissant
        pipeline1 = [{ "$match": {"Gender": {"$eq": "Male"}}},
                     { "$group": {"_id": "$Education Level",
                                  "AvgSal": {"$avg": "$Salary"}}},
                                  {"$sort": {"_id": 1 }}]
        
        #Requête permettant de filtrer les données relatives aux femmes, de calculer la moyenne des 
        # salaires et de les regrouper par niveau d'éducation, trier par ordre croissant
        pipeline2 = [{ "$match": {"Gender": {"$eq": "Female"}}},
                     { "$group": {"_id": "$Education Level",
                                  "AvgSal": {"$avg": "$Salary"}}},
                                  {"$sort": {"_id": 1 }}]
        #Aggregation de la requête homme
        results = db.aggregate(pipeline1)
        #Création d'une liste qui recevra les résultats de la requête
        male_data = []
        #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste 
        for result in results:
            male_data.append(result)

        #Aggregation de la requête femme
        results = db.aggregate(pipeline2)
        #Création d'une liste qui recevra les résultats de la requête
        female_data = []
        #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste 
        for result in results:
            female_data.append(result)

        #Renvoi des résultats pour future utilisation dans la class GraphDesigner
        returned_data.append(male_data)
        returned_data.append(female_data)
        return returned_data

    def solveSalaryByGenderByYearsOfXp(self):
        returned_data = []
        #Récupération des données de notre collection via le Singleton
        db = MongoDBSingleton.get_instance().db["complete_profiles"]
        #Requête permettant de filtrer les données relatives aux hommes, de calculer la moyenne des 
        # salaires et de les regrouper par année d'expérience, trier par ordre croissant
        pipeline1 = [{ "$match": {"Gender": {"$eq": "Male"}}},
                     { "$group": {"_id": "$Years of Experience",
                                  "AvgSal": {"$avg": "$Salary"}}},
                                  {"$sort": {"_id": 1 }}]
        
        #Requête permettant de filtrer les données relatives aux femmes, de calculer la moyenne des 
        # salaires et de les regrouper par année d'expérience, trier par ordre croissant
        pipeline2 = [{ "$match": {"Gender": {"$eq": "Female"}}},
                     { "$group": {"_id": "$Years of Experience",
                                  "AvgSal": {"$avg": "$Salary"}}},
                                  {"$sort": {"_id": 1 }}]
        #Aggregation de la requête homme
        results = db.aggregate(pipeline1)
        # Création d'une liste qui recevra les résultats de la requête
        male_data = []
        # Boucle qui ajoute chaque ligne du résultat à la suite dans la liste 
        for result in results:
            male_data.append(result)
        
        #Aggregation de la requête femme
        results = db.aggregate(pipeline2)
        #Création d'une liste qui recevra les résultats de la requête
        female_data = []
        #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste 
        for result in results:
            female_data.append(result)

        #Renvoi des résultats pour future utilisation dans la class GraphDesigner
        returned_data.append(male_data)
        returned_data.append(female_data)
        return returned_data

    def solveBottom100Salaries(self):
        returned_data = []
        #Récupération des données de notre collection via le Singleton
        db = MongoDBSingleton.get_instance().db["complete_profiles"]
        #Requête permettant de récupérer les 100 individus les moins rémunérés, de les regrouper par 
        # genre et de calculer leur salaire moyen et leur année d'expériences moyenne
        pipeline = [{"$sort": {"Salary": 1 }},
                    {'$limit': 100},
                    { "$group": {"_id": "$Gender",
                                  "AvgSal": {"$avg": "$Salary"},
                                  'Genre': {'$sum':1},
                                  'Experience': {'$avg': '$Years of Experience'}}},
                    {'$sort': {'_id':1}}]
        #Aggregation de la requête
        results = db.aggregate(pipeline)
        #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste
        for result in results:
            returned_data.append(result)
        #Renvoi des résultats pour future utilisation dans la class GraphDesigner
        return returned_data

    def solveTop100Salaries(self):
        returned_data = []
        #Récupération des données de notre collection via le Singleton
        db = MongoDBSingleton.get_instance().db["complete_profiles"]
        #Requête permettant de récupérer les 100 individus les mieux rémunérés, de les regrouper par 
        # genre et de calculer leur salaire moyen et leur année d'expériences moyenne
        pipeline = [{"$sort": {"Salary": -1 }},
                    {'$limit': 100},
                    { "$group": {"_id": "$Gender",
                                  "AvgSal": {"$avg": "$Salary"},
                                  'Genre': {'$sum':1},
                                  'Experience': {'$avg': '$Years of Experience'}}},
                    {'$sort': {'_id':1}}]
        #Aggregation de la requête
        results = db.aggregate(pipeline)
        #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste
        for result in results:
            returned_data.append(result)
        #Renvoi des résultats pour future utilisation dans la class GraphDesigner
        return returned_data

    def solveTop50SalariesByGender(self):
        returned_data = []
        #Récupération des données de notre collection via le Singleton
        base = MongoDBSingleton.get_instance().db
        db = base["complete_profiles"]
        #Requête permettant de récupérer les 50 hommes les mieux rémunérés, de calculer leur profil
        # moyen en fonction des variables
        pipeline1 = [{'$match': {'Gender' : {'$eq' : 'Male'}}},
                    {"$sort": {"Salary": -1 }},
                    {'$limit': 50},
                    { "$group": {"_id": '$Gender',
                                  "AvgSal": {"$avg": "$Salary"},
                                  'AvgAge' : {'$avg': '$Age'},
                                  'Experience': {'$avg': '$Years of Experience'},
                                  'Education': {'$avg' : '$Years of Study'}}}]
        
        #Requête permettant de récupérer les 50 femmes les mieux rémunérés, de calculer leur profil
        # moyen en fonction des variables
        pipeline2 = [{'$match': {'Gender' : {'$eq' : 'Female'}}},
                    {"$sort": {"Salary": -1 }},
                    {'$limit': 50},
                    { "$group": {"_id": '$Gender',
                                  "AvgSal": {"$avg": "$Salary"},
                                  'AvgAge' : {'$avg': '$Age'},
                                  'Experience': {'$avg': '$Years of Experience'},
                                  'Education': {'$avg' : '$Years of Study'}}}]
        #Aggregation de la requête
        results = db.aggregate(pipeline1)
        #Création de la collection Top Profiles 
        try:
            base.create_collection('top_profiles',check_exists=True)
            #Création d'une liste qui recevra les résultats de la requête
            male_data = []
            #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste
            for result in results:
                male_data.append(result)
                base['top_profiles'].insert_one(result)

            #Aggregation de la requête
            results = db.aggregate(pipeline2)
            #Création d'une liste qui recevra les résultats de la requête
            female_data = []
            #Boucle qui ajoute chaque ligne du résultat à la suite dans la liste
            for result in results:
                female_data.append(result)
                base['top_profiles'].insert_one(result)
            
            #Renvoi des résultats pour future utilisation dans la class GraphDesigner
            returned_data.append(male_data)
            returned_data.append(female_data)
        #Dans le cas où la collection existe déjà, ne rien faire
        except:
            print('La collection existe déjà')
            pass
        #Renvoi des résultats pour future utilisation dans la class GraphDesigner
        return returned_data

    #Correspondance des problématiques avec leur résolution  
    def solveIssue(self, problematic:str):
        match problematic: 
            #Dans le cas où la problématique est SalaryByGenderByEduLevel, renvoyer la résolution de cette problématique 
            case 'SalaryByGenderByEduLevel': 
                return self.solveSalaryByGenderByEduLevel()
            #Dans le cas où la problématique est SalaryByGenderByYearsOfXp, renvoyer la résolution de cette problématique
            case 'SalaryByGenderByYearsOfXp':
                return self.solveSalaryByGenderByYearsOfXp()
            #Dans le cas où la problématique est Top100Salaries, renvoyer la résolution de cette problématique 
            case 'Top100Salaries':
                return self.solveTop100Salaries()
            case 'Bottom100Salaries':
                return self.solveBottom100Salaries()
            #Dans le cas où la problématique est Top50SalariesByGender, renvoyer la résolution de cette problématique
            case 'Top50SalariesByGender': 
                return self.solveTop50SalariesByGender()
            #Dans le cas où la problématique n'est pas connue, ne rien renvoyer
            case _:
                return "Je ne connais pas cette problématique."