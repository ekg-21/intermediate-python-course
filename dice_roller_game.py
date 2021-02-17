#Make sure to only edit within MAIN
def main():
  import random
  player1_name = input("Enter player 1 name: ")
  player2_name = input("Enter player 2 name: ")
  goal = int(input('Set a goal score of sum of dice: '))
  #dice_rolls = int(input('How many dice would you like to roll per round for each player? '))
  dice_size = int(input('How many sides are the dice? '))
  current_turn = 1
  dice_sum_p2 = 0
  dice_sum_p1 = 0
  while True:
    if current_turn == 1:
      print(f"{player1_name}'s turn")
      for i in range(0,1):
        roll = random.randint(1,dice_size)
        dice_sum_p1 += roll
        if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
        else:
          print(f'You rolled a {roll}')
      if dice_sum_p1 == goal or dice_sum_p1 > goal:
        print(f'{player1_name} has rolled a total of {dice_sum_p1}\nYou win!')
        break
      else:
        current_turn = current_turn * -1
        print(f'{player1_name} has rolled a total of {dice_sum_p1} so far\n')

    if current_turn == -1:  
      print(f"{player2_name}'s turn")
      for i in range(0,1):
        roll = random.randint(1,dice_size)
        dice_sum_p2 += roll
        if roll == 1:
          print(f'You rolled a {roll}! Critical Fail')
        elif roll == dice_size:
          print(f'You rolled a {roll}! Critical Success!')
        else:
          print(f'You rolled a {roll}')
      if dice_sum_p2 == goal or dice_sum_p2 > goal:
          print(f'{player2_name} has rolled a total of {dice_sum_p2}\nYou win!')
          break
      else:
        current_turn = current_turn * -1
        print(f'{player2_name} has rolled a total of {dice_sum_p2} so far\n')

if __name__== "__main__":
  main()