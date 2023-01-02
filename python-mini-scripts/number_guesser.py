import random

while True:
    top_of_range = input("Type a number: ")  # "5" -> int(top_of_range) -> 5

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0:
            print("Please type a number larger than 0 next time")
            continue
        
        break
    else:
        print("Please type a number next time")
        continue
        

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    user_guess = input("Make a guess: ")
    guesses += 1

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You git it!")
        print("You got it in", guesses, "guesses")
        break
    elif user_guess > random_number:
        print("You were above the number!")
        
    else: 
        print("You were below the number!")
        
