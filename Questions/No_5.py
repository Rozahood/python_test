def createList(r1, r3):
    return [item for item in range(r1, r3 + 1)]


myList = createList(1, 30)
# result = [item for item in myList if item % 3 == 0]
sum = 0
for i in range(1, 31):
    if i % 3 == 0:
        sum += 1
        print("The sum of integers between 1 and 30 that are divisible by 3 is:", sum)
