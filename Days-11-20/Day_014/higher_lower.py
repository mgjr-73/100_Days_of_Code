import art
import game_data
from random import randint
from os import system, name


# Refresh screen before printing result. See https://www.geeksforgeeks.org/clear-screen-python/
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    elif name == 'posix':
        _ = system('clear')

# Pick random game_data
def pick_game_data():
    index = randint(0,(len(game_data.data)-1))
    return game_data.data[index]

# Pick game_data for B and make sure it's different from A on every round.
def game_round(data_A):
    data_B = (pick_game_data())
    while data_A == data_B:
        data_B = (pick_game_data())

    return data_B

# Evaluate correct answer and return correct answer and game_data that will replace game_data1
def evaluate_data(count1, count2):
    answer = 'a'
    carry_over_data = count1
    if count2['follower_count'] > count1['follower_count']:
        answer = 'b'
        carry_over_data = count2

    return answer, carry_over_data


game_data1 = (pick_game_data())
response = ""
score = 0
while True:
    clear_screen()
    game_data2 = (game_round(game_data1))

    print(art.logo)
    print(response)
    print(f"Compare A: {game_data1['name']}, a {game_data1['description']}, from {game_data1['country']}.")
    print(art.vs)
    print(f"Against B: {game_data2['name']}, a {game_data2['description']}, from {game_data2['country']}.")

    player_answer = input("Who has more followers? Type 'A' or 'B' ")
    correct_answer, next_data = evaluate_data(game_data1, game_data2)

    if player_answer.lower() == correct_answer:
        score += 1
        response = f"You are right! Current score: {score}"
        game_data1 = next_data
    else:
        clear_screen()
        print(f"Sorry that's wrong. Final score {score}")
        break

