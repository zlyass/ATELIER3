# La classe Point
class Point:
    # Constructor de la classe Point
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    # La méthode toString() pour la classe Point
    def __str__(self):
        return f"({self.x}, {self.y})"

# La classe Segment
class Segment:
    # Constructor de la classe Segment
    def __init__(self, x1=0.0, y1=0.0, x2=0.0, y2=0.0):
        self.orig = Point(x1, y1)
        self.extrem = Point(x2, y2)
    # La méthode toString() pour la classe Segment
    def __str__(self):
        return f"Segment de {self.orig} à {self.extrem}"
print("---------------------------------")
# Une instance de la classe Point
point = Point(1,4)

# L'affichage de l'instance
print("Le point ",point)

print("---------------------------------")
# Une instance de la classe Segment
segment = Segment(1, 2, 3, 4)

# L'affichage de l'instance.
print(segment)