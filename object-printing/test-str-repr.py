

class Dog:
    i = 5

    def __init__(self):
        self.j = 6

    
    def __str__(self):
        return f"DogStr(i={Dog.i}, j={self.j})"

    def __repr__(self):
        classvar=self.__class__
        classvarname= self.__class__.__name__
        return f"DogRepr(i={Dog.i}, j={self.j}, classvar={classvar}, classvarname={classvarname})"


d = Dog()


print(d)
print(repr(d))
