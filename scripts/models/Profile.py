from EduLevel import EduLevel

#Création de la class Profile 
class Profile:
    #Définition des propriétés correspondant aux champs de notre base de données
    def __init__(self, age : float | int, gender : str, edu_lvl : str, job_title : str, years_of_xp : float, salary : float | int):
        self.age = int(age)
        self.gender = gender
        self.education_level = EduLevel.getRealValue(edu_lvl)
        self.job_title = job_title
        self.years_of_xp = years_of_xp
        self.salary = int(salary)