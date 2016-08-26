import time
import random

possibleChoices = ['rock', 'paper', 'scissors']

def start():
  print('Are you ready to take on the rock paper scissors challenge?')
  playerChoice = input('Input your choice here: ')

  if(playerChoice not in possibleChoices):
    print('You have entered an invalid string, please try again!\n')
    start()
  else:
    print('I\'m thinking...')
    time.sleep(2)
    cpuChoice = cpuChoose()
    print()
    compareChoices(playerChoice, cpuChoice)

def cpuChoose():
  cpuChoice = random.choice(possibleChoices)
  return cpuChoice

def compareChoices(choice1, choice2):
  print('You chose', choice1, 'and I chose', choice2)
  if(choice1 == choice2):
    print('It was a draw! Try again!\n')
    start()
  else:
    result = (possibleChoices.index(choice2) + 1) % 3 == possibleChoices.index(choice1)
    result = 'win' if result else 'lose'
    print('You', result + '!')

start()