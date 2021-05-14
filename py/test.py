import numpy as np


def convert_base(num, to_base=10, from_base=10):
    if type(num) is int:
        num = str(num)
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


# генератор правил
def generator(length_of_list=10, a=0):
    while True:
        number = convert_base(a, 3, 10).rjust(length_of_list, '0')
        a += 1

        # if number.count('2') > 2:
        #     continue

        # адаптация к реальным условиям: пример, перевод [2] в [2, 1, 0]
        help_list = []
        for b in range(length_of_list - 1, 0, -1):

            if number[b] == '0':
                help_list = [0] + help_list
            if number[b] == '1':
                help_list = [1, 0] + help_list
            if number[b] == '2':
                help_list = [2, 1, 0] + help_list
            if number[b] == '3':
                help_list = [3, 2, 1, 0] + help_list
            if number[b] == '4':
                help_list = [4, 3, 2, 1, 0] + help_list

        yield help_list


def open_and_convert_results():
    # open
    global results, np_results
    try:
        with open('cache/results.txt', 'r', encoding="utf-8") as file:
            # заполняем массив результатами
            for line in file:
                results.append(float(line[:-1]))
    except Exception as e:
        print('Cannot open the file')
        print(e)
        return

    # conversion
    help_list = []
    for i in range(len(results) - 4, 1, -1):
        if results[i] < 1.2 and results[i + 1] >= 1.2:
            help_list = [0] + help_list
        # двойной
        if results[i] < 1.2 and results[i + 1] < 1.2 and results[i + 2] >= 1.2:
            help_list = [1, 0] + help_list
        # тройный
        if results[i] < 1.2 and results[i + 1] < 1.2 and results[i + 2] < 1.2 and \
                results[i + 3] >= 1.2:
            help_list = [2, 1, 0] + help_list
        # четверные
        if results[i] < 1.2 and results[i + 1] < 1.2 and results[i + 2] < 1.2 and \
                results[i + 3] < 1.2 and results[i + 4] >= 1.2:
            help_list = [3, 2, 1, 0] + help_list
        # пятерные
        if results[i] < 1.2 and results[i + 1] < 1.2 and results[i + 2] < 1.2 and \
                results[i + 3] < 1.2 and results[i + 4] < 1.2 and results[i + 5] >= 1.2:
            help_list = [4, 3, 2, 1, 0] + help_list

    # to numpy array
    np_results = np.array(help_list)


g = generator()
for c in range(0, 3 ** 10):
    print(next(g))

















def get_number_of_bets (arr, pos_of_seq):

    x = 0
    count = 0
    double_crash = False
    while not double_crash:

        x += 1
        if arr[pos_of_seq - x] == 0:
            count += 1
        else:
            count -= 2
            double_crash = True

    if count < 0:
        count = 0

    return count


























