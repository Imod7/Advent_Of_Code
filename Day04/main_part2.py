

def check_adjacent(num):
    i_str = str(num)
    i = 0
    # print("length")
    # print(len(i_str))
    while (i < (len(i_str) - 1)):
        if (i_str[i] == i_str[i + 1]):
            return (1)
        i += 1
    return (0)

def check_adjacent_bytwo(num, digit):
    i_str = str(num)
    i = 0
    flag = 0
    # print("length")
    # print(len(i_str))
    while (i < (len(i_str) - 2)):
        if ((i_str[i] == i_str[i + 1]) and (i_str[i + 1] != i_str[i + 2]) and (i_str[i] != digit)):
            return (1)
        if ((i_str[len(i_str) - 1] == i_str[len(i_str) - 2]) and (i_str[len(i_str) - 1] != i_str[len(i_str) - 3]) and (i_str[len(i_str) - 1] != digit)):
            return (1)
        i += 1
    return (0)

def check_adjacent_bythree(num):
    i_str = str(num)
    i = 0
    # print("length")
    # print(len(i_str))
    while (i < (len(i_str) - 2)):
        if ((i_str[i] == i_str[i + 1]) and (i_str[i + 1] == i_str[i + 2])):
            if (check_adjacent_bytwo(num, i_str[i]) == 0):
                return (0)
        i += 1
    return (1)

def check_increase(num):
    i_str = str(num)
    i = 0
    # print("length")
    # print(len(i_str))
    while (i < (len(i_str) - 1)):
        if (int(i_str[i]) > int(i_str[i + 1])):
            return (0)
        i += 1
    return (1)

count = 0
for num in range(125730, 579381):
    if (check_adjacent(num) == 1):
        if (check_increase(num) == 1):
            if (check_adjacent_bythree(num) == 1):
                count += 1
                print(num)

print("Passwords Count :", count)