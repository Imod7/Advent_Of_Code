from shared_functions import get_file_lines
from typing import Dict, List, Text

input_lines = get_file_lines()


def prepare_mask(input_lines: Text, i: int):
    mask = input_lines[i][7:]
    mask = mask.strip()
    mask_lst = [char for char in mask]
    return mask_lst


def prepare_memory_value(input_lines: Text, i: int):
    mem = input_lines[i].split("= ", 1)
    mem = mem[1].strip()
    bin_mem = bin(int(mem))
    bin_mem = bin_mem.split('0b')[1]
    zeros_pad_len = 36 - len(bin_mem)
    y = 0
    num_lst = []
    while y < zeros_pad_len:
        num_lst.append('0')
        y += 1
    y = 0
    while y < len(bin_mem):
        num_lst.append(bin_mem[y])
        y += 1
    return num_lst


def apply_mask(mask_lst, num_lst):
    result_lst = []
    i = 0
    while i < len(mask_lst):
        if mask_lst[i] == 'X':
            result_lst.append(num_lst[i])
        else:
            result_lst.append(mask_lst[i])
        i += 1
    return result_lst


def calculate_new_value(result_lst):
    new_str = ""
    for x in result_lst:
        new_str += x
    new_val = int(new_str, 2)
    return new_val


i = 0
memory_dict = {}
while i < len(input_lines):
    if input_lines[i][0:4] == "mask":
        mask_lst = prepare_mask(input_lines, i)
    if input_lines[i][0:3] == "mem":
        mem = input_lines[i].split("] = ", 1)
        mem = mem[0].split("[", 1)
        mem = mem[1].strip()
        num_lst = prepare_memory_value(input_lines, i)
        result_lst = apply_mask(mask_lst, num_lst)
        new_val = calculate_new_value(result_lst)
        memory_dict[mem] = new_val
        # print("\nLINE : ", input_lines[i])
        # print("Memory address : ", mem)
        # print("mask_lst : ", mask_lst)
        # print("num_lst  : ", num_lst)
        # print("res_lst  : ", result_lst)
        # print("new num  : ", new_val)
    i += 1


answer = sum(memory_dict.values())
print("Final Answer : ", answer)

assert answer == 15403588588538