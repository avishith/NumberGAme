import random
def guess(x):
    random_number = random.randint(1,x)
    guess =0
    trail=0
    while guess!=random_number:
        guess =int(input(f"enter the number b/w 1 and {x} :" ))
        if guess > random_number:
            print('Sorry the guess number is too high')
        elif guess < random_number:
            print('Sorry the guess number is too LOW')
    print(f"Yay That's correct,you guessed {random_number} " )
guess(100)