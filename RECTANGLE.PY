# Class Rectangle
class Rectangle:

    # Constructor de la classe Rectangle
    def __init__(self, longueur, largeur):
        self.name = "rectangle"
        self.longueur = longueur
        self.largeur = largeur
    
    # La méthode de la surface 
    def surface(self):
        return self.longueur * self.largeur
    
    # La méthode afficher 
    def afficher(self):
        print("{ " + self.name + " , longueur: " + str(self.longueur) + " , largeur: " + str(self.largeur) + " }")

# La classe Carré hirté de la classe Rectangle
class Carre(Rectangle):

    # Constructor de la classe Carré
    def __init__(self, longueur):
        # Constructor de la classe parent
        super().__init__(longueur, longueur)
        self.name = "carré"

    # La méthode afficher (Polymorphisme)
    def afficher(self):
        print("{ " + self.name + " , longueur: " + str(self.longueur) + " }")

print("---------------------------------")
# Une instance de la classe Rectangle
rect = Rectangle(13, 15)
rect.afficher()
print(rect.surface())
print("---------------------------------")
# Une instance de la classe Carré
carre = Carre(16)
carre.afficher()
print(carre.surface())