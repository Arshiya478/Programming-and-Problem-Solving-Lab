#Incremented Date

day = int(input())
month = int(input())
year = int(input())

if year <= 0:
	print("Invalid Date")

# Validate month
elif month < 1 or month > 12:
	print("Invalid Date")

else:
	days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	if year % 400 == 0:
		days[2] = 29
	elif year % 4 == 0 and year % 100 != 0:
		days[2] = 29
	else:
		days[2] = 28

	if day < 1 or day > days[month]:
		print("Invalid Date")
	else:
		day += 1

		if day > days[month]:
			day = 1
			month += 1

		if month > 12:
			month = 1
			year += 1

		print(f"{day:02d}-{month:02d}-{year}")