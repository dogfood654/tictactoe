# find all possiblities and compare

'''
123
456
789

123
456
789
147
258
369
159
357
'''

x_arr = [1, 2, 4, 7]
in_a_row = [[1, 2, 3], [4, 5, 6], [7, 8, 9], 
            [1, 4, 7], [2, 5, 8], [3, 6, 9], 
            [1, 5, 9], [3, 5, 7]]
a = 0
answer = []

for pattern in in_a_row:
    a = 0
    for i in x_arr:
        if i in pattern:
            a += 1
    if a == 3:
        answer = pattern
        break

print(answer)
