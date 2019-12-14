
input_list = []
with open("puzzle_input.txt") as f:
  while True:
    c = f.read(1)
    if not c:
    #   print "End of file"
      break
    input_list.append(c)

# print(input_list)

layer_list = []
for j in range(6):
    column = []
    for i in range(25):
        column.append('2')
    layer_list.append(column)


print("initial layer list")
print(layer_list)

def print_final_layer(layer_list):
    for i in range(6):
        for j in range(25):
            print("#" if layer_list[i][j] == "1" else " ", end = '')
        print()


k = 0
for _ in range(len(input_list) // (6 * 25)):
    for i in range(6):
        for j in range(25):
            # print("k")
            # print(k)
            print(j, i, k)
            # if k == len(input_list) - 1:

            if (input_list[k] == '0' and layer_list[i][j] == '2'):
                layer_list[i][j] = input_list[k]
            if (input_list[k] == '1' and layer_list[i][j] == '2'):
                layer_list[i][j] = input_list[k]
            k += 1
        # i += 1
        # k += 1

print_final_layer(layer_list)
exit()
    # print("layer_list")
    # print(layer_list)
    # print("k")
    # print(k)
    # print("len")
    # print(len(input_list))
            # column.append('2')
        # layer_list.append(column)

    # print("Zeros")
    # print(layer_list.count('0'))
#     print("final layer_list")
#     print(layer_list)




# print("Solution : ", ones * twos)
# print(layer_list)