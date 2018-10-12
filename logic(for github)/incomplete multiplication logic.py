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
#this one deos the counting
num_of_row = len(num_of_row)
print('number of rows in matrix 1 : {}'.format(num_of_row))
########################################################################

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
        
        rows.append(test_matrix[x][i])
        
print('rows 1 : {}'.format(rows))



########################################################################
## rows2 is the rows in matrix2 placed out in a line for simplicity
##logic is a bit rough will fix later
rows2 = []
rows2_format = []
for i in range(len(test_matrix2[0])):                                  
    for x in range(len(test_matrix2)):
        
        rows2.append(test_matrix2[x][i])
        
x = np.array(rows2)

y = np.array_split(x, 3)

for i in range(len(test_matrix2[0])):
    rows2_format.append(y[i])
print('rows 2 : {}'.format(rows2_format))

############################################################################
#a list of everything in the all the columns of matrix 1

column_list = []
for i in range(len(test_matrix)):
    for x in range(len(test_matrix[0])):
        column_list.append(test_matrix[i][x])

##########################################################################

#a list of everything in the all the columns of matrix 2
column_list2 = []
test_list = []
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
    smallest = columns2
elif columns < columns2:
    largest = columns2
    smallest = columns
elif columns == columns2:
    largest = columns
    smallest = columns2
else:
    print('either failed or magic')

list_of_multipyed_values = []


for ii in range(3):
    for x in range(3):
        for i in range(4):
        
 
            list_of_multipyed_values.append(test_matrix[x][i] * rows2_format[ii][i])

t = np.array(list_of_multipyed_values)
finished = np.array_split(t, 9)

for i in range(9):
    print(sum(finished[i]))


