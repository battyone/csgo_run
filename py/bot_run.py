import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# initializing
chrome_path = r"Selenium Web Driver\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
driver.set_window_size(1080, 1080)

result1_old = float(0)
result2_old = float(0)
bets_in_row = 4
able_to_bet = 2
exchange = 0.25
balance = 0

bet_at_last_round = False

# telegram


def auth_run():
    # go to CSGORUN
    driver.get(f'https://csgorun.org')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="auto-upgrade-input"]').send_keys(u'\ue009' + u'\ue003') #clear
    driver.find_element_by_xpath('//*[@id="auto-upgrade-input"]').send_keys("1.2")

    # go to Steam
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/header/div[2]/button').click()
    time.sleep(3)

    # auth
    driver.find_element_by_xpath('//*[@id="steamAccountName"]').send_keys("mim432")
    driver.find_element_by_xpath('//*[@id="steamPassword"]').send_keys("popusi8833")
    driver.find_element_by_xpath('//*[@id="imageLogin"]').click()
    input('\nPress Enter after authentication')
    print('Continued...')
    time.sleep(5)

    # turn off sounds
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/header/div[1]/button').click()

    # hide chat
    #driver.find_element_by_xpath('//*[@id="root"]/div[2]/div/div[1]/button[2]').click()


def update():
    
    try:
        global result1_old, result2_old, bet_at_last_round, bets_in_row, able_to_bet

        result1 = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/a[1]/span')
        result1 = float(result1.get_attribute('innerHTML')[:-1])
        result2 = driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[3]/a[2]/span')
        result2 = float(result2.get_attribute('innerHTML')[:-1])

        if not result1 == result1_old and not result2 == result2_old:

            # save old results
            result1_old = result1
            result2_old = result2

            if bet_at_last_round:
                bet_at_last_round = False
                if result1 <= 1.2:
                    able_to_bet = 0
                    exchange()

            # update able_to_bet until 2
            if result1 <= 1.2 and result2 <= 1.2:
                ble_to_bet = 2

	    # reload
            if bets_in_row == 0:
                exchange()
                bets_in_row = 4

            # make a bet
            if result1 <= 1.2 and result2 >= 1.2:
                if able_to_bet == 0:
                    print('Round skipped')
			        
            else:

                # попытки
                if able_to_bet != 0:
                    print('Bet!')
                    make_bet()
                    bet_at_last_round = True
                    able_to_bet = able_to_bet - 1
                    bets_in_row = bets_in_row - 1

            print(f'{result1} {result2}')

    except Exception as E:
        print('Unable take results')
        print(E)

    


def make_bet():
    try:
        time.sleep(7)
	# choose all in
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div[1]/label/div').click()
	    
	# choose x1.2
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/button[2]').click()

	# press start
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/button').click()

    except Exception as E:
        print('Unable make a bet')
        print(E)


def get_balance():
    global balance
    balance = driver.find_element_by_xpath('//*[@id="root"]/div[1]/header/div[2]/div/a[2]')
    balance = balance.get_attribute('innerHTML')[:-2]
    print(balance)


def win_or_lose():
    pass

    

def exchange():
    # choose all in
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div[1]/label/div').click()
    # open exchange
    driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div[3]/button[1]').click()
    time.sleep(1)
    # enter value
    driver.find_element_by_xpath('//*[@id="exchange-filter-maxPrice-field"]').send_keys(u'\ue009' + u'\ue003') #clear
    driver.find_element_by_xpath('//*[@id="exchange-filter-maxPrice-field"]').send_keys(f"{exchange}")
    time.sleep(1)
    # choose the first element
    driver.find_element_by_xpath('//*[@id="modal-portal"]/div[2]/div[2]/div/div[3]/div[1]/div/button[1]').click()
    time.sleep(1)
    # accept
    driver.find_element_by_xpath('//*[@id="modal-portal"]/div[2]/div[2]/div/div[2]/div[1]/button').click()
    # close
    driver.find_element_by_xpath('//*[@id="modal-portal"]/div[2]/div[2]/div/div[1]/button').click()



if __name__ == '__main__':

    auth_run()
    while True:
        update()
        time.sleep(2)

    driver.close()
