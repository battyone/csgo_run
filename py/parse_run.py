from urllib.request import urlopen, Request
from selenium import webdriver
from tqdm.auto import tqdm
import time


def get_the_latest_number_of_game():
    # initializing
    chrome_path = r"Selenium Web Driver\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)
    driver.set_window_size(1080, 1080)

    # parcing the latest game number
    driver.get(f'https://csgorun.org')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[2]/div[3]/a[1]').click()
    time.sleep(3)
    the_latest_number_of_game = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div/div[1]/div[1]/div/span[2]')
    the_latest_number_of_game = the_latest_number_of_game.get_attribute('innerHTML')
    the_latest_number_of_game = ''.join(c for c in the_latest_number_of_game if c.isdigit())
    the_latest_number_of_game = int(the_latest_number_of_game)

    # closing
    driver.close()
    return the_latest_number_of_game


def get_previous_number_of_game():
    try:
        with open('cache/ini.txt', 'r', encoding="utf-8") as file:
            # читаем только первую строку
            previous_number_of_game = file.readline() 
            previous_number_of_game = int(previous_number_of_game)
            return previous_number_of_game

    except:
        input("ERROR of getting the previous result")
        return


def parce_run():

    previous_number_of_game = get_previous_number_of_game()
    the_latest_number_of_game = get_the_latest_number_of_game()
    quantity = the_latest_number_of_game - previous_number_of_game - 1

    # главная часть работы - парсим все нужные значения
    print()
    for current_page in tqdm(range(previous_number_of_game + 1, the_latest_number_of_game), desc='Parsing', unit='bets'):
        reg_url = f"https://api.csgorun.org/games/{current_page}]/"
        req = Request(url=reg_url)
        html = str(urlopen(req).read()).split(',')[4]

        # записываем в файл
        with open('cache/results.txt', 'r', encoding="utf-8") as file:
            original_text = file.read()

        with open('cache/results.txt', 'w', encoding="utf-8") as file:
            file.write(html[8:] + '\n')
            file.write(original_text)

        # записываем в ini последнее значение, чтобы 
        # потом начинать парсить значения с него
        with open('cache/ini.txt', 'w', encoding="utf-8") as file:
            file.write(str(current_page))


if __name__ == '__main__':

    parce_run()
