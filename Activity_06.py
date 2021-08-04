numbers = input('enter 5 numbers ')
numbers_list = numbers.split(" ")
output1= numbers_list[0:3]
print(output1)
numbers_list[0]=0
numbers_list[4]=0
output2= numbers_list[0:6]
print(output2)
output3= numbers_list[0:3]
output3[0]=0
output3[2]=0
print(output3)
output4= numbers_list[::-1]
print(output4)
