

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
            count += 1

print("Passwords Count :", count)