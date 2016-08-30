import time
import random

possibleChoices = ['rock', 'lizard', 'spock', 'scissors', 'paper']

def start():
  print('Are you ready to take on the rock paper scissors lizard spock challenge?')
  playerChoice = input('Input your choice here: ')

  if(playerChoice not in possibleChoices):
    print('You have entered an invalid string, please try again!\n')
    return start()
  else:
    print('I\'m thinking...')
    time.sleep(random.uniform(1.7, 2.5))
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
    return start()
  else:
    result = (possibleChoices.index(choice1) + 1) % 5 == possibleChoices.index(choice2)
    result = result if result else (possibleChoices.index(choice1) - 2) % 5 == possibleChoices.index(choice2)
    result = 'win' if result else 'lose'
    print('You', result + '!')

start()
