numberList = {1, 2, 3, 4, 5, 6, 7}

my_iter = iter(numberList)
for number in numberList:
    print(next(my_iter))

print(50*"=")

my_iter2 = iter(numberList)
for number in range(0, len(numberList)):
    print(next(my_iter2))