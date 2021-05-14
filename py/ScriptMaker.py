def make_scripts(algorithms, sm_ratio):
    # берем алгоритмы из файла
    '''
    algorithms = []
    with open('cache/good_sequences.txt', 'r', encoding="utf-8") as sm_file:
        for line in sm_file:
            algorithms.append(line[:-1])
    '''

    with open('cache/good_sequences.js', 'w', encoding="utf-8") as file:
        # перебор всех алгоритмов
        for sm_i in range(0, len(algorithms)):

            file.write('if (')
            length = len(algorithms[sm_i]) - 1
            for n in range(length, -1, -1):

                # первый
                if n == length:
                    if int(algorithms[sm_i][n]) == 1:
                        file.write(f'results[{n}] >= {sm_ratio} && ')
                    else:
                        file.write(f'results[{n}] <  {sm_ratio} && ')

                # последний
                elif n == 0:
                    if int(algorithms[sm_i][n]) == 1:
                        file.write(f'results[{n}] >= {sm_ratio}')
                    else:
                        file.write(f'results[{n}] <  {sm_ratio}')

                # основное
                else:
                    if int(algorithms[sm_i][n]) == 1:
                        file.write(f'results[{n}] >= {sm_ratio} && ')
                    else:
                        file.write(f'results[{n}] <  {sm_ratio} && ')

            file.write('){' + f'console.log("Make a bet {sm_i + 1} ↓ %cx{sm_ratio}", "color:DodgerBlue");makeBet();' + '}\n')


def local_make_scripts(algorithms, sm_ratio):

    # открытия файла с алгоритмами
    sm_file = open('cache/good_sequences.txt', 'r')

    results = []
    for line in sm_file:
        results.append(float(line[:-1]))

    # перебор всех алгоритмов
    for sm_i in range(0, len(algorithms)):

        print('if(', end='')
        length = len(algorithms[sm_i]) - 1
        for n in range(length, -1, -1):

            # первый
            if n == length:
                if int(algorithms[sm_i][n]) == 1:
                    print(f'results[{n}] >= {sm_ratio} && ', end='')
                else:
                    print(f'results[{n}] <  {sm_ratio} && ', end='')

            # последний
            elif n == 0:
                if int(algorithms[sm_i][n]) == 1:
                    print(f'results[{n}] >= {sm_ratio}', end='')
                else:
                    print(f'results[{n}] <  {sm_ratio}', end='')

            # основное
            else:
                if int(algorithms[sm_i][n]) == 1:
                    print(f'results[{n}] >= {sm_ratio} && ', end='')
                else:
                    print(f'results[{n}] <  {sm_ratio} && ', end='')

        print('){', end='')
        print(f'console.log("Make a bet {sm_i + 1} ↓ %cx{sm_ratio}", '
              f'"color:DodgerBlue");ChooseCoefficient ({sm_ratio});makeBet();', end='')
        print('}')


if __name__ == '__main__':

    sm_open_file = False

    if not sm_open_file:
        print('Преобразование алгоритмов')
        count = input('Сколько будет алгоритмов? ')
        count = int(count)
        ratio = input('Коэффициент: ')
        ratio = float(ratio)

        sm_good_algorithms = []
        for i in range(0, count):
            sm_good_algorithms.append(input(f'Введите алгоритм ({i + 1}): '))

        local_make_scripts(sm_good_algorithms, ratio)
        input('\nНажмите любую кнопку для выхода')

    else:
        ratio = input('Коэффициент: ')
        ratio = float(ratio)
        make_scripts(1.2)
        pass

else:
    sm_open_file = True

