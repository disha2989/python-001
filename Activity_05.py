numbers = input('enter 5 numbers ')
numbers_list = numbers.split(" ")
sum = 0
for i in numbers_list:
    sum = sum + int(i)
print(sum)
