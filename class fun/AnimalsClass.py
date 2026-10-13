# In Class messing around with more classes

class Animal:
    def __init__(self, name, age, hunger, diet):
        self.name = name
        self.age = age
        self.hunger = hunger
        self.diet = ["meat", "veg","bull"]
    def feed(self, foodtype):
        if self.diet.__contains__(foodtype):
            if self.hunger < 100:
                self.hunger += 5
                print("Yum!")
            else:
                print("Too full to eat")
        else:
            print("Non-Valid FoodType")

