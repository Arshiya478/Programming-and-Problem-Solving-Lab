#Count Vowels in a String-1

text = input()
vowels = "aeiouAEIOU"

count = 0
for char in text:
	if char in vowels:
		count += 1

print(count)
