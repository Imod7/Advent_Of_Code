# AoC 2018 - Day 1 - Part 2
# Subject can be found here : https://adventofcode.com/2018/day/1

from typing import Union

def read_file_func() -> list:
	input_file = open("input.txt", "r")
	lines = input_file.readlines()
	# print(type(lines))
	return lines

def track_freq_changes(result_freq: int, track_freq: dict) -> Union[dict, int]:
	exit_prgm = 0
	# print("result freq = ", result_freq)
	# print("dict : ", track_freq)
	if result_freq not in track_freq:
		# print("not in list")
		track_freq[result_freq] = 1
	else:
		# print("IN list")
		track_freq[result_freq] += 1
		exit_prgm = 1
		return track_freq, exit_prgm
	return track_freq, exit_prgm

def apply_frequencies(result_freq: int, track_freq: dict) -> Union[int, dict]:
	lines = read_file_func()
	# result_freq = 0
	# my_freq_list = []
	for line in lines:
		line = line.strip()
		# print(line, end = " ")
		result_freq += int(line)
		# my_freq_list.append(result_freq)
		track_freq, exit_prgm = track_freq_changes(result_freq, track_freq)
		# print("intern of ROUND -> ", result_freq)
		if exit_prgm == 1:
			return result_freq, track_freq, exit_prgm
	# print("FINAL of ROUND -> ", result_freq)
	return result_freq, track_freq, exit_prgm

if __name__ == "__main__":
	exit_prgm = 0
	round = 1
	track_freq = {}
	print("Round ", round)
	result_freq, track_freq, exit_prgm = apply_frequencies(0, track_freq)
	print("Resulting Frequency -> ", result_freq)
	# result_freq = 138 * 543
	while exit_prgm == 0:
		round += 1
		print("Round ", round)
		result_freq, track_freq, exit_prgm = apply_frequencies(result_freq, track_freq)
		# print("dict out ", track_freq)
		print("Resulting Frequency -> ", result_freq)
	print("\nSolution -> ", result_freq)
	