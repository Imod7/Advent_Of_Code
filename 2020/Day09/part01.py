# Advent of Code 2020
# --- Day 9: Encoding Error ---
# https://adventofcode.com/2020/day/9

from typing import List


def get_data(file_name='input.txt') -> List[int]:
    """Function that opens and reads the input text file line by line.

    :param file_name: If no parameter is given it reads by default the input.txt file.
    :return: 1 lists of integers.
    """
    with open(file_name, "r") as input_file:
        xmas_input = []
        for line in input_file:
            line = int(line.rstrip())
            xmas_input.append(line)
    return xmas_input


def check(cur, preamble_lst):
    i = 0
    while i < len(preamble_lst):
        y = i + 1
        while y < len(preamble_lst):
            if cur == preamble_lst[i] + preamble_lst[y]:
                return 0
            y += 1
        i += 1
    return 1


def main(preamble_num) -> int:
    xmas_input = get_data()
    cur = preamble_num
    while cur < len(xmas_input):
        start = cur - preamble_num
        end = cur
        preamble_lst = xmas_input[start:end]
        preamble_lst.sort()
        # print("xmas_lst     : ", xmas_input[start:end])
        # print("preamble_lst : ", preamble_lst)
        # print("cur : ", cur)
        # print("start : ", start)
        # print("end : ", end)
        if xmas_input[cur] > preamble_lst[-1] + preamble_lst[-2]:
            return xmas_input[cur]
        else:
            res = check(xmas_input[cur], preamble_lst)
            if res == 1:
                return xmas_input[cur]
            cur += 1


if __name__ == "__main__":
    preamble = 25
    xmas_result = main(preamble)
    print("Part 01 result : ", xmas_result)
