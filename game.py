from art import logo, vs
from info import data
import random
import os

playing = True
score = 0
correct = False


while playing:
    os.system('cls||clear')

    generate_A = random.randint(0, len(data) - 1)
    print(logo)

    if correct == True:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {data[generate_A]['name']}, a {data[generate_A]['description']}, from {data[generate_A]['country']}")
    print(vs)
    generate_B = random.randint(0, len(data) - 1)

    if generate_A == generate_B:
        generate_B = random.randint(0, len(data))
    print(f"Against B: {data[generate_B]['name']}, a {data[generate_B]['description']}, from {data[generate_B]['country']}")
    

    
    user_guess = input("Who has more followers? Type 'A' or 'B': ")

    if user_guess.lower() == 'a':
        choice_A = data[generate_A]['follower_count']
        choice_B = data[generate_B]['follower_count']
        if choice_A > choice_B:
            score += 1
            correct = True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            playing = False

    elif user_guess.lower() == 'b':
        choice_A = data[generate_A]['follower_count']
        choice_B = data[generate_B]['follower_count']
        if choice_A < choice_B:
            score += 1
            currect = True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            playing = False

