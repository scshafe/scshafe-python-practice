


class Dog:
    def __init__(self):
        self.i = 1


class Cat:
    def __init__(self):
        print("Cat init")
        self.j = 2
    
    def __enter__(self):
        print("Cat enter")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cat exit")
        return



with Cat() as c:
    print("Cat context manager works")


with Dog() as d:
    print("Dog works too")