import random

game_results = ["Wins:", 0, "Draws:", 0, "Losses:", 0, "Total:", 0]
user_behaviour = ["rock:", 0, "paper:", 0, "scissors:", 0]

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

while True:
    player_move = input("Choose [r]ock, [p]aper or [s]cissors: ")

# collecting user behaviour:
    if player_move == "r":
        player_move = rock
        user_behaviour[1] += 1
    elif player_move == "p":
        player_move = paper
        user_behaviour[3] += 1
    elif player_move == "s":
        player_move = scissors
        user_behaviour[5] += 1
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

# under what conditions a player wins:
    if (player_move == rock and computer_move == scissors) \
            or (player_move == paper and computer_move == rock) \
            or (player_move == scissors and computer_move == paper):
        game_results[1] += 1
        print("You win!")

# under what conditions the match is a draw or a loss:
    elif player_move == computer_move:
        game_results[3] += 1
        print("Draw.")
    else:
        game_results[5] += 1
        print("You lose!")

    game_results[7] += 1

    player_input_final = input("Type [y]es to play again or any other key to quit.")

    if player_input_final == "y":
        continue
    else:
        print("Thank you for playing!")
        print(" ".join(map(str, game_results)))
        print("You choices were " + " ".join(map(str, user_behaviour)))
        print(f"Success Rate: {game_results[1]/game_results[7]:.2f}%")

        break
