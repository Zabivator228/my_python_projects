import random

def is_valid(n, granica): # функция валидности числа
    return 1 <= n <= granica

def play_again(): # функция повтора игры
    while True:
        povtor = input('Будем играть ещё? (Да/Нет)').lower()
        if povtor in ('да', 'нет'):
            return povtor == 'да'
        print('Не понял вас. Да, или нет?')   

def game_loop(): 
    print('Добро пожаловать в числовую угадайку!')

    while True:  # Основной цикл игры
        print('В каком диапазоне вы хотите угадать число? Введите правую границу диапазона (например 100)')
        granica = int(input())
        right_num = random.randint(1, granica)
        attempts = 0
        print('Какое количество попыток вы хотите установить? Если попытки кончатся - вы проиграете')
        max_attempts = int(input())

        while attempts < max_attempts:  # Цикл попыток
            print(f'Введите число от 1 до {granica} включительно.')
            user_num = int(input())

            if not is_valid(user_num, granica):
                print(f'А может быть все-таки введем целое число от 1 до {granica}?')
                continue

            if user_num < right_num:
                print(f'Ваше число меньше загаданного, попробуйте еще разок. Осталось попыток: {max_attempts - attempts - 1}')
                attempts += 1
            elif user_num > right_num:
                print(f'Ваше число больше загаданного, попробуйте еще разок. Осталось попыток: {max_attempts - attempts - 1}')
                attempts += 1
            else:
                print('Вы угадали! Поздравляем!')
                print(f'Количество неудачных попыток: {attempts}')
                if not play_again():
                    print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')
                    return
                else:
                    break
               

        else:  # Этот блок выполняется, если цикл while attempts < max_attempts завершился без break (т.е. попытки закончились)
            print('Вы исчерпали все попытки. Вы проиграли.')
            print(f'Загаданное число было {right_num}')
            if not play_again():
                print('Спасибо, что играли в числовую угадайку. Ещё увидимся...')
                return
            continue

game_loop()