import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Décorateur pour créer un cercle via le diamètre
    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area()})"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __gt__(self, other):
        return self.radius > other.radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius


# Tests
c1 = Circle(5)
c2 = Circle(3)
c3 = Circle.from_diameter(10)  # rayon = 5

print(c1)
print(f"Aire : {c1.area()}")
print(f"c1 + c2 : {c1 + c2}")
print(f"c1 > c2 : {c1 > c2}")
print(f"c1 == c3 : {c1 == c3}")

cercles = [Circle(7), Circle(2), Circle(5), Circle(1)]
print(f"Triés : {[str(c) for c in sorted(cercles)]}")