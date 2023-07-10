from enum import Enum

#Création de la classe Enum EduLevel qui permettra de définir un ensemble de valeurs constantes nommées
class EduLevel (Enum):
    HIGH_SCHOOL = 0
    BACHELOR = 3
    MASTER = 5
    PHD = 8

    # Création d'une méthode statique afin de retourner un nombre d'années correspondant à un niveau de diplôme
    @staticmethod
    def getRealValue(value) -> int:
        match value:
            #Dans le cas où le niveau d'études est High School, renvoyer la valeur 0
            case 'High School':
                return EduLevel.HIGH_SCHOOL.value
            #Dans le cas où le niveau d'études est Bachelor, peu importe la syntaxe, renvoyer la valeur 3
            case 'Bachelor\'s' | 'Bachelor' | 'Bachelor\'s Degree':
                return EduLevel.BACHELOR.value
            #Dans le cas où le niveau d'études est Master, peu importe la syntaxe, renvoyer la valeur 5
            case 'Master\'s' | 'Master' | 'Master\'s Degree':
                return EduLevel.MASTER.value
            #Dans le cas où le niveau d'études est PhD, peu importe la syntaxe, renvoyer la valeur 8
            case 'PhD' | 'phD':
                return EduLevel.PHD.value