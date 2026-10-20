import dice

die = dice.D6()

### checking distribution of rolls over n rolls ###

number_of_rolls = 10000

num_of_1 = 0
num_of_2 = 0
num_of_3 = 0
num_of_4 = 0
num_of_5 = 0
num_of_6 = 0

for i in range(number_of_rolls):

    roll = die.roll()

    match roll:
        case 1:
            num_of_1 += 1
        case 2:
            num_of_2 += 1
        case 3:
            num_of_3 += 1
        case 4:
            num_of_4 += 1
        case 5:
            num_of_5 += 1
        case 6:
            num_of_6 += 1

print("over", number_of_rolls, "rolls the dice rolled:")

print(num_of_1, "ones")
print(num_of_2, "twos")
print(num_of_3, "threes")
print(num_of_4, "fours")
print(num_of_5, "fives")
print(num_of_6, "sixes")

