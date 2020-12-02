# https://adventofcode.com/2020/day/2
# --- Day 2: Password Philosophy ---

# after spending too much time to find a regex pattern to count the non 
# consecutive occurences (with a low and high bound) of a char in the string...
# I just used count and done in a minute

import re

def open_file(input_file):
	input_data = open(input_file, "r")
	input_lines = input_data.readlines()
	return input_lines

def build_regex(line_txt):
	min_times = int(line_txt[0].split('-')[0])
	max_times = int(line_txt[0].split('-')[1])
	occurences = int(line_txt[2].count(line_txt[1][0]))
	# print(occurences)
	if occurences >= min_times and occurences <= max_times:
		# print("val")
		return True
	else:
		# print("inval")
		return False
	# tried with regex in the commented code below but nope
	# min_times = line_txt[0].split('-')[0]
	# max_times = line_txt[0].split('-')[1]
	# occurences = line_txt[2].count(line_txt[1][0])
	# pattern = "." + line_txt[1][0] + "." + "{" + min_times + "," + max_times + "}"
	# print(pattern)
	# match_pattern = re.match(pattern, line_txt[2])
	# print(match_pattern)
	# if match_pattern:
	# 	print("val")
	# 	# return True
	# else:
	# 	print("inval")
	# 	# return False

def main(input_file):
	input_lines = open_file(input_file)
	valid_pwd = 0
	for line in input_lines:
		# list_text = [line_word.split(" ") for line_word in line]
		# print("\nline -> ", line, end ='')
		line_txt_parts = line.split()
		# print("splitted line -> ", line_txt_parts)
		res = build_regex(line_txt_parts)
		if res == True:
			valid_pwd += 1
	return valid_pwd

if __name__ == "__main__":
	valid_pwd_total = main("input.txt")
	print("Total valid passwords -> ", valid_pwd_total)