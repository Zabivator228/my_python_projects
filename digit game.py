import random

def is_valid(n):
    return 1 <= n <= granica

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

        if not is_valid(user_num):
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
            print('Будем играть ещё? (Да/Нет)')
            povtor = input().lower()
            while povtor not in ('да', 'нет'):
                print('Не понял вас. Да, или нет?')
                povtor = input().lower()

            if povtor == 'нет':
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
                break  # Выход из внешнего цикла, если не хотим играть больше
            else:  # Если 'да', начинаем новую игру
                break #выход из цикла попыток, чтобы началась новая игра

    else:  # Этот блок выполняется, если цикл while attempts < max_attempts завершился без break (т.е. попытки закончились)
        print('Вы исчерпали все попытки. Вы проиграли.')
        print(f'Загаданное число было: {right_num}')
        # ВОПРОС О ПОВТОРНОЙ ИГРЕ ПЕРЕНЕСЕН ИЗ ЭТОГО МЕСТА, ЧТОБЫ НЕ ДУБЛИРОВАТЬ КОД
        print('Будем играть ещё? (Да/Нет)')
        povtor = input().lower()
        while povtor not in ('да', 'нет'):
            print('Не понял вас. Да, или нет?')
            povtor = input().lower()

        if povtor == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break  # Выход из внешнего цикла, если не хотим играть больше

    if povtor == 'нет':
        break #выход из основного цикла
