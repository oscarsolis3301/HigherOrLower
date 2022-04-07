from art import logo, vs
from info import data
import random
import os

playing = True
score = 0
correct = True


def generate(generate_A, generate_B):
    """Generates two random values from the start to the end of the list"""
    generate_A = random.randint(0, len(data) - 1)
    generate_B = random.randint(0, len(data) - 1)
    return generate_A, generate_B

def checker():
    """Checks the user's input and returns True if they got it correct, or False if incorrect"""
    user_guess = input("Who has more followers? Type 'A' or 'B': ")
    if user_guess.lower() == 'a':
        choice_A = data[generate_A]['follower_count']
        choice_B = data[generate_B]['follower_count']
        if choice_A > choice_B:
            return True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            return False
    elif user_guess.lower() == 'b':
        choice_A = data[generate_A]['follower_count']
        choice_B = data[generate_B]['follower_count']
        if choice_A < choice_B:
            return True
        else:
            print(f"Sorry, that's wrong. Final score {score}")
            return False


while correct:
    """Main game loop"""
    os.system('cls||clear')

    print(logo)
    generate_A = ''
    generate_B = ''
    generate_A, generate_B = generate(generate_A, generate_B)

    if correct == True and score != 0:
        print(f"You're right! Current score: {score}")

    print(f"Compare A: {data[generate_A]['name']}, a {data[generate_A]['description']}, from {data[generate_A]['country']}")
    print(vs)

    if generate_A == generate_B:
        generate_B = random.randint(0, len(data))
    print(f"Against B: {data[generate_B]['name']}, a {data[generate_B]['description']}, from {data[generate_B]['country']}")
    
    correct = checker()
    if correct == True:
        score += 1
    
    
    
    
  

