#Multiplication of Two Square Matrices

print("dimension: ", end="")
n = int(input())

print("first matrix:")
A = []
for _ in range(n):
	row = list(map(int, input().split()))
	A.append(row)

print("second matrix:")
B = []
for _ in range(n):
	row = list(map(int, input().split()))
	B.append(row)

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
	for j in range(n):
		for k in range(n):
			result[i][j] += A[i][k] * B[k][j]

print("Resultant Matrix:")
for row in result:
	print(*row)