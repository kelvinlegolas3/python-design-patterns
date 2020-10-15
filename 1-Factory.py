class Dog:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"Woof! My name is {self.name}!"
    
class Cat:
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"Meow! My name is {self.name}!"
    

def Get_Pet(pet_type, name):
    
    """Factory Method"""
    """A creational pattern that uses factory methods to deal with the problem of creating objects without having 
    to specify the exact class of the object that will be created."""
    
    pets = dict(dog=Dog(name), cat=Cat(name))
    
    return pets[pet_type]

dog = Get_Pet("dog", "Chachi")
print(dog.speak())

cat = Get_Pet("cat", "Kulit")
print(cat.speak())