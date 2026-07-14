# Number Guessing Game(Task 4)
import random
num = random.randint(1, 100)
count = 0
while True:
    guess = int(input("Enter your guess (1-100): "))
    count += 1
    if guess < num:
        print("Too Low!")
    elif guess > num:
        print("Too High!")
    else:
        print("Congratulations! You guessed correctly.")
        print("Total guesses:", count)
        break