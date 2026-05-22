#Largest of Three Numbers

a = int(input())
b = int(input())
c = int(input())

if(a >= b) & (a >= c):
	largest = a
elif(b >= a) & (b >= c):
	largest = b
else:
	largest = c

print(f"{largest}")