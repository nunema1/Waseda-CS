# In Class messing around with more classes

class Animal:
    def __init__(self, name, age, hunger, diet):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.diet = ["meat", "veg"]
    def feed(self, foodtype):
        if self.diet.index(foodtype) == True:
            if self.hunger() < 100:
                self.hunger += 5
                print("Yum!")
            else:
                print("Too full to eat")
        else:
            return "Non-Valid FoodType"

class Carnivore:
    def __init__(self):
        pass

class Herbivore:
    def __init__(self):
        pass

class Omnivore:
    def __init__(self):
        pass