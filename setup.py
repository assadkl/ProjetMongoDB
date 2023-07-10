# This file contains your application setup code (should be run first and only one time)
from scripts.models.mongo_db_singleton import MongoDBSingleton
from scripts.models.EduLevel import EduLevel
import pandas as pd
from tqdm import tqdm

client = MongoDBSingleton.get_instance().db["complete_profiles"]
#Validator : {
#   $jsonSchema: {
#     bsonType: 'object',
#     required: [
#       'Age',
#       'Gender',
#       'Education Level',
#       'Job Title',
#       'Years of Experience',
#       'Salary'
#     ],
#     properties: {
#       Age: {
#         bsonType: 'double',
#         description: 'L\'age de la personne est nécessaire'
#       },
#       Gender: {
#         bsonType: 'string',
#         description: 'Le genre de la personne est nécessaire'
#       },
#       'Education Level': {
#         bsonType: 'string',
#         description: 'Le niveau d\'éducation de la personne est nécessaire'
#       },
#       'Job Title': {
#         bsonType: 'string',
#         description: 'Le titre du métier de la personne est nécessaire'
#       },
#       'Years of Experience': {
#         bsonType: 'double',
#         description: 'Les années d\'expérience de la personne est nécessaire'
#       },
#       Salary: {
#         bsonType: 'double',
#         description: 'Le salaire de la personne est nécessaire'
#       }
#     }
#   }
# }
#Création du dataframe sur la base du fichier .csv source
dataframe = pd.read_csv("./assets/Salary_Data.csv")
#Calcul du nombre de valeurs nulles
missing_values = dataframe.isna().sum()
#Suppression des lignes comportants des valeurs nulles
dataframe.dropna(inplace=True)
#Affichage du compte des valeurs nulles
print(missing_values)
#Mise en place de la barre de chargement avant import
with tqdm(total=len(dataframe), desc='Importing data') as pbar:
    #Pour chaque ligne du fichier
    for identificator, data in dataframe.iterrows():
        #Transformation en dictionnaire pour facilité de traitement
        dict_data = data.to_dict()
        #Remplacement/Uniformiation de la valeur Education Level
        match dict_data['Education Level']:
            #En Bachelor si la donnée est Bachelor's ou Bachelor's Degree
            case 'Bachelor\'s' | 'Bachelor\'s Degree':
                dict_data["Education Level"] = 'Bachelor'
            #En Master si la donnée est Master's ou Master's Degree
            case 'Master\'s' | 'Master\'s Degree':
                dict_data['Education Level'] = 'Master'
            #En PhD si la donnée est phD ou PhD
            case 'phD' | 'PhD':
                dict_data['Education Level'] = 'PhD'
            #Par défaut    
            case _:
                dict_data['Education Level'] = 'High School'
        dict_data['Years of Study'] = EduLevel.getRealValue(dict_data['Education Level'])
        #Une fois les valeurs potentiellement modifiées, insertion en base de données
        client.insert_one(dict_data)
        #Progression de la barre de chargement
        pbar.update(1)