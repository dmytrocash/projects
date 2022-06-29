#1
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

import random

length = len(names) - 1
random_int = random.randint(0, length)
random_name = names[random_int]

print(f"{random_name} is going to buy the meal today!")

#2
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
random_name = random.choice(names)

print(f"{random_name} is going to buy the meal today!")