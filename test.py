# encoding: utf-8

import math
import csv


def math_ceil():
	''' 向上取整 '''
	a = math.ceil(670/30)
	print(a)

def test_csv():
	datas = [
		['a', 'b', 'c'],
		['e', 'f', 'g'],
	]

	with open('test.csv', 'w', encoding='utf-8', newline='') as csvfile:
		writer = csv.writer(csvfile)
		for row in datas:
			writer.writerow(row)


if __name__ == "__main__":
	# math_ceil()
	test_csv()
