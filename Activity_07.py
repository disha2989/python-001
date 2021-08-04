numbers = input('enter 2 numbers ')
numbers_list = numbers.split(" ")
sum=0
for i in numbers_list:
    sum=sum+int(i)
print( numbers_list[0] +" + "+ numbers_list[1] +" = "+ str(sum) ) 
