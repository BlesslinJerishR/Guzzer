import random

start = int(input("Enter Start : "))
stop = int(input("Enter Stop : "))
secret = random.randint(start, stop)
life = int(input("yo got Lives ? "))
print(secret)
print(f'I am thinking a secret number between {start} & {stop}')

# Guzzer 6
for g in range(life):
    guess = int(input('Guzz now : '))

    if guess < secret:
        print('Too Low')
    elif guess > secret:
        print('Too High')
    else:
        # Correct Guess
        break

if guess == secret:
    print('Good Job you Guezzed my number in ' + str(g) + ' Guzzes')
else:
    print('You Had only one Job')