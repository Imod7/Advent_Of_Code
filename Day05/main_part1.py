
input_list = []
with open ("input.txt") as myfile:
    for line in myfile:
        input_list = line.split(',')

input_list = list(map(int, input_list))
# print(input_list)

# 01101
# ABCDE
#
#    DE = instruction => 01 = addition
#   C = input1's mode
#  B = input2's mode

def getValue(memory, index, is_immediate):
    if (is_immediate == 1):
        # print("immediate value = ", memory[index])
        return (memory[index])
    else:
        # print("not immediate value = ", memory[index], index)
        return memory[memory[index]]

def addition(i, input_lst, par_pos1, par_im2):
    # print("\n num = ",input_lst[i], "index : ", i, "addition", input_lst[i + 1], input_lst[i + 2], "to", getValue(input_lst, i + 3, 1))
    arg1 = getValue(input_lst, i + 1, par_pos1)
    # print("arg1  :", arg1)
    arg2 = getValue(input_lst, i + 2, par_im2)
    # print("arg1 + arg2 = ", arg1, arg2)
    s = arg1 + arg2
    input_lst[getValue(input_lst, i + 3, 1)] = s

def multiplication(i, input_lst, par_pos1, par_im2):
    # print(i, "multiplication", input_lst[i], par_pos1, par_im2)
    # print("\nindex : ", i, " , num : ",input_lst[i],"multiplication", input_lst[i + 1], input_lst[i + 2], "to", getValue(input_lst, i + 3, 1))
    arg1 = getValue(input_lst, i + 1, par_pos1)
    arg2 = getValue(input_lst, i + 2, par_im2)
    mult = arg1 * arg2
    input_lst[getValue(input_lst, i + 3, 1)] = mult
    # print(input_lst)

def opcode_three(i, input_lst, input_num):
    # print("opcode three")
    pos1 = input_lst[i + 1]
    input_lst[pos1] = input_num
    # print("input set to ", input_num)
    # print(input_lst)

def opcode_four(i, input_lst, par_pos1):
    val = getValue(input_lst, i + 1, par_pos1)
    print("outputting")
    print(val)
    # print("index : ", i)
    # print(input_lst)

def check_opcode(num, digits_len):
    opcode = 0
    parameter = 0
    par_pos1 = 0
    par_im2 = 0
    num_str = str(num)
    opcode = int(num_str[-2:])
    parameter = num_str[:-2]
    # print("\nnum : ", num)
    # print("parameter : ", parameter)
    # print("len(parameter) : ", len(parameter))
    if (len(parameter) == 1):
        par_pos1 = int(parameter[0])
    elif (len(parameter) == 2):
        par_pos1 = int(parameter[1])
        par_im2 = int(parameter[0])
    # print("par_pos1 : ", par_pos1)
    # print("par_im2 : ", par_im2)
    return (opcode, parameter, par_pos1, par_im2)


def run_opcode(opcode, i, input, par_pos1, par_im2):
    if (opcode == 1):
        addition(i, input, par_pos1, par_im2)
        i = i + 4
        return (0, i)
    elif (opcode == 2):
        multiplication(i, input, par_pos1, par_im2)
        i = i + 4
        return (0, i)
    elif (opcode == 3):
        opcode_three(i, input, input_num)
        i = i + 2
        return (0, i)
    elif (opcode == 4):
        opcode_four(i, input, par_pos1)
        i = i + 2
        return (0, i)
    elif (opcode == 99):
        return (99, 0)
    else:
        print("opcode ", opcode, " is not valid")
            
def calculation(input, input_num):
    i = 0
    while i < len(input):
        digits_len = len(str(input[i]))
        # print("\nInput num :", input[i])
        # print("Digits Len :", digits_len)
        # print("Index :", i)
        opcode, parameter, par_pos1, par_im2 = check_opcode(input[i], digits_len) 
        result, i = run_opcode(opcode, i, input, par_pos1, par_im2)
        if (result == 99):
            break
        # print("Changed List")
        # print(input)
        # print("\n")


input = input_list.copy()
# print("Original Input")
# print(input)
input_num = 1
calculation(input, input_num)

# num_str = "123"
# parameter = num_str[:-2]
# print("parameter : ", parameter)
# print("len(parameter) : ", len(parameter))
# opcode = num_str[-2:]
# print("opcode : ", opcode)

# print("Final List")
# print(input)