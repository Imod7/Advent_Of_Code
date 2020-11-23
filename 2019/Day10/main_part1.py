lines_infile = 0
with open("puzzle_input.txt", 'r') as f:
    input_line = f.readline().rstrip('\n')
    lst = []
    lst.append(input_line)
    chars_inline = len(input_line)
    while input_line:
        # print("Line {}: {}".format(lines_infile, input_line.strip()))
        input_line = f.readline().rstrip('\n')
        lst.append(input_line)
        lines_infile += 1

print("Number of Lines in file : ", lines_infile)
print("Chars in line : ", chars_inline)

raw_data = []
with open("puzzle_input.txt", 'r') as f:
  while True:
    c = f.read(1)
    if not c:
    #   print "End of file"
      break
    # print "Read a character:", c
    if c != '\n':
        raw_data.append(c)

print("Raw data : ", raw_data)

input_list = []
k = 0
for j in range(lines_infile):
    column = []
    for i in range(chars_inline):
        column.append(raw_data[k])
        k += 1
    input_list.append(column)

# print ('\n'.join(lst))
print("Input List")
print(input_list)

print("Input List Nicely Print")
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        print(input_list[i][j], end='')
    print()

def check_left(i, j, input_list):
    i += 1
    while i < lines_infile:
        while j < chars_inline:



print("Check")
result_list = {}
for i in range(lines_infile):
    column = []
    for j in range(chars_inline):
        if (input_list[i][j] == '#'):
            check_left(i, j, input_list)
            check_right(i, j, input_list)
        k += 1
    print()
    input_list.append(column)