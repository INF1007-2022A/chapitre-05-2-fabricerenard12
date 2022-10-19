#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	INDEX_NAME = 0
	INDEX_QUANTITY = 1
	INDEX_PRICE = 2
	sous_total = 0

	for i in data:
		sous_total += i[INDEX_QUANTITY] * i[INDEX_PRICE]

	taxes = (15 / 100) * sous_total
	total = sous_total + taxes

	facture = name + '\n'
	facture += 'SOUS TOTAL' + 5 * ' ' + f'{sous_total:.2f} $\n'
	facture += 'TAXES' + 11 * ' ' + f'{taxes:.2f} $\n'
	facture += 'TOTAL' + 10 * ' ' + f'{total:.2f} $'
	return facture


def format_number(number, num_decimal_digits):
	negative = False

	if number < 0:
		negative = True
		number = abs(number)

	decimal = str(round(number % 1, num_decimal_digits))
	number = int(number)
	res = ''
	parts = []

	while number:
		print(res)
		part = number % 1000
		parts.append(str(part))
		number //= 1000

	
	if negative:
		res += '-'

	parts.reverse()

	for i in range(0, len(parts)):
		res += parts[i]
		if i == (len(parts) - 1):
			break
		else:
			res += ' '
	
	res += f'{decimal[1:]}'

	return res
	
	


def get_triangle(num_rows):
	rows = ['A']
	string = ''

	for i in range(num_rows - 1):
		rows.append(rows[i] + 2 * 'A')

	n = len(rows) - 1
	string += '+' * (len(rows[n]) + 2) + '\n'

	for i in rows:
		spaces = (len(rows[n]) - len(i)) // 2
		string += '+' * 1 + ' ' * spaces + i + ' ' * spaces + '+' * 1 + '\n'
	
	string += '+' * (len(rows[n]) + 2)

	return string


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
