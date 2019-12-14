


def file_number_of_lines(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1

file_lines = file_number_of_lines("file.txt")
print("Number of lines in the file: ",file_number_of_lines("file.txt"))

def part2_fuel(num):
        sum_results = 0
        while (num >= 0):
                print(num)
                num = int(num / 3)
                num = num - 2
                if (num >= 0):
                        sum_results = sum_results + num
                print("Current Sum")
                print(sum_results)
        return (sum_results)
                

sum_results = 0
with open("file.txt", "r") as f:
    list_original = []
    list_ints = []
    line = f.readline()
    while line:
        line = line.strip('\n')
        num = int(line)
        result = part2_fuel(num)
        list_original.append(line)
        list_ints.append(result)
        line = f.readline()

# final_part1 = sum(list_ints)

# sum = 0
# for x in list_ints:
#         sum += x

final_part2 = sum(list_ints)

# print("Original List")
# print(list_original)
print("List with Results")
print(list_ints)
print(len(list_ints))
# print("Sum")
# print(final_part1)
# print("Sum of ints")
# print(sum)

print("Part2 Sum ")
print(final_part2)
