# 2. Have the user define how many in a row you need to win - checking for 3 in a row on a 5x5 is very different than checking for 5
# in a row on 5x5.

user_prompt = 3

'''
1,2,3,4,5,6,7,8,9

123
456
789

horizontal
123
456
789

vertical
147 (%3 = 1)
258 (%3 = 2)
369 (%3 = 0)

diagonal
159 (+3+1)
357 (+3-1)

put into more dictionaries

if N/A or other player's piece
    n = 0
else own piece
    n += 1

'''

d = {   "string1": " ", "string2": " ", "string3": " ",
        "string4": " ", "string5": " ", "string6": " ",
        "string7": " ", "string8": " ", "string9": " "}

in_a_row = 0

# check horizontal
'''
for i in range(1,10):
    if i % 3 == 1:
        in_a_row = 0
    if d["string{0}".format(i)] == "X":
        in_a_row += 1
    else:
        in_a_row = 0
    if i % 3 == 0:
        if in_a_row == 3:
            break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''

# check vertical
'''
for i in range(1,4):
    in_a_row = 0
    y = i
    for x in range(0,3):
        z = y + (x * 3)
        if d["string{0}".format(z)] == "X":
            in_a_row += 1
        else:
            in_a_row = 0
        if x == 2:
            if in_a_row == 3:
                break
    if in_a_row == 3:
        break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''

# check diagonal 1
'''
for i in range(1,4):
    in_a_row = 0
    y = i
    for x in range(0,3):
        z = y + x * (3 + 1)
        if d["string{0}".format(z)] == "X":
            in_a_row += 1
        else:
            in_a_row = 0
        if x == 2:
            if in_a_row == 3:
                break
        if z % 3 == 0:
            break
    if in_a_row == 3:
        break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''

# check diagonal 2
'''
list = []
number = 3
for i in range(1, number*number, 3):
    list.append(i)

for i in range(0,3):
    in_a_row = 0
    y = list[i]
    for x in range(0,3):
        z = y + x * (3 + 1)
        if d["string{0}".format(z)] == "X":
            in_a_row += 1
        else:
            in_a_row = 0
        if x == 2:
            if in_a_row == 3:
                break
        if z >= 7:
            break
    if in_a_row == 3:
        break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''

# check diagonal 3
'''
for i in range(1,4):
    in_a_row = 0
    y = i
    for x in range(0,3):
        z = y + x * (2)
        if d["string{0}".format(z)] == "X":
            in_a_row += 1
        else:
            in_a_row = 0
        if x == 2:
            if in_a_row == 3:
                break
        if z in list:
            break
    if in_a_row == 3:
        break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''

# check diagonal 4
'''
list2 = []
number = 3
for i in range(number, number*number+1, 3):
    list2.append(i)
print(list2)

for i in range(0,3):
    in_a_row = 0
    y = list2[i]
    for x in range(0,3):
        z = y + x * (2)
        print(z)
        if d["string{0}".format(z)] == "X":
            in_a_row += 1
        else:
            in_a_row = 0
        if x == 2:
            if in_a_row == 3:
                break
        if z >= 7:
            break
    if in_a_row == 3:
        break

if in_a_row == 3:
    print("win")
else:
    print("lose")
'''
