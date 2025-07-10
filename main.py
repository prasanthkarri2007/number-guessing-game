#number guessing game

import random



lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = (input("Enter your guess: "))

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < lowest_num or guess > highest_num:
            print("Your guess is out of range.")

        elif guess < answer:
            print("Your guess is too low.")

        elif guess > answer:
            print("Your guess is too high.")

        elif guess == answer:
            print("Congratulations, you guessed the number!")
            print(f"You guessed the number in {guesses} guesses")
            break
    else:
        print("Invalid input")