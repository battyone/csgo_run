import json

data = """
{
	"dates": [

	]	
}"""	


# создаем папку everyday_numbers.txt
try:
	with open('cache/everyday_numbers.txt', 'r', encoding="utf-8") as f:
		pass
except Exception as e:
	with open('cache/everyday_numbers.txt', 'w', encoding="utf-8") as f:
		f.write(data)





























