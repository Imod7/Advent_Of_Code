

input_list = []
with open("input.txt") as file:
    input_list = file.read().splitlines()

# print(input_list)

def indirect_orbits(str, count):
    # match = [s for s in input_list if str == str[-3:]]
    match = [i for i, s in enumerate(input_list) if str == s[-3:]]
    # print("match = ", match)
    if (len(match) > 0):
        # count += 1
        print("str = ", str, " index = ", match, " item = ", input_list[match[0]][:3])
        # indirect_orbits(input_list[match[0]][:3], count)
        # print(">>----- count = ", count)
        return (indirect_orbits(input_list[match[0]][:3], count + 1))
    else:
        # print(">> COUNT = ", count)
        return (count)

def direct_orbits(str):
    count = 0
    count1 = 0
    direct = str[-3:]
    print("\ndirect = ", direct)
    print("\nindirect = ", str[:3])
    count1 += indirect_orbits(str[:3], count)
    # print("str = ", str)
    print(">> count1 = ", count1)
    return (count1)


orbits = 0
indir_orbits = 0
while orbits < len(input_list):
# while orbits < 2:
    indir_orbits += direct_orbits(input_list[orbits])
    print("indirect count = ", indir_orbits)
    orbits += 1

print("Direct Orbits = ", orbits)
print("Indirect Orbits = ", indir_orbits)
print("Total Orbits = ", orbits + indir_orbits)