from os import system
from random import randrange, shuffle, choice

init = ''
max_attempts = 0
max_num = 100
game_choice = None
while init != "Выход":
    system('cls')
    game_choice = input('Я вспомнил парочку игр. Не желаешь сыграть?' +
                        '\nМогу предложить \'Угадай число\' или \'Анаграммы\'')
    if game_choice == 'Угадай число':
        system('cls')
        init = input('Давай сыграем в угадай число. +
                     '\nНапиши "Правила" для вывода правил' +
                     '\nДля изменения параметров напиши "Параметры"' +
                     '\nДля начала игры напиши "Игра"' +
                     '\nДля выхода напиши "Выход"')
        if init == 'Правила':
            system('cls')
            print('Всё очень просто:' +
                  '\nЯ загадываю число, ты угадываешь его.' +
                  '\nЕсли хочешь, можно установить максимальное число попыток.' +
                  '\nВ противном случае, игра продолжается до тех пор, пока ты не отгадаешь число.' +
                  '\nВ конце я так же выведу количество попыток, за которое ты угадал число.' +
                  '\nЕсли хочешь, так же можем и поменяться ролями')
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
            yesno = input('Хочешь поменяться ролями?')
            if yesno == 'Нет':
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
            elif yesno == 'Да':
                print('Хорошо, загадывай число, но давай по-честному!')
                max_num_pc = input('Какое число будет максимальным?')
                cheat = input('''Ну что загадал? 
                Знаю я тебя, сейчас, в процессе игры, ещё десять раз поменяешь число.
                Давай пиши сюда. И сам не забудешь, и я буду уверен что ты не мухлюешь.''')
                if cheat:
                    print('Таааак. Мне кажется, это число', cheat, '. Ну что, я угадал? Можешь не отвечать, я и так знаю что угадал, я же великолепен!')
                else:
                    print('А тебя не так просто провести. Ну что ж, так даже интересней.')
                    print('Давай условимся отвечать строго является ли моё число \'Больше\', \'Меньше\' или же я \'Угадал\'')
                    answer = ''
                    min_num_pc = 0
                    while answer != 'Угадал':
                        guess_pc = int(max_num_pc) - (int(max_num_pc)-min_num_pc)//2
                        answer = input(guess_pc)
                        if guess_pc == max_num_pc:
                            print ('Эй! Да ты жульничаешь! Я так и знал! Ну да ладно, я и сам, ведь, пытался. Так что мы квиты, да?')
                            input('Жми \'Enter\' для возврата в меню.')
                            break
                        if answer == 'Больше':
                            max_num_pc = guess_pc
                        elif answer == 'Меньше':
                            min_num_pc = guess_pc
                    print('Здорово, я, наконец, угадал!')
                    input('Дави \'Enter\' и давай ещё раз попробуем!')
    elif game_choice == 'Анаграммы':
        pass
    else:
        print('Не понял, давай ещё раз.')
print('До встречи.')
input('Нажми \'Enter\', чтобы выйти')
