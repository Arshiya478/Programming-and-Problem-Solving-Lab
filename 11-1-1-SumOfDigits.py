#Sum of Digits of a Number

num = int(input("Enter a number: "))

total = 0
num = abs(num)

while num > 0:
	digit = num % 10
	total += digit
	num //= 10

print("Sum of digits:", total)