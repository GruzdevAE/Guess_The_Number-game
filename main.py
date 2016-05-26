from random import randrange

init = ''
guess = 0
while init != 'exit':
    init = input('Hello! Type \'rules\' to print rules, type number to set max number or type \'exit\' to exit\n')
    if init == 'rules':
        print('''\nThe rules are simle:
            Just type in the number you want to set as the max number
            and start guessing. One number per attempt untill you're succesfull.
            In the end i wil also print the number of attempts it has taken you
            to guess the number.\n''')
    elif init.isdigit():
        number = randrange(int(init))+1
        attempt = 1
        guess = input('\nEnter your guess here: ')
        if guess.isdigit():
            while int(guess) != number:
                if number <= int(guess):
                    print('\nThat\'s too much')
                elif number >= int(guess):
                    print('\nDefinately not that small')
                attempt += 1
                guess = input('\nEnter your guess here: ')
        else:
            print('No, you need to enter digits here.')
        print('Exactly! I\'ve had the', number, 'number in mind!')
        print('You\'ve made it in', attempt, 'attempts')
print('Goodbye!')
