def open_file(file_name):
	input_file = open("input.txt", "r")
	file_lines = input_file.readlines()
	return file_lines 

def main(file_name):
	file_lines = open_file(file_name)
	expenses = []
	for lines in file_lines:
		expenses.append(int(lines))
	for i in range(0, len(expenses)):
		for j in range(1, len(expenses)):
			for k in range(2, len(expenses)):
				if expenses[i] + expenses[j] + expenses[k] == 2020:
					print("expenses [ ", expenses[i], ", ", expenses[j],", ", expenses[k], " ] sum to -> ", expenses[i] + expenses[j] + expenses[k])
					return expenses[i] * expenses[j] * expenses[k]

if __name__ == "__main__":
	final_expenses = main("input.txt")
	print("Expense report = ", final_expenses)