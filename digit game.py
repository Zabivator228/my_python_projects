# один из моих первых проектов. писал его ещё до установки visual studio, в редакторе IDLE.

import random # импортируем модуль random для генерации случайных чисел

attempts = 0 # переменная попыток, которая увеличивается при каждой неудачной попытке

def is_valid(n): # функция проверки валидности числа
    if 1 <= n <= granica:
        return True
    else:
        return False
    

print('Добро пожаловать в числовую угадайку!') 
print('В каком диапазоне вы хотите угадать число? Введите правую границу диапазона (например 100)')
granica = int(input())
right_num = random.randint(1, granica)
while True: # основной цикл игры
    print(f'Введите число от 1 до {granica} включительно.')
    user_num = int(input())
    if is_valid(user_num) == False: # вызываем функцию для проверки
        print(f'А может быть все-таки введем целое число от 1 до {granica}?')
        continue
    if user_num < right_num: # здесь и ниже, проверки, как введённое число относится к правильному
        print('Ваше число меньше загаданного, попробуйте еще разок')
        attempts += 1
        continue
    elif user_num > right_num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        attempts += 1
        continue
    elif user_num == right_num:
        print('Вы угадали! Поздравляем!')
        print(f'Количество неудачных попыток: {attempts}') # здесь программа показывает количество неудачных попыток. То есть, последняя попытка была правильной и в счётчик не идёт
        print('Будем играть ещё? (Да/Нет)') # предложение начать игру заново или завершить работу программы
        povtor = input().lower()
        while povtor not in ('да', 'нет'): # проверка, является ли введённая строка допустимым значением, да или нет
            print('Я тебя не понимаю. Да, или нет?')
            povtor = input().lower()
            continue
        if povtor == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif povtor == 'да':
            print('Какой диапазон хочешь на этот раз?')
            granica = int(input())
            right_num = random.randint(1, granica)
            attempts = 0
            continue
