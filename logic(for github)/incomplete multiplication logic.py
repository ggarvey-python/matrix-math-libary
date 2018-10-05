import numpy as np

test_matrix = [[3,2,3,6],
               [4,3,7,2],
               [3,4,2,7]]

test_matrix2 = [[7,3,2],
                [5,3,5],
                [6,2,6],
                [5,3,5]]

##0,1,2,3,4,5,6,7,8

columns2 = 0

try:
    for i in range(100):
        test_matrix[i]
        columns2 += 1
except IndexError as e:
    #print('columns')
    pass
else:
    #print('too many columns please change the source')
    pass

finally:
    print('exit success!!!')
    pass

#non = number of nubers

    
    
rows2 = []


number_range2 = []
##
for i in range(len(test_matrix2[0])):
    number_range2.append(i)
    
for i in range(len(number_range2)):
    for x in range(len(test_matrix2)):
        
        rows2.append(test_matrix2[x][i])
        


columns = 0

try:
    for i in range(100):
        test_matrix[i]
        columns += 1
except IndexError as e:
    #print('columns')
    pass
else:
    #print('too many columns please change the source')
    pass

finally:
    print('exit success!!')
    pass

#non = number of nubers

    
    
rows = []

try:
    non = 0
    for i in range(100):
        test_matrix[i][non]
        non+=1
except:
    pass
    #print(non)
for num in test_matrix[0]:
    pass

number_range = []
##
for i in range(len(test_matrix[0])):
    number_range.append(i)
    
for i in range(len(number_range)):
    for x in range(len(test_matrix)):
        
        rows.append(test_matrix[x][i])
##        
##print(rows)
##print(rows2)

num_of_col = len(test_matrix)
num_of_col2 = len(test_matrix2)

num_of_row = []
num_of_row2 = []

##print(len(rows))
#print(len(test_matrix2[0]))

column_list = []
for i in range(len(test_matrix)):
    for x in range(len(test_matrix[0])):
        #pass
        column_list.append(test_matrix[i][x])


column_list2 = []
for i in range(len(test_matrix2)):
    for x in range(len(test_matrix2[0])):
        #pass
        column_list2.append(test_matrix2[i][x])
print(column_list)
print(column_list2)
