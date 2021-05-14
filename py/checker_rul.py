import numpy as np
from tqdm.auto import tqdm

# global
results = []
np_results = []

# система счисления для последовательностей
BASE = 3
LENGTH_OF_RULES = 4


def generator(a=0):
    while True:
        number = convert_base(a, BASE, 10).rjust(LENGTH_OF_RULES, '0')

        # адаптация к реальным условиям: пример, перевод [2] в [2, 1, 0]
        help_list = []
        for b in range(LENGTH_OF_RULES - 1, 0, -1):

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

        yield np.array(help_list)
        a += 1


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


def get_number_of_bets(arr, pos_of_seq):

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


def main(progress_bar=True):

    global LENGTH_OF_RULES

    g = generator()
    for __ in tqdm(range(BASE ** LENGTH_OF_RULES - 1, 1, -1), desc=f'Checking {LENGTH_OF_RULES}', unit='seq', disable=progress_bar):


        seq = next(g)
        print(seq)
        searched = search_sequence_numpy(np_results, seq)
        if len(searched) > 0:

            min = 0
            max = 0

            print(searched, end='')
            for b in range(0, len(searched)):
                # пропускаем нулевой элемент, т.к.
                # нулевой элемент -1 = ошибка
                if searched[0] == 0:
                    number = get_number_of_bets(np_results, searched[b])
                    min = number
                    max = number
                    continue

                number = get_number_of_bets(np_results, searched[b])
                if number > max:
                    max = number

                if number < min:
                    min = number

                print(f' max = {max} min = {min}')





if __name__ == '__main__':
    open_and_convert_results()
    main()



























