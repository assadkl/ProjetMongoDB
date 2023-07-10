from tkinter import ttk, StringVar, END, Tk
from scripts.models.mongo_db_singleton import MongoDBSingleton
from scripts.models.UIMethods import UIMethods
from scripts.utils import SOLVABLE_ISSUES
from scripts.models.ProblemSolver import ProblemSolver
from scripts.models.GraphDesigner import GraphDesigner

class UI:
    window = Tk()

    def __init__(self):
        #Créer la fenêtre principale
        self.window.title("Projet Mongo - ACA")
        #Taille de cette fenêtre
        self.window.geometry("1400x700")
        
        #Indentation de la page actuelle a 0
        self.CURRENT_PAGE = 0
        ttk.Label(self.window, text='Page actuelle : ').grid(column=1,row=1)
        self.current_page_label_var = StringVar(value=str(self.CURRENT_PAGE))
        #Création d'un champs texte
        self.current_page_label = ttk.Label(self.window, textvariable=self.current_page_label_var)
        #Position de ce champs sur la fenêtre
        self.current_page_label.grid(column=1,row=2)
        #Création de colonnes dans le champs texte
        columns = ['id','age','genre','niveau_education','emploi','annees_exprerience','salaire']

        #Création d'un widget Treeview dans l'interface graphique, celui_ci est utilisé pour afficher des données 
        # sous forme d'arbre, avec des en-têtes de colonne pour organiser les données.
        self.data_tree = ttk.Treeview(self.window, columns=columns, show='headings')

        #On appelle la methode get_bdd_data de la classe UIMethods qui récupérer les données de la base de données
        #  en fonction de la page actuelle. Le résultat de cette opération est ensuite stocké dans self.retrieved_data.
        self.retrieved_data = UIMethods.get_bdd_data(current_page=self.CURRENT_PAGE)
        self.load_data(self.retrieved_data)
        
        #Implémentation des boutons page précédente et suivante
        previous_button = ttk.Button(self.window,text='Page précédente',command=self.previous_page)
        previous_button.grid(column=1,row=4)
        next_button = ttk.Button(self.window,text='Page suivante',command=self.next_page)
        next_button.grid(column=1,row=5)

        #Définission d'un widget de type Combobox (liste) dans l'interface, on crée une variable de type string, variable qui est 
        # utilisée pour stocker une valeur
        self.selected_issue = StringVar(value='SalaryByGenderByEduLevel')
        #Liste de nos solveurs à problématiques
        self.issue_list_box = ttk.Combobox(self.window,textvariable=self.selected_issue,values=SOLVABLE_ISSUES)
        #Sa position
        self.issue_list_box.grid(column=1,row=6)
        #Implémentation du bouton, qui lancera le solveur correspondant au choix de l'utilisateur
        issue_button = ttk.Button(self.window,text='Résoud ma problématique',command=self.solve_selected_issue)
        #Position du bouton
        issue_button.grid(column=1,row=7)

        #Affichage des résultats graphiques
        self.graph_designer = GraphDesigner()
        #Ici le solver pour la problématique des profils moyens
        self.solver = ProblemSolver()

        self.window.mainloop()
        
    def load_data(self, data_to_load):
        self.current_page_label_var.set(str(self.CURRENT_PAGE))
        columns = ['id','age','genre','niveau_education','emploi','annees_exprerience','salaire']

        #Création d'un widget Treeview dans l'interface graphique, celui_ci est utilisé pour afficher des données 
        # sous forme d'arbre, avec des en-têtes de colonne pour organiser les données.
        self.data_tree = ttk.Treeview(self.window, columns=columns, show='headings')
        #Implémentation des en-têtes
        self.data_tree.heading('id', text='Identifiant')
        self.data_tree.heading('age', text='Age')
        self.data_tree.heading('genre', text='Genre')
        self.data_tree.heading('niveau_education', text='Niveau d\'éducation')
        self.data_tree.heading('emploi', text='Emploi')
        self.data_tree.heading('annees_exprerience', text='Années d\'exprérience')
        self.data_tree.heading('salaire', text='Salaire')
        self.data_tree.grid(column=1,row=3)
        #Ici la boucle pour insérer les données
        for data in data_to_load:
            data_to_insert = []
            for item in data.values():
                data_to_insert.append(item)
            self.data_tree.insert('',END,values=data_to_insert)

#Méthodes des boutons:
    #Définition méthode du retour à la page précécdente
    def previous_page(self):
        if(self.CURRENT_PAGE>0):
            self.CURRENT_PAGE = self.CURRENT_PAGE-1
            new_results = UIMethods.get_bdd_data((self.CURRENT_PAGE))
            self.load_data(new_results)
    #Définition méthode pour afficher la page suivante
    def next_page(self):
        self.CURRENT_PAGE = self.CURRENT_PAGE+1
        new_results = UIMethods.get_bdd_data((self.CURRENT_PAGE))
        self.load_data(new_results)
    #Définition de la méthode de résolution de la problématique
    #On appelle le solveur et le graphique (ou résultat) correspondants à la problématique choisie
    def solve_selected_issue(self):
        results = self.solver.solveIssue(self.issue_list_box.get())
        self.graph_designer.designGraph(self.issue_list_box.get(), results)