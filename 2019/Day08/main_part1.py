

input_list = []
with open("puzzle_input.txt") as f:
  while True:
    c = f.read(1)
    if not c:
    #   print "End of file"
      break
    input_list.append(c)

# print(input_list)

layer_list_final = []
i = 0
zeros = 200
while i < len(input_list):
    j = 0
    layer_list = []
    while j < 150:
        layer_list.append(input_list[i])
        i += 1
        j += 1
    # print("Zeros")
    # print(layer_list.count('0'))
    # print("layer_list")
    # print(layer_list)
    if (layer_list.count('0') < zeros):
        zeros = layer_list.count('0')
        layer_list_final = layer_list
        # layer += 1

ones = layer_list_final.count('1')
twos = layer_list_final.count('2')

print("Solution : ", ones * twos)
# print(layer_list)

