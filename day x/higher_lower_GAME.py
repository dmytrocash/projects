import random
import os
from higher_lower_DATA import data
from higher_lower_ART import logo
from higher_lower_ART import vs

def compare(guess, followers_count1, followers_count2):
  if followers_count1 > followers_count2:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
continue_game = True
account2 = random.choice(data)

while continue_game:
  account1 = account2
  print(f"Compare A: {account1['name']}, {account1['description']}, from {account1['country']}")
  followers_count1 = account1['follower_count']
  #оставил для проверки
  print(followers_count1)

  print(vs)

  account2 = random.choice(data)
  if account2 == account1:
    account2 = random.choise(data)

  print(f"Against B: {account2['name']}, {account2['description']}, from {account2['country']}")
  followers_count2 = account2['follower_count']
  #оставил для проверки
  print(followers_count2)

  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  os.system("clear")
  print(logo)

  if_correct = compare(guess, followers_count1, followers_count2)

  if if_correct:
    score += 1
    print(f"You're right! Current score: {score}")
  else:
    continue_game = False
    print(f"Sorry, that's wrong. Final score: {score}")