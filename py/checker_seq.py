import numpy as np
from tqdm.auto import tqdm
from ScriptMaker import make_scripts


def search_sequence_numpy(arr, seq):
    """ Find sequence in an array using NumPy only.
    https://stackoverflow.com/questions/36522220/searching-a-sequence-in-a-numpy-array

    Parameters
    ----------
    arr    : input 1D array
    seq    : input 1D array

    Output
    ------
    Output : 1D Array of indices in the input array that satisfy the
    matching of input sequence in the input array.
    In case of no match, an empty list is returned.
    """

    # Store sizes of input array and sequence
    Na, Nseq = arr.size, seq.size

    # Range of sequence
    r_seq = np.arange(Nseq)

    # Create a 2D array of sliding indices across the entire length of input array.
    # Match up with the input sequence & get the matching starting indices.
    M = (arr[np.arange(Na - Nseq + 1)[:, None] + r_seq] == seq).all(1)

    # Get the range of those indices as final output
    if M.any() > 0:
        return np.array(np.where(M)).ravel().tolist()
    else:
        return []  # No match found


def checker_results(len_of_seq, val, wins_ratio, progress_bar):
    # открываем файл с результатами
    with open('cache/results.txt', 'r', encoding="utf-8") as file:

        # заполняем массив результатами
        results = []
        for line in file:
            results.append(float(line[:-1]))

        # переходим к массиву numpy и удаляем
        # уже ненужный массив с результатами
        np_results = np.array(results)

        # переводим массив из чисел
        # в bool массив из True и False
        np_results = val <= np_results

        # создаем минимальный порог совпадений
        # равный 0,022% от общего числа результатов
        number_of_minimum_wins = round(len(np_results) / 100 * 0.022)

    # перебираем каждый возможный алгоритм на схожесть
    # с результатами и делаем предположительную ставку
    good_sequences = []

    # поиск всех совпадений последовательностей
    print()
    for a in tqdm(range(2 ** len_of_seq - 1, 0, -1), desc=f'Checking {len_of_seq}', unit='seq', disable=progress_bar):
        seq = bin(a)[2:].rjust(len_of_seq, '0')

        # пропускаем ненужные алгоритмы в которых
        #  присутствует более 5 проигрышей
        if seq.count('0') > 5:
            continue

        # sequence_TrueFalse алгоритмы преобразуем
        # в список для дальнейшего сравнивания с результатами
        seq_tf = list(seq)
        for one in range(0, len(seq_tf)):
            if seq_tf[one] == '1':
                seq_tf[one] = True
            else:
                seq_tf[one] = False
        seq_tf = np.array(seq_tf)

        # поиск алгоритмов в результатах и
        # предположительные ставки
        searched = search_sequence_numpy(np_results, seq_tf)
        if len(searched) > 0:

            wins = 0
            loses = 0

            # цикл для праверки ставок
            # берем индекс [-1] первого совпадения
            # если True, то wins += 1
            for b in range(0, len(searched)):

                # пропускаем нулевой элемент, т.к.
                # нулевой элемент -1 = ошибка
                if searched[0] == 0:
                    continue

                if np_results[searched[b] - 1]:
                    wins += 1
                else:
                    loses += 1

            # вывод результатов и сохранение в файл
            if wins >= number_of_minimum_wins:
                local_ratio = round((100 - loses / wins * 100), 1)
                if local_ratio >= wins_ratio:
                    good_sequences.append(seq)
                    if progress_bar:
                        print(f'{seq} {wins} | {loses} | {local_ratio}%')

    # записываем хорошие алгоритмы в файл
    # with open('cache/good_sequences.txt', 'w', encoding="utf-8") as file:
    #    for ch_i in range(0, len(good_sequences)):
    #        file.write(good_sequences[ch_i] + '\n')

    # записываем хорошие алгоритмы
    make_scripts(good_sequences, val)


if __name__ == '__main__':

    quest = input("Выбрать полные настройки? (1-да/ 2-нет) ")

    if int(quest) == 1:
        len_of_seq = input("Длинна алгоритмов ")
        len_of_seq = int(len_of_seq)

        koef = input("Ставка ")
        koef = float(koef)

        wins_ratio = input("Коэффициент побед (%) ")
        wins_ratio = int(wins_ratio)

        prog_bar = input("Выводить алгоритмы/показать прогресс бар (1/2) ")
        if int(prog_bar) == 1:
            prog_bar = True
        else:
            prog_bar = False

        print()
        checker_results(len_of_seq, koef, wins_ratio, prog_bar)
        input('\nНажмите Enter для выхода')

    # дефолтные настройки
    else:
        print()
        checker_results(21, 1.2, 90, False)
