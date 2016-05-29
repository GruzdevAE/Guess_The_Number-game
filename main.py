from os import system
from random import randrange

init = ''
max_attempts = 0
max_num = 100
while init != "Выход":
    system('cls')
    init = input('''Привет! Давай сыграем в угадай число.
Напиши "Правила" для вывода правил
Для изменения параметров напиши "Параметры"
Для начала игры напиши "Игра"
Для выхода напиши "Выход"''')
    if init == 'Правила':
        system('cls')
        print('''Всё очень просто:
Я загадываю число, ты угадываешь его.
Если хочешь, можно установить максимальное число попыток.
В противном случае, игра продолжается до тех пор, пока ты не отгадаешь число.
В конце я так же выведу количество попыток, за которое ты угадал число.''')
        input('Нажми любую кнопку для возврата в меню')
        system('cls')
    elif init == 'Параметры':
        system('cls')
        options = ''
        while options != 'Меню':
            system('cls')
            print('Параметры:')
            print('Максимальное число:', max_num)
            print('Число попыток:', max_attempts)
            print('Если число попыток установить 0, количество попыток будет бесконечным.')
            options = input('Введи параметр для изменения или "Меню" для выхода в меню: ')
            if options == 'Максимальное число':
                max_num = int(input('Введи максимальное число, до которого можно загадывать: '))
            if options == 'Число попыток':
                max_attempts = int(input('Введи максимальное число попыток, которое ты можешь использовать: '))
    elif init == 'Игра':
        system('cls')
        print('Дай-ка подумать...')
        number = randrange(max_num)+1
        print('Всё, я загадал. Можешь начинать.')
        guess = 0
        attempt = 0
        while int(guess) != number:
            if attempt == max_attempts and max_attempts != 0:
                print('Ты проиграл, у тебя закончились попытки.')
                break
            guess = input('Введи число: ')
            if guess.isdigit():
                if int(guess) < number:
                    print('Маловато, давай ещё раз.')
                elif int(guess) > number:
                    print('Слишком много.')
                attempt += 1
            else:
                print('Нет, я просил число. Давай ещё раз')
        if attempt < max_attempts or max_attempts == 0:
            print('Отлично! Ты угадал всего за', attempt-1, 'попыток!')
        input('Нажми \'Enter\' чтобы продолжить')
        system('cls')
print('До встречи.')
input('Нажми \'Enter\', чтобы выйти')
