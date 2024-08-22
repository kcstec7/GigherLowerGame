# Exercise Higher Lower Game
import os
from Day_14_Art import logo, vs
from Day_14_Data import data
from random import randint

def print_header():
    os.system('cls')
    print(logo)

def pick_people(previous_option):

    if previous_option != {}:
        random_option_A = previous_option
    else:
        random_index_1 = randint(0, number_of_records - 1)
        random_option_A = data[random_index_1]
        previous_options.append(random_index_1)

    random_option_B = {}
    while random_option_B == {}:
        random_index_2 = randint(0, number_of_records - 1)

        if random_index_2 not in previous_options:
            random_option_B = data[random_index_2]
            previous_options.append(random_index_2)

    return random_option_A, random_option_B

def print_description(description):

    if (description[0].lower() == 'a' or
            description[0].lower() == 'e' or
            description[0].lower() == 'i' or
            description[0].lower() == 'o' or
            description[0].lower() == 'u'):
        return "an " + description
    else:
        return "a " + description
def get_details(random_option_A, random_option_B):

    print(f"Compare A: {random_option_A["name"]}, {print_description(random_option_A["description"])}, from {random_option_A["country"]}")
    print(vs)
    print(f"Against B: {random_option_B["name"]}, {print_description(random_option_B["description"])}, from {random_option_B["country"]}\n\n")

    followers_A = random_option_A["follower_count"]
    followers_B = random_option_B["follower_count"]

    # print(f"Debug: A = {followers_A}, B = {followers_B}")

    return followers_A, followers_B

def guess_and_check(followers_A, followers_B):

    guess = ""
    while guess != "A" and guess != "B":
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    if guess == "A" and followers_A > followers_B:
        return "R"  # For RIGHT
    elif guess == "B" and followers_B > followers_A:
        return "R"  # For RIGHT
    else:
        return "W"  # For WRONG

print_header()
number_of_records = len(data)
score = 0
continue_game = True
previous_winner = {}
previous_options = []

while continue_game:

    option_A, option_B = pick_people(previous_winner)
    num_followers_A, num_followers_B = get_details(option_A, option_B)

    if guess_and_check(num_followers_A, num_followers_B) == "R":

        score += 1

        print_header()
        print(f"You're right! Current score: {score}\n")

        if len(previous_options) == len(data):
            print("Congratulations! You got all the answers right!")
            continue_game = False
        else:
            if num_followers_A > num_followers_B:
                previous_winner = option_A
            else:
                previous_winner = option_B
    else:
        print(f"\nSorry, that's wrong. Final score: {score}")
        continue_game = False
