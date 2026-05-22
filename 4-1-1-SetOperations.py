#Set Operations

setA_input = input("Set A: ")
setA = set(map(int, setA_input.split()))

setB_input = input("Set B: ")
setB = set(map(int, setB_input.split()))

union_set = setA | setB
intersection_set = setA & setB
difference_set = setA - setB

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)