import random

secret_number = random.randint(1,190)
attempts = 0

print("Guess the number between 1 & 190")


while True:
    guess = int(input("Enter your guess:"))
    attempts += 1

    if guess < secret_number:
        print("too low!")

    elif guess > secret_number:
        print("Too high")

    else:
        print(f"Congratulations! your guess the correct number in {attempts} attempts.")
        break

