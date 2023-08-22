import random #Import Random to faciliate the computer's moves
import math #(Complaint about Banker's Rounding here)

#Global variables
values = ['Rock', 'Paper', 'Scissors']

#||||||||||
#Functions
#||||||||||

#Get the number of rounds the user would like to play
def get_rounds():
  while True:
    rounds_input = input('How many rounds would you like to be best-out-of?: ')
    if rounds_input.isdigit():
      rounds_input = int(rounds_input)
      if rounds_input >= 3 and rounds_input < 11:
        if rounds_input % 2 != 0:
          break
        else:
          print('Number of rounds must be odd. There are no ties in Rock Paper Scissors!')
      else:
        print('Please input a number greater than 3 and less than 11')
    else:
      print('Rounds must be a digit')
  return rounds_input

#Get and validate the player's move
def get_player_move():
  while True:
    move = input('Please choose Rock, Paper, or Scissors: ')
    if move not in values:
      print('Please enter a valid move')
    else:
      break
  return move

#Get the computer's move
def get_comp_move():
  return random.choice(values)

#Find who won the round
def find_round_winner(player_move, comp_move):
  #Tie handling
  if player_move == comp_move:
    print('You both chose the same move!')
    return 2
  #Computer win conditions
  elif player_move == 'Rock' and comp_move == 'Paper':
    print('Computer wins!')
    return 0
  elif player_move == 'Paper' and comp_move == 'Scissors':
    print('Computer wins!')
    return 0
  elif player_move == 'Scissors' and comp_move == 'Rock':
    print('Computer wins!')
    return 0
  #Player wins
  else:
    print('You win!')
    return 1

#||||||||||
#Main
#||||||||||
def main():
  #Variables because I have issues with scope
  player_wins = 0
  comp_wins = 0
  round_counter = 0
  #Welcome user and choose best-out-of
  print("Welcome to Connor's Rock Paper Scissors v1.0!")
  print('\n')
  rounds = get_rounds()
  print('This game will be best out of ' + str(rounds) + '.')
  rounds = math.ceil(rounds / 2) 
  print('Lets begin!')
  print('\n')
  #Actual meat of the game
  while player_wins < rounds and comp_wins < rounds:
    round_counter += 1
    print('--- ROUND', round_counter, '---')
    player_move = get_player_move()
    comp_move = get_comp_move()
    print('You chose', player_move + '.')
    print('The computer chose', comp_move + '.')
    winner = find_round_winner(player_move, comp_move)
    if winner == 1:
      player_wins += 1
    elif winner == 0:
      comp_wins += 1
    print('--- SCORE ---')
    print('You:', player_wins)
    print('Computer:', comp_wins)
    print('\n')
  print('Thanks for playing!')

#Allow for infinite gameplay
while True:
  main()
  infinite_flag = 0
  while infinite_flag == 0:
    keep_going = input('Would you like to play again? Y/N: ')
    if keep_going == 'Y':
      print('\n')
      break
    elif keep_going == 'N':
      infinite_flag = 1
    else:
      print('Please enter Y or N')
  if infinite_flag == 1:
    break