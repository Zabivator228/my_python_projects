# один из моих первых проектов. писал его ещё до установки visual studio, в редакторе IDLE.

import random # импортируем модуль random для генерации случайных чисел

right_num = random.randint(1, 100) # правильный ответ, введя который, игра заканчивается
attempts = 0 # переменная попыток, которая увеличивается при каждой неудачной попытке

def is_valid(n): # функция проверки валидности числа
    if 1 <= n <= 100:
        return True
    else:
        return False

print('Добро пожаловать в числовую угадайку!')    
while True: 
    print('Введите число от 1 до 100 включительно.')
    user_num = int(input())
    if is_valid(user_num) == False: 
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    if user_num < right_num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        attempts += 1
        continue
    elif user_num > right_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        attempts += 1
        continue
    elif user_num == right_num:
        print('Вы угадали! Поздравляем!')
        print(f'Количество неудачных попыток: {attempts}')
        print('Будем играть ещё? (Да/Нет)')
        povtor = input().lower()
        if povtor == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif povtor == 'да':
            right_num = random.randint(1, 100)
            attempts = 0
            continue
