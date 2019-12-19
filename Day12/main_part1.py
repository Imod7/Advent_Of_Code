from operator import add

# moons_positions = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]
moons_positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]

moons_velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

moons_positions_step = []
moons_velocity_step = []
def apply_gravity(i, j, sublist):
    result = moons_positions[i][j]
    velocity = 0
    for k, sublist in enumerate(moons_positions):
        # print ("Comparing : ", moons_positions[i][j], " with ", moons_positions[k][j])
        if moons_positions[i][j] > moons_positions[k][j]:
            result -= 1
            velocity -= 1
        elif moons_positions[i][j] < moons_positions[k][j]:
            result += 1
            velocity += 1
    # print(velocity)
    moons_positions_step[i].append(result)
    moons_velocity_step[i].append(velocity)

def apply_velocity(pos_lst, vel_lst):
    print(pos_lst)
    for i, pos in range(len(pos_lst)):
        for j, vel in range(len(vel_lst)):
            moons_positions_step[i][j] = moons_positions_step[i][j] + vel_lst[i][j]

def motion_simulation(steps):
    count = 0
    while count < steps:
        for i, sublist in enumerate(moons_positions):
            # print ("index_i : ", index, " sublist = ", sublist)
            moons_positions_step.append([])
            moons_velocity_step.append([])
            for j, nums in enumerate(sublist):
                # print()
                # print ("NEXT NUM : ", moons_positions[i][j], " coordinates : ", i, j)
                apply_gravity(i, j, sublist)
        if count != 0:
            sum_lst = [[sum(x) for x in zip(moons_positions_step[i], moons_velocity_step[i])] for i in range(len(moons_positions_step))]
        print("Moons Positions after STEP ", count + 1)
        print(moons_positions_step)
        print("Moons Velocities after STEP ", count + 1)
        print(moons_velocity_step)
        if count != 0:
            print("Moons Positions Final (velocity applied) after STEP ", count + 1)
            print(sum_lst)
        count += 1
        print()

print("Initial Moons Positions")
print(moons_positions)
print("Initial Moons Velocities")
print(moons_velocity)
print()

steps = 1
motion_simulation(steps)



# for i, sublist in enumerate(moons_positions_step):
#     apply_velocity(sublist, moons_velocity)

# [sum(x) for x in zip(list1, list2)]

# sum_lst = list( map(add, moons_positions_step, moons_velocity_step) )


