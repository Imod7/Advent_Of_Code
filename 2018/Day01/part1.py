# AoC 2018 - Day 1 - Part 1
# Subject can be found here : https://adventofcode.com/2018/day/1

def read_file_func() -> list:
	input_file = open("input.txt", "r")
	lines = input_file.readlines()
	# print(type(lines))
	return lines

def apply_frequencies() -> int:
	lines = read_file_func()
	result_freq = 0
	for line in lines:
		line.strip()
		# print()
		# print(line, end = "")
		result_freq += int(line)
		# print("Resulting Frequency -> ", result_freq)
	return result_freq

if __name__ == "__main__":
	result_freq = apply_frequencies()
	print("Resulting Frequency -> ", result_freq)