import personne
import math
from _datetime import date, datetime

class MyClass:
    def __init__(self): # Notre méthode constructeur      
        self.nom = date.today() #{math.sqrt(}
        self.prenom = "Jean" # Quelle originalité
        self.age = 33 # Cela n'engage à rien
        self.lieu_residence = "Paris"


if __name__ == '__main__':
    print("Hello World!!")
    Personne.t()
    j = MyClass()
    print("Name"+j.nom.__str__())
    j = Personne()
    print("Name"+j.nom)
    print("square="+j.square(5.0).__str__())
    
