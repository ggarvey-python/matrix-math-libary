import numpy as np

#matrix math libary logic testing
#NOT THE COMPLETE APP


test_matrix = [[8,4,2,2,7],
               [6,2,5,7,3],
               [4,3,7,2,8],
               [5,2,8,2,9],
               [2,7,4,6,5],
               [2,9,4,7,5],
               [7,3,6,2,0]]

test_matrix2 = [[4,2,5,3,8,3,7],
                [2,3,6,3,5,8,3],
                [9,1,4,2,8,5,8],
                [6,3,3,7,3,7,4],
                [1,7,4,6,2,7,9]]


## to see the amount of numbers in each matrix
columns = len(test_matrix[0])
columns2 = len(test_matrix2[0])

print('numbers in columns (matrix 1) : {}'.format(columns))
print('numbers in columns (matrix 2) : {}'.format(columns2))


###########################################################################

##########################################################################
##
num_of_row2 = []

for num in test_matrix2[0]:
    num_of_row2.append(num)

num_of_row2 = len(num_of_row2)
print('number of rows in matrix 1 : {}'.format(num_of_row2))

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
    print('either failed')

list_of_multipyed_values = []

##the most efficent way to multiply the matrices out


for i in range(largest):
    for ii in range(largest):
        list_of_multipyed_values.append(np.dot(np.array(test_matrix[i]), rows2_format[ii]))

print(list_of_multipyed_values)
t = np.array(list_of_multipyed_values)
#splits an arrat 9 is the expexted number of values


finished = np.array_split(t, num_of_row2)


#i in range of expected number of values at the end
##finished_multiplyed = []
##for i in range(smallest*2):
##    finished_multiplyed.append(sum(finished[i]))
##
##    
finished_multiplyed = []
##finished_multiplyed = np.array_split(finished_multiplyed, 49)
##

for i in finished:
    finished_multiplyed.append(i)

    
finished_multiplyed = np.array(finished_multiplyed)

print('''{}
exit success '''.format(finished_multiplyed))

####################################################################################
