input_list = []
with open ("input.txt") as myfile:
    for line in myfile:
        input_list = line.split(',')

input_list = list(map(int, input_list))

# EXAMPLE
# input_list = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

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

def addition(i, input_lst, param1, param2):
    # print("\n num = ",input_lst[i], "index : ", i, "addition", input_lst[i + 1], input_lst[i + 2], "to", getValue(input_lst, i + 3, 1))
    arg1 = getValue(input_lst, i + 1, param1)
    # print("arg1  :", arg1)
    arg2 = getValue(input_lst, i + 2, param2)
    # print("arg1 + arg2 = ", arg1, arg2)
    s = arg1 + arg2
    input_lst[getValue(input_lst, i + 3, 1)] = s

def multiplication(i, input_lst, param1, param2):
    # print(i, "multiplication", input_lst[i], param1, param2)
    # print("\nindex : ", i, " , num : ",input_lst[i],"multiplication", input_lst[i + 1], input_lst[i + 2], "to", getValue(input_lst, i + 3, 1))
    arg1 = getValue(input_lst, i + 1, param1)
    arg2 = getValue(input_lst, i + 2, param2)
    mult = arg1 * arg2
    input_lst[getValue(input_lst, i + 3, 1)] = mult

def store_to_address(i, input_lst, input_num):
    pos1 = input_lst[i + 1]
    input_lst[pos1] = input_num

def outputting(i, input_lst, param1):
    val = getValue(input_lst, i + 1, param1)
    print("outputting")
    print(val)

def jump_if_true(i, input_lst, param1, param2):
    # print("jump_if_true")
    # print("num1 = ", input_lst[i + 1], "num2 = ", input_lst[i + 2])
    arg1 = getValue(input_lst, i + 1, param1)
    arg2 = getValue(input_lst, i + 2, param2)
    # print("param1 = ", param1, "param2 = ", param2)
    # print("arg1 = ", arg1, "arg2 = ", arg2)
    if (arg1 != 0):
        i = arg2
    else:
        i = i + 3
    return i

def jump_if_false(i, input_lst, param1, param2):
    # print("jump_if_false")
    arg1 = getValue(input_lst, i + 1, param1)
    arg2 = getValue(input_lst, i + 2, param2)
    if (arg1 == 0):
        i = arg2
    else:
        i = i + 3
    return i

def less_than(i, input_lst, param1, param2):
    arg1 = getValue(input_lst, i + 1, param1)
    arg2 = getValue(input_lst, i + 2, param2)
    if (arg1 < arg2):
        input_lst[getValue(input_lst, i + 3, 1)] = 1
    else:
        input_lst[getValue(input_lst, i + 3, 1)] = 0

def equals(i, input_lst, param1, param2):
    arg1 = getValue(input_lst, i + 1, param1)
    arg2 = getValue(input_lst, i + 2, param2)
    if (arg1 == arg2):
        input_lst[getValue(input_lst, i + 3, 1)] = 1
    else:
        input_lst[getValue(input_lst, i + 3, 1)] = 0

def run_opcode(opcode, i, input, param1, param2):
    print("opcode = ", opcode)
    if (opcode == 1):
        addition(i, input, param1, param2)
        i = i + 4
        return (0, i)
    elif (opcode == 2):
        multiplication(i, input, param1, param2)
        i = i + 4
        return (0, i)
    elif (opcode == 3):
        store_to_address(i, input, input_num)
        i = i + 2
        return (0, i)
    elif (opcode == 4):
        outputting(i, input, param1)
        i = i + 2
        return (0, i)
    elif (opcode == 5):
        k = jump_if_true(i, input, param1, param2)
        # i = i + k
        return (0, k)
    elif (opcode == 6):
        k = jump_if_false(i, input, param1, param2)
        # i = i + k
        return (0, k)
    elif (opcode == 7):
        less_than(i, input, param1, param2)
        i = i + 4
        return (0, i)
    elif (opcode == 8):
        equals(i, input, param1, param2)
        i = i + 4
        return (0, i)
    elif (opcode == 99):
        return (99, 0)
    else:
        print("opcode ", opcode, " is not valid")

def check_opcode(num):
    opcode = 0
    parameter = 0
    param1 = 0
    param2 = 0
    num_str = str(num)
    opcode = int(num_str[-2:])
    parameter = num_str[:-2]
    # print("\nnum : ", num)
    # print("parameter : ", parameter)
    # print("len(parameter) : ", len(parameter))
    if (len(parameter) == 1):
        param1 = int(parameter[0])
    elif (len(parameter) == 2):
        param1 = int(parameter[1])
        param2 = int(parameter[0])
    # print("param1 : ", param1)
    # print("param2 : ", param2)
    return (opcode, parameter, param1, param2)

def run_program(input, input_num):
    i = 0
    while i < len(input):
        # print("\nInput num :", input[i], "Index :", i)
        opcode, parameter, param1, param2 = check_opcode(input[i]) 
        result, i = run_opcode(opcode, i, input, param1, param2)
        if (result == 99):
            break
        # print("Changed List")
        # print(input)
        # print("\n")

input = input_list.copy()
input_num = 5
run_program(input, input_num)


# print("Final List")
# print(input)