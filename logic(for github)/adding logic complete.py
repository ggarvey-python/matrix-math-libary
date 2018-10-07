##THIS IS AN OLD FILE AND IS LIKLY TO BE DEPRECATED
##

import numpy as np
import math

test_matrix = [[3,2,6],
               [4,3,7],
               [3,4,2]]

test_matrix2 = [[7,3,2],
                [5,3,5],
                [6,2,6]]

if test_matrix[1][2]:
    print('okay!!')

try:
    if not test_matrix[1][4]:
        print('YOU FAILED AT PROGRAMMING GO BACK TO THE BASICS YOU SUCK!!!!!')

except IndexError as e:
    print('My program accually has some potential')

new_matrix = []


#stores the added matrix values
number_list = []
number_list2 = []
number_matrix = []

l1 = []
l2 = []
l3 = []

matrix = []

for List in test_matrix:
    for num in List:
        number_list.append(num)


for List2 in test_matrix2:
    for num2 in List2:
        number_list2.append(num2)

for i in range(len(number_list)):
    x = number_list[i]+number_list2[i]
    number_matrix.append(x)
    

l1.append(number_matrix[0])
l1.append(number_matrix[1])
l1.append(number_matrix[2])

l2.append(number_matrix[3])
l2.append(number_matrix[4])
l2.append(number_matrix[5])

l3.append(number_matrix[6])
l3.append(number_matrix[7])
l3.append(number_matrix[8])

matrix = [l1,l2,l3]



print(number_matrix)
print(l1, l2, l3)
print(matrix)
    
    





               
#print(new_matrix)
