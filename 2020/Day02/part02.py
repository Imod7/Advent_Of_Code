# https://adventofcode.com/2020/day/2
# --- Day 2: Password Philosophy --- Part Two --- ---

# regex and XOR save the day :)

import re

def open_file(input_file):
	input_data = open(input_file, "r")
	input_lines = input_data.readlines()
	return input_lines

def build_regex(line_txt, num):
	pos = int(line_txt[0].split('-')[num]) - 1
	pattern = "^.{" + str(pos) + "}" + line_txt[1][0] + ""
	match_res = re.match(pattern, line_txt[2])
	return match_res
	

def xor_regex(line_txt):
	first_match = build_regex(line_txt, 0)
	second_match = build_regex(line_txt, 1)
	if bool(first_match) ^ bool(second_match):
		return True
	else:
		return False

def main(input_file):
	input_lines = open_file(input_file)
	valid_pwd = 0
	for line in input_lines:
		# print("\nline -> ", line, end ='')
		line_txt_parts = line.split()
		# print("splitted line -> ", line_txt_parts)
		res = xor_regex(line_txt_parts)
		if res == True:
			valid_pwd += 1
	return valid_pwd

if __name__ == "__main__":
	valid_pwd_total = main("input.txt")
	print("Total valid passwords -> ", valid_pwd_total)