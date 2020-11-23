
def read_file() -> list:
	input_file = open("input.txt", "r")
	lines = input_file.readlines()
	return lines

# Function where we count how many times each character in the string 
# appears and we populate the corresponding dictionary
def count_chars_in_lines() -> list:
	lines = read_file()
	count_chars = {}
	count = 0
	for line in lines:
		count += 1
		print("\nLine ", count, " : ", line, end = "")
		for ch in line:
			if ch not in count_chars:
				count_chars[ch] = 1
			else:
				count_chars[ch] += 1
		print(count_chars)
		count_chars = {}
	return count_chars

def find_occurences():
	count_chars = count_chars_in_lines()
	result_dict = {"2_occur":0, "3_occur": 0}
	if 2 in char_found.values():
		result_dict["2_occur"] += 1
	if 3 in char_found.values():
		result_dict["3_occur"] += 1
	return (result_dict["2_occur"] * result_dict["3_occur"])

if __name__ == "__main__":
	checksum = find_occurences()
	print(checksum)