from typing import List, Any

import numpy as np

# matrix math libary logic testing
# NOT THE COMPLETE APP
##misteak columns are acually rows will fix in final version

test_matrix_old = [[8, 4],
                   [5, 3]]

test_matrix2_old = [[4, 2],
                   [2, 3] ]
test_matrix = []

test_matrix2 = []  # type List[int]

if len(test_matrix2_old) > len(test_matrix_old):
    test_matrix2 = test_matrix_old
    test_matrix = test_matrix2_old


else:
    test_matrix = test_matrix_old
    test_matrix2 = test_matrix2_old
## to see the amount of numbers in each matrix
columns = len(test_matrix)
columns2 = len(test_matrix2)

print('numbers in columns (matrix 1) : {}'.format(columns))
print('numbers in columns (matrix 2) : {}'.format(columns2))

###########################################################################
num_of_row = len(test_matrix[0])

print(num_of_row)
##########################################################################
##
num_of_row2 = len(test_matrix2[0])

print(num_of_row2)

#######################################################################

rows2 = []
rows2_format = []
for i in range(len(test_matrix2[0])):
    for x in range(len(test_matrix2)):
        rows2.append(test_matrix2[x][i])

x = np.array(rows2)

y = np.array_split(x, len(test_matrix2[0]))

for i in range(len(test_matrix2[0])):
    rows2_format.append(y[i])
print('rows 2 : {}'.format(rows2_format))

############################################################################
##a list of everything in the all the columns of matrix 1

column_list = []
for i in range(len(test_matrix)):
    for x in range(len(test_matrix[0])):
        column_list.append(test_matrix[i][x])

##########################################################################

# a list of everything in the all the columns of matrix 2
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
    print('either failed')

if num_of_row * columns == num_of_row2 * columns2:

    x = largest
    y = largest
    split_value = num_of_row
elif num_of_row * columns != num_of_row2 * columns2:
    x = largest
    y = smallest
    split_value = num_of_row2
#
 #   list_of_multipyed_values = []

##the most efficent way to multiply the matrices out

def matrix_multipying_logic(x, y, smallest, largest, test_matrix, test_matrix2):
    list_of_multipyed_values = []
    for i in range(x):
        for ii in range(y):
            print(np.dot(np.array(test_matrix[i]), rows2_format[ii]))
            list_of_multipyed_values.append(np.dot(np.array(test_matrix[i]), rows2_format[ii]))

    print(list_of_multipyed_values)
    t = np.array(list_of_multipyed_values)
    # splits an arrat 9 is the expexted number of values

    finished = np.array_split(t, largest)

    finished_multiplyed = []
    ##finished_multiplyed = np.array_split(finished_multiplyed, 49)
    ##

    for i in finished:
        finished_multiplyed.append(i)

    finished_multiplyed = np.array(finished_multiplyed)

    print('''{}
    exit success multiply '''.format(finished_multiplyed))
    print(largest, smallest)

matrix_multipying_logic(x, y, smallest, largest, test_matrix, num_of_row)

def adding_logic(column_list, column_list2, test_matrix):
    added = []
    for i in range(len(column_list)):
        added.append(column_list[i] + column_list2[i])
    #added = np.array(added)
    added = np.array_split(added, num_of_row)
    added = np.array(added)
    print(added)

adding_logic(column_list, column_list2, num_of_row)