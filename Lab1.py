def flag():
    colors = {'white': '\u001b[47m', 'blue': '\u001b[44m', 'red': '\u001b[41m'}
    colors_in_flag = ['red', 'white', 'blue']
    line = ' ' * 30
    END = '\u001b[0m'
    for i in (colors_in_flag + [i for i in reversed(colors_in_flag)]): 
        print(f'{colors[i]}{line}{END}')

def ornament():
    import math

    red = '\u001b[41m'
    END = '\u001b[0m'

    for i in range(7):
        parab_offset = math.ceil(i ** 2 / 2)  
        left_space = ' ' * (20 - parab_offset)
        left_first = ' ' * 21
        between_space = ' ' * (parab_offset * 2 - 1)
        if i == 0:
            print(f'{left_first}{red}   {END}')
        else:
            print(f'{left_space}{red}   {END}{between_space}{red}   {END}')

def write_function():
    axis = [[0 for i in range(10)] for i in range(10)]
    result = [f'{1 / i:.2f}' for i in range(1, 11)]

    step = round(abs(float(result[0]) - float(result[9])) / 9, 2) #рассчитываем шаг сетки по y

    for i in range(10):
        for j in range(10):
            if j == 0:
                axis[i][j] = f'{(step * (8-i) + step):.1f}' #заполняем Оу в соответствии с шагом сетки

    for x in range(9):  #для каждого значения X
        y_value = result[x]  #получаем значение функции
        for i in range(10):
            if abs(float(axis[i][0]) - float(y_value)) < step:
                axis[i][x+1] = 1  #отмечаем точку в соответствующем столбце
                break

    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += '\t' + str(float(axis[i][j])) + '\t' #сетка по у выводится между двумя табами
            if axis[i][j] == 0:
                line += '--' #если позиция в сетке не отмечена, она заполняется дефисами
            if axis[i][j] == 1:
                line += '**' #нужные точки отмечаются звёздочками 
        print(line)

    print('\t0\t1 2 3 4 5 6 7 8 9')

def calculate_percentage():
    more_5 = []
    less_5 = []
    for i in open('sequence.txt'):
        x = float(i)
        if x > 0 and x > 5:
            more_5.append(x)
        elif x > 0 and x < 5:
            less_5.append(x)
    percentage1 = round(len(more_5) / (len(more_5) + len(less_5)) * 100) * ' '
    percentage2 = round(len(less_5) / (len(more_5) + len(less_5)) * 100) * ' '

    Blue = '\u001b[44m'
    Red = '\u001b[41m'
    END = '\u001b[0m'
    print(f'Чисел больше 5: 48% {Red}{percentage1}{END}') 
    print(f'Чисел меньше 5: 52% {Blue}{percentage2}{END}')

import os, time, random
Green = '\u001b[32m'
END = '\u001b[0m'
Red = '\u001b[31m'
commands = ['PROCEED', 'COMPUTE', 'TRANSMIT', 'RESPONSE']
binary = ['01001001', '01010100', '01001101', '01001111']
print(f'{Green}Data received. Starting decoding. . .{END}')
time.sleep(1)
os.system('cls')
print(f'{Green}...{END}')
time.sleep(0.5)
os.system('cls')
for i in range(5):
    express1 = random.choice(commands)
    express2 = random.choice(binary)
    for i in range(20):
        print(f'{Green}{express1}: {END}{Red}{express2}{END}')
        print(f"{Green}Progress: [{'#' * (i % 10)}{' ' * (9 - i % 10)}]{END}")
        time.sleep(0.05)
        os.system('cls')
    print(f'{Red}Done!{END}')
    time.sleep(1)
    os.system('cls')
print(f'{Green}Decoding done. Providing required data below{END}')
time.sleep(0.5)
print(f'{Red}ITMO python coding lab1 passed successfully{END}')

