#Test file to test parent class Animal by print statements
import AnimalsClass

dog = AnimalsClass.Animal("Charlie", 12, 12, 2)

print(dog.name, dog.age, dog.hunger, dog.diet)

print(dog.diet[0])
print(dog.diet[1])

dog.feed('meat')
print(dog.hunger)
dog.feed('veg')
print(dog.hunger)
dog.feed('cow')
print(dog.hunger)
