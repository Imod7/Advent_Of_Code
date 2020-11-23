original_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]

input = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,19,5,23,2,23,13,27,1,10,27,31,2,31,6,35,1,5,35,39,1,39,10,43,2,9,43,47,1,47,5,51,2,51,9,55,1,13,55,59,1,13,59,63,1,6,63,67,2,13,67,71,1,10,71,75,2,13,75,79,1,5,79,83,2,83,9,87,2,87,13,91,1,91,5,95,2,9,95,99,1,99,5,103,1,2,103,107,1,10,107,0,99,2,14,0,0]
# input = [1,0,0,0,99]
# input = [2,3,0,3,99]
# input = [2,4,4,5,99,0]
# input = [1,1,1,4,99,5,6,0,99]

print("Initial List")
print(input)

def addition(i, input_lst):
    print(i, end = " ")
    print(input[i]) 
    pos1 = input_lst[i + 1]
    pos2 = input_lst[i + 2]
    pos3 = input_lst[i + 3]
    print(pos1)
    print(pos2)
    print(pos3)
    sum = input_lst[pos1] + input_lst[pos2]
    print(sum)
    input_lst[pos3] = sum
    print("addition")
    print(input_lst)

def multiplication(i, input_lst):
    pos1 = input_lst[i + 1]
    pos2 = input_lst[i + 2]
    pos3 = input_lst[i + 3]
    mult = input_lst[pos1] * input_lst[pos2]
    input_lst[pos3] = mult
    print("multiplication")
    print(input_lst)

i = 0
while i < len(input):
    print("next loop")
    print(i, end = " ")
    print(input[i]) 
    if (input[i] == 1):
        addition(i, input)
    elif (input[i] == 2):
        multiplication(i, input)
    elif (input[i] == 99):
        print("Final Result")
        print(input[0])
        break
    i = i + 4
    # print(i)

print("Final List")
print(input)