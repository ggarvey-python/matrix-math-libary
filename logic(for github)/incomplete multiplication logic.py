import numpy as np

#matrix math libary logic testing
#NOT THE COMPLETE APP


test_matrix = [[3,2,3,6],
               [4,3,7,2],
               [3,4,2,7]]

test_matrix2 = [[7,3,2],
                [5,3,5],
                [6,2,6],
                [5,3,5]]


## to see the amount of numbers in each matrix
columns = len(test_matrix[0])
columns2 = len(test_matrix2[0])

print('numbers in columns (matrix 1) : {}'.format(columns))
print('numbers in columns (matrix 2) : {}'.format(columns2))


###########################################################################
# the amount of rows in eact matrix
num_of_row = []

for num in test_matrix[0]:
    num_of_row.append(num)
##this one deos the counting
num_of_row = len(num_of_row)
print('number of rows in matrix 1 : {}'.format(num_of_row))
##########################################################################

num_of_row2 = []

for num in test_matrix2[0]:
    num_of_row2.append(num)

num_of_row2 = len(num_of_row2)
print('number of rows in matrix 1 : {}'.format(num_of_row2))

#######################################################################
##rows is the rows in matrix1 placed out in a line for simplicity

rows = []

for i in range(len(test_matrix[0])):                                  
    for x in range(len(test_matrix)):
        


print(len(column_list))

        rows.append(test_matrix[x][i])
        
print('rows 1 : {}'.format(rows))



########################################################################
## rows2 is the rows in matrix2 placed out in a line for simplicity

rows2 = []

for i in range(len(test_matrix2[0])):                                  
    for x in range(len(test_matrix2)):
        
        rows2.append(test_matrix2[x][i])
        
print('rows 2 : {}'.format(rows2))

############################################################################
#a list of everything in the all the columns of matrix 1

column_list = []
for i in range(len(test_matrix)):
    for x in range(len(test_matrix[0])):
        column_list.append(test_matrix[i][x])

##########################################################################

#a list of everything in the all the columns of matrix 2
column_list2 = []
for i in range(len(test_matrix2)):
    for x in range(len(test_matrix2[0])):
        column_list2.append(test_matrix2[i][x])

        
print('columns 1 : {}'.format(column_list))
print('columns 2 : {}'.format(column_list2))

############################################################################
##now the mutiping,


##to see which matrix has longer columns for the multipycation wittjj rosws

if columns > columns2:
    largest = columns
elif columns < columns2:
    largest = columns2
elif columns == columns2:
    largest = columns
else:
    print('either failed or magic')


test_list = []

#39

##columns 
##columns2

#rows
#rows2


for i in range(len(column_list)):
    print(rows[i] * column_list2[i])





print(len(column_list))








