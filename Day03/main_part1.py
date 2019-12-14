# list_wire1 = ['R8', 'U5', 'L5', 'D3']
# list_wire2 = ['U7', 'R6', 'D4', 'L4']


list_wire1 = []
with open ("wire1.txt") as myfile:
    for line in myfile:
        list_wire1 = line.split(',')
# print("Wire1 Input")
# print(list_wire1)

list_wire2 = []
with open ("wire2.txt") as myfile:
    for line in myfile:
        list_wire2 = line.split(',')
# print("Wire2 Input")
# print(list_wire2)

# Printing a list of lists in a more clear way
# Combine everything into one long string and then print it
# print('\n'.join(' '.join(map(str, sub)) for sub in listoflists))


wire1 = set()
wire2 = set()

def store_path(coord, coord_set):
    global last_pos_tup
    global wire1
    global wire2
    if (coord[:1] == 'R'):
        len = int(coord[1:])
        i = 0
        x = last_pos_tup[0]
        y = last_pos_tup[1]
        while (i <= len):
            tup = (x + i, y)
            i += 1
            coord_set.add(tup)
        last_pos_tup = tup
        # print(coord_set)
    if (coord[:1] == 'L'):
        len = int(coord[1:])
        i = 0
        x = last_pos_tup[0]
        y = last_pos_tup[1]
        while (i <= len):
            tup = (x - i, y)
            i += 1
            coord_set.add(tup)
        last_pos_tup = tup
        # print(coord_set)
    if (coord[:1] == 'U'):
        len = int(coord[1:])
        i = 0
        x = last_pos_tup[0]
        y = last_pos_tup[1]
        while (i <= len):
            tup = (x, y + i)
            i += 1
            coord_set.add(tup)
        last_pos_tup = tup
        # print(coord_set)
    if (coord[:1] == 'D'):
        len = int(coord[1:])
        i = 0
        x = last_pos_tup[0]
        y = last_pos_tup[1]
        while (i <= len):
            tup = (x, y - i)
            i += 1
            coord_set.add(tup)
        last_pos_tup = tup
        # print(coord_set)

last_pos_tup = (0, 0)
# tup = (0, 0)
for coord in list_wire1:
    store_path(coord, wire1)
#     print("Last Position Tuple")
#     print(last_pos_tup)
print("Print Wire1 Set")
# wire1.add(tup)
print(wire1)   


last_pos_tup = (0, 0)
# tup = (0, 0)
for coord in list_wire2:
    store_path(coord, wire2)
    # print("Last Position Tuple")
    # print(last_pos_tup)
print("Print Wire2 Set")
# wire2.add(tup)
print(wire2)

# intersection 
print("Intersection :", wire1 & wire2) 
intersection = wire1 & wire2
# remove the tuple with the minus
intersection = {element for element in intersection if element not in {(0,0)}}


distance = 100000000
for coord in intersection:
    current_distance = abs(coord[0]) + abs(coord[1])
    if (current_distance <= distance):
        distance = current_distance
        # print("coord[0]")
        # print(coord[0])
        # print("coord[1]")
        # print(coord[1])
        # print("distance")
        # print(distance)
        # print("current distance")
        # print(current_distance)
print("Distance to closest intersection")
print(distance)

