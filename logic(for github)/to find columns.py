test_matrix = [[3,2,6],
               [4,3,7],
               [3,4,2]]

test_matrix2 = [[7,3,2],
                [5,3,5],
                [6,2,6]]

##0,1,2,3,4,5,6,7,8

columns = 0

try:
    for i in range(100):
        test_matrix[i]
        columns += 1
except IndexError as e:
    print(columns)
else:
    print('too many columns please change the source')

finally:
    print('exit success!!!')
        