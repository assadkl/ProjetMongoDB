import matplotlib.pyplot as plt

#Création de la class GraphDesigner permettant de renvoyer les graphiques de résolution de problématiques
class GraphDesigner:

    def __init__(self):
        print("Je dessine des graphes")

    #Définition de plusieurs méthodes permettant de créer les graphes correspondants aux problématiques appelées
    def designSalaryByGenderByEduLevel(self, data):
        education_hommes = []
        education_femmes = []
        salaires_hommes = []
        salaires_femmes = []
        #Boucles qui ajoutent les résultats de la class ProblemSolver correspondant à la problématique 
        # SalaryByGenderByEduLevel dans les listes précédemment créées
        for doc in data[0]:
            education_hommes.append(doc['_id'])
            salaires_hommes.append(doc['AvgSal'])
        for doc in data[1]:
            education_femmes.append(doc['_id'])
            salaires_femmes.append(doc['AvgSal'])
        
        #Définition de la taille de la fenêtre du graphe
        plt.figure(figsize=(10, 6))
        #Définition de la largeur des barres
        width = 0.35
        #Définition de la position des barres pour les hommes
        x_h = range(len(education_hommes))
        #Création des barres pour les hommes représentant leur salaire moyen
        plt.bar(x_h, salaires_hommes, width, label='Male')
        #Définition de la position des barres pour les femmes qui seront décalées par rapport à celles des hommes
        x_f = [x + width for x in x_h]
        #Création des barres pour les femmes représentant leur salaire moyen
        plt.bar(x_f, salaires_femmes, width, label='Female')
        #Configuration de l'axe des abscisses et celui des ordonnées
        plt.xlabel('Niveau d\'éducation')
        plt.ylabel('Moyenne des salaires')
        #Configuration du titre 
        plt.title('Moyenne des salaires par niveau d\'éducation et genre')
        #Définition des étiquettes de l'axe x
        plt.xticks([x + width / 2 for x in x_h], education_femmes)
        #Ajout de la légende
        plt.legend()
        #Affichage du graphique
        plt.show()

    def designSalaryByGenderByYearsOfXp(self, data):
        experiences_hommes = []
        experiences_femmes = []
        salaires_hommes = []
        salaires_femmes = []
        #Boucles qui ajoutent les résultats de la class ProblemSolver correspondant à la problématique 
        # SalaryByGenderByYearsOfXp dans les listes précédemment créées
        for doc in data[0]:
            experiences_hommes.append(doc['_id'])
            salaires_hommes.append(doc['AvgSal'])
        for doc in data[1]:
            experiences_femmes.append(doc['_id'])
            salaires_femmes.append(doc['AvgSal'])

        plt.figure(figsize=(10, 6))
        #Création d'un graphique linéaire montrant le salaire moyen en fonction du nombre d'années d'expérience pour les hommes et les femmes
        plt.plot(experiences_hommes, salaires_hommes, label='Male')
        plt.plot(experiences_femmes, salaires_femmes, label='Female')
        plt.xlabel('Expérience')
        plt.ylabel('Salaire moyen')
        plt.title('Salaire moyen par année d\'expérience et par genre')
        plt.legend()
        plt.show()

    def designBottom100Salaries(self, data):
        gender_bottom_salaries = []
        bottom_salaries = []
        #Boucle qui ajoute les résultats de la class ProblemSolver correspondant à la problématique 
        # Bottom100Salaries dans les listes précédemment créées
        for doc in data:
            gender_bottom_salaries.append(doc['Genre'])
            bottom_salaries.append(doc['AvgSal'])

        plt.figure(figsize=(6, 6))
        #Création d'un diagramme circulaire montrant la répartition hommes femmes parmi les 100 personnes les moins rémunérées
        plt.pie(gender_bottom_salaries, autopct='%1.1f%%', startangle=90, labels=['Femmes','Hommes'])
        plt.title('Pourcentage des genres parmi 100 personnes les moins rémunérées')
        plt.legend()
        plt.show()

        plt.figure(figsize=(6, 6))
        #Création des barres pour les femmes montrant leur salaire moyen
        plt.bar(data[0]['_id'], data[0]['AvgSal'], label='Femmes')
        #Création des barres pour les hommes montrant leur salaire moyen
        plt.bar(data[1]['_id'], data[1]['AvgSal'], label='Hommes')
        plt.title('Salaires par genre des 100 personnes les moins rémunérées')
        plt.legend()
        plt.show()

        plt.figure(figsize=(6, 6))
        #Création des barres pour les femmes montrant leur année d'expérience moyenne
        plt.bar(data[0]['_id'], data[0]['Experience'], label='Femmes')
        #Création des barres pour les hommes montrant leur année d'expérience moyenne
        plt.bar(data[1]['_id'], data[1]['Experience'], label='Hommes')
        plt.title('Année d\'expérience par genre des 100 personnes les moins rémunérées')
        plt.legend()
        plt.show()

    def designTop100Salaries(self, data):
        gender_top_salaries = []
        top_salaries = []
        #Boucle qui ajoute les résultats de la class ProblemSolver correspondant à la problématique 
        # Top100Salaries dans les listes précédemment créées
        for doc in data:
            gender_top_salaries.append(doc['Genre'])
            top_salaries.append(doc['AvgSal'])

        plt.figure(figsize=(6, 6))
        #Création d'un diagramme circulaire montrant la répartition hommes femmes parmi les 100 personnes les mieux rémunérées
        plt.pie(gender_top_salaries, autopct='%1.1f%%', startangle=90, labels=['Femmes','Hommes'])
        plt.title('Pourcentage des genres parmi 100 personnes les mieux rémunérées')
        plt.legend()
        plt.show()

        plt.figure(figsize=(6, 6))
        #Création des barres pour les femmes montrant leur salaire moyen
        plt.bar(data[0]['_id'], data[0]['AvgSal'], label='Femmes')
        #Création des barres pour les hommes montrant leur salaire moyen
        plt.bar(data[1]['_id'], data[1]['AvgSal'], label='Hommes')
        plt.title('Salaires par genre des 100 personnes les mieux rémunérées')
        plt.legend()
        plt.show()

        plt.figure(figsize=(6, 6))
        #Création des barres pour les femmes montrant leur année d'expérience moyenne
        plt.bar(data[0]['_id'], data[0]['Experience'], label='Femmes')
        #Création des barres pour les hommes montrant leur année d'expérience moyenne
        plt.bar(data[1]['_id'], data[1]['Experience'], label='Hommes')
        plt.title('Année d\'expérience par genre des 100 personnes les mieux rémunérées')
        plt.legend()
        plt.show()

    def designTop50SalariesByGender(self, data):
        #Boucle qui affiche les résultats de la class ProblemSolver correspondant à la problématique 
        # Top50SalariesByGender
        for item in data:
            print(item)

    #Correspondance des problématiques avec leur graphes
    def designGraph(self, type_graph:str, data):
        match type_graph: 
            #Dans le cas où la problématique est SalaryByGenderByEduLevel, renvoyer le graphe de cette problématique 
            case 'SalaryByGenderByEduLevel': 
                return self.designSalaryByGenderByEduLevel(data)
            #Dans le cas où la problématique est SalaryByGenderByYearsOfXp, renvoyer le graphe de cette problématique
            case 'SalaryByGenderByYearsOfXp':
                return self.designSalaryByGenderByYearsOfXp(data)
            #Dans le cas où la problématique est Top100Salaries, renvoyer le graphe de cette problématique
            case 'Top100Salaries':
                return self.designTop100Salaries(data)
            #Dans le cas où la problématique est Bottom100Salaries, renvoyer le graphe de cette problématique
            case 'Bottom100Salaries':
                return self.designBottom100Salaries(data)
            #Dans le cas où la problématique est Top50SalariesByGender, renvoyer le graphe de cette problématique
            case 'Top50SalariesByGender': 
                return self.designTop50SalariesByGender(data)
            #Dans le cas où la problématique n'est pas connue, ne rien renvoyer
            case _:
                return "Je ne sais pas dessiner ce graph."