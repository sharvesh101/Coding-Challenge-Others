import random

secret_number = random.randint(1, 10)
print(secret_number)

guess = int(input("Guess The random number: "))

if guess > secret_number:
    print("Too High")
elif guess < secret_number:
    print("Too Low")
else:
    print("Correct")