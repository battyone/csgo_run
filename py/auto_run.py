from parse_run import *
from checker_seq import *


def main():

    # парсим
    parce_run()

    # проверяем последовательности
    checker_results(21, 1.2, 91, False)

    # собираем в файл расширения и обновляем


if __name__ == '__main__':

    main()

    print('\n\n')
    input('Нажмите Enter для выхода')
