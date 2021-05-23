from shared_functions import get_file_lines
from typing import Dict, List, Text


def is_operator(char: Text):
    return char in ["*", "/", "+", "-", "%"]


def are_operands(first_op: Text, second_op: Text):
    return first_op.isdigit() and second_op.isdigit()


def calc_sum(oper1, oper2):
    return oper1 + oper2


def calc_substract(oper1, oper2):
    return oper1 - oper2


def calc_multiply(oper1, oper2):
    return oper1 * oper2


def calc_divide(oper1, oper2):
    return oper1 / oper2


def calc_modulo(oper1, oper2):
    return oper1 % oper2


def dispatching(op: Text, oper1: Text, oper2: Text):
    operation_func = {
        '+': calc_sum,
        '-': calc_substract,
        '*': calc_multiply,
        '/': calc_divide,
        '%': calc_modulo,
    }
    return operation_func[op](int(oper1), int(oper2))


def calc_in_list(calc_list: List[Text]):
    """Calculate the 2 last elements in the list."""
    list_len = len(calc_list)
    calc_result = dispatching(calc_list[list_len - 2],
                              calc_list[list_len - 1],
                              calc_list[list_len - 3])
    calc_list.pop()
    calc_list.pop()
    calc_list[-1] = str(calc_result)
    return calc_list


def calc_remain_in_list(i: int, calc_list: List[Text]):
    """Calculate the remaining numbers in list starting from the beginning."""
    if is_operator(calc_list[i]) and are_operands(calc_list[i - 1],
                                                  calc_list[i + 1]):
        calc_result = dispatching(calc_list[i], calc_list[i - 1], calc_list[i + 1])
        calc_list.pop(i)
        calc_list.pop(i)
        calc_list.pop(i - 1)
        calc_list.insert(0, str(calc_result))
        i = 0
    else:
        i += 1
    return i, calc_list


def check_character(input_line: Text):
    calc_list = []
    ch = 0
    while ch < len(input_line):
        list_len = len(calc_list)
        if list_len > 2 and is_operator(
                calc_list[list_len - 2]) and are_operands(
                calc_list[list_len - 1], calc_list[list_len - 3]):
            calc_list = calc_in_list(calc_list)
        elif is_operator(input_line[ch]) and \
                are_operands(input_line[ch - 1], input_line[ch + 1]):
            calc_result = dispatching(input_line[ch], calc_list[-1], input_line[ch + 1])
            calc_list[-1] = str(calc_result)
            ch += 2
        elif input_line[ch] == ")":
            ch += 1
            i = list_len - 1
            while i != -1:
                if calc_list[i] == "(":
                    calc_list.pop(i)
                    break
                i -= 1
            i = 0
            while i <= len(calc_list) - 1 and calc_list[i] != "(":
                i, calc_list = calc_remain_in_list(i, calc_list)
        else:
            calc_list.append(input_line[ch])
            ch += 1
    i = 0
    while i < len(calc_list):
        i, calc_list = calc_remain_in_list(i, calc_list)
    calc_list.pop()
    return calc_list


input_lines = get_file_lines()
result = []
for i in range(len(input_lines)):
    # for i in range(35, 36):
    input_lines[i] = input_lines[i].replace(" ", "")
    # print("Expression : ", input_lines[i])
    result = result + check_character(input_lines[i])

res = list(map(int, result))
# print("List with all results : ", res)
answer = sum(res)
print("Final Answer : ", answer)

assert res[35] == 344916
assert res[26] == 97339344
assert res[3] == 220845112
assert res[13] == 18816
assert answer == 1451467526514
