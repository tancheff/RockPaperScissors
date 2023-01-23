import random

count_games = 0
count_wins = 0
count_draws = 0

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid input. Please try again...")

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
        print(f"The computer chose {computer_move}.")
    elif computer_random_number == 2:
        computer_move = paper
        print(f"The computer chose {computer_move}.")
    else:
        computer_move = scissors
        print(f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        count_wins += 1
        print("You win!")
    elif player_move == computer_move:
        count_draws += 1
        print("Draw.")
    else:
        print("You lose!")

    count_games += 1

    player_input_final = input("Type [y]es to play again or any other key to quit.")

    if player_input_final == "y":
        continue
    else:
        print("Thank you for playing!")
        print(f"Total Games: {count_games}. Total Wins: {count_wins}. "
              f"Total Losses: {count_games-count_wins}. Total Draws: {count_draws}.")
        break
