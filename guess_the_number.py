import random
wins = 0
best_score = 30


while True:
    guesses = 0
    history = []
    space = "-" * 80
    print(space)
    print("Welcome to the Number Guessing Game!")
    difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
    print()
    print("-" *80)
    print()

    while difficulty not in ["easy", "medium", "hard"]:
        print(space)
        print("Invalid difficulty level. Please choose from the options")
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()

    if difficulty == "easy":
        print(space)
        secret = random.randint (1, 50)
        max_guesses = 10
        range_hint = "between 1 and 50"
    elif difficulty == "medium":
        print(space)
        secret = random.randint (1,500)
        max_guesses = 12
        range_hint = "between 1 and 500"
    elif difficulty == "hard":
        print(space)
        secret = random.randint (1, 1000)
        max_guesses = 15
        range_hint = "between 1 and 1000"
    else:
        print("something went wrong with the difficulty selection, defaulting to easy mode")
        secret = random.randint (1, 50)
        max_guesses = 10
        range_hint = "between 1 and 50"

    print(space)
    print()
    print(f"The secret number is {range_hint}")
    print()
    print(space)


    while True:
        guesses += 1

        print(space)
        print()
        print(f"This is guess number {guesses}")
        print()
        

        try:
            print(space)
            print()
            guess = int(input("Enter your guess: "))
            print()

        except ValueError:
            print("Please enter a valid number.")
            continue
        history.append(guess)
        print()
        print(f"your responses so far: {history}")
        print()
        if guess == secret:
            print()
            print(f"you got it in {guesses} tries! yessir you are a winner!!!!!!!")
            print()
            wins += 1
            if guesses < best_score:
                best_score = guesses
                print()
                print (f"NEW RECORD! Your best score is now {best_score} guesses! wow!")
                print()
            break
        elif guess < secret:
            print()
            print("Too low, try again")
            print()
        else:
            print()
            print("too high, try again")
            print()

        distance = abs(guess - secret)

        if distance <= 10:
            print()
            print("you are on fireeeeee!!!")
            print()

        elif distance <= 50:
            print()
            print("you are getting warmer, keep going!")
            print()
            
        else:
            print()
            print("you are freezing cold, try again!")
            print()

        if max_guesses - guesses == 5:
            print()
            print("youve got 5 more guesses left, keep trying!")
            print()

        if guesses == max_guesses:
            print()
            print(f"Sorry, you've used all {max_guesses} guesses. The secret number was {secret}. Better luck next time!")
            print()
            break
    print(space)
    print()
    again = input("Wanna give it another go?").lower()

    if again != "yes":
        print("see you next time!")
        if wins > 0:
            print(f"You won {wins} times! nice!")
            print(f"Your best score is {best_score} guesses! impressive!")
        print()
        break