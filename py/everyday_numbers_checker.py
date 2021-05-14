import json
import time
import schedule
from os import sys
from datetime import datetime
from parse_run import get_the_latest_number_of_game


def write_json(data):
	with open('cache/everyday_numbers.txt', 'w', encoding="utf-8") as f:
		json.dump(data, f, ident=4)


def working():

	# парсим последний номер
	the_latest_number_of_game = get_the_latest_number_of_game()

	# устанавливаем время
	###############          Добавить в json файл инфу, а не к файлу
	############### https://www.youtube.com/watch?v=QrRcZmDaO_I
	# now = datetime.now()
	# record = {f'{now.day}-{now.month}-{now.year}' : f'{the_latest_number_of_game}'}

	# записываем номер со временем
	# j = json.dumps(record)

	with open('cache/everyday_numbers.txt', encoding="utf-8") as json_file:
		data = json.load(json_file)
		temp = data["dates"]

		now = datetime.now()
		y = {f'{now.day}-{now.month}-{now.year}' : f'{the_latest_number_of_game}'}
		temp.append(y)
		

	# закрываем программу
	sys.exit(0)


working()
# schedule.every().day.at("02:04").do(working)

# while True:
	# schedule.run_pending()
	# time.sleep(10)







