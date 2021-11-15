import random

secret = random.randint(1, 20)
print(secret)
print('I am thinking a secret number between 1 & 20 ')

# Guzzer 6
for g in range(1, 7):
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