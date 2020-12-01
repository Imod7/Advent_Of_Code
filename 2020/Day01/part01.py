
def open_file(file_name):
	input_file = open("input.txt", "r")
	file_lines = input_file.readlines()
	return file_lines 

def main(file_name):
	file_lines = open_file(file_name)
	expenses = []
	for lines in file_lines:
		expenses.append(int(lines))
	# print(len(expenses))
	for i in range(0, len(expenses)):
		for j in range(1, len(expenses)):
			if expenses[i] + expenses[j] == 2020:
				print("expenses [ ", expenses[i], ", ", expenses[j], " ] sum to -> ", expenses[i] + expenses[j])
				return expenses[i] * expenses[j]

if __name__ == "__main__":
	final_expenses = main("input.txt")
	print("Expense report = ", final_expenses)