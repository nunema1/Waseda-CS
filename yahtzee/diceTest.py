import dice

d6 = dice.D6()
d6two = dice.D6()
average = 0
sum = 0
numRoll = 10
roll = 0

for i in range(1, numRoll):
    roll = d6.roll()
    roll2 = d6two.roll()
    print(roll)
    print(roll2)
    sum += roll
    sum += roll2
average = sum / numRoll
print(average)
