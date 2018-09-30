import random
min = 1
max = 6
roll_again ="yes"

while roll_again == "yes":
    print("rooling the dices")
    print("the value on the dice sre")
    print(random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("roll the dices again?")       
