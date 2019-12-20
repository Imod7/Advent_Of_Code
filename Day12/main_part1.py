from operator import add

# moons_positions = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]
moons_positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
moons_velocity = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

moons_positions_step = moons_positions.copy()
moons_positions_new = []
moons_velocity_step = moons_velocity.copy()
moons_velocity_new = []

def apply_gravity(i, j, sublist):
    # print(i, j)
    # print(moons_positions_new)
    # print(moons_positions_new[0][0])
    result = moons_positions_step[i][j]
    velocity = 0
    for k, sublist in enumerate(moons_positions_step):
        # print ("Comparing : ", moons_positions_step[i][j], " with ", moons_positions_step[k][j])
        if moons_positions_step[i][j] > moons_positions_step[k][j]:
            result -= 1
            velocity -= 1
        elif moons_positions_step[i][j] < moons_positions_step[k][j]:
            result += 1
            velocity += 1
    # print(velocity)
    # print(result)
    moons_positions_new[i].append(result)
    # moons_positions_step[i][j] = result
    moons_velocity_new[i].append(velocity)

# def apply_velocity(pos_lst, vel_lst):
#     print(pos_lst)
#     for i, pos in range(len(pos_lst)):
#         for j, vel in range(len(vel_lst)):
#             moons_positions_step[i][j] = moons_positions_step[i][j] + vel_lst[i][j]

def motion_simulation(steps):
    global moons_positions_step
    global moons_velocity_step
    count = 0
    while count < steps:
        # print("Simulation : Moons Positions Step")
        # print(moons_positions_step)
        moons_positions_new[:] = []
        moons_velocity_new[:] = []
        for i, sublist in enumerate(moons_positions_step):
            # print ("index_i : ", index, " sublist = ", sublist)
            moons_positions_new.append([])
            # print("== Moons positions ==")
            # print(moons_positions_new)
            moons_velocity_new.append([])
            for j, nums in enumerate(sublist):
                # print()
                # print ("NEXT NUM : ", moons_positions[i][j], " coordinates : ", i, j)
                # print(moons_positions_copy)
                apply_gravity(i, j, sublist)
        # print("Moons NEW")
        # print(moons_positions_new)
        # print("Moons veloc NEW")
        # print(moons_velocity_new)
        if count != 0:
            sum_vel_lst = [[sum(x) for x in zip(moons_velocity_new[i], moons_velocity_step[i])] for i in range(len(moons_velocity_new))]
            sum_lst = [[sum(x) for x in zip(moons_positions_new[i], moons_velocity_step[i])] for i in range(len(moons_positions_new))]
            # print("SUM")
            # print(sum_lst)
        moons_positions_step[:] = []
        moons_positions_step = moons_positions_new.copy()
        moons_velocity_step[:] = []
        moons_velocity_step = moons_velocity_new.copy()
        if count == 0:
            print("Moons Positions after STEP ", count + 1)
            print(moons_positions_step)
            print("Moons Velocities after STEP ", count + 1)
            print(moons_velocity_step)
        if count != 0:
            print("Moons Positions Final (velocity applied) after STEP ", count + 1)
            moons_positions_step = sum_lst.copy()
            print(moons_positions_step)
            print("Moons Velocity Final (velocity applied) after STEP ", count + 1)
            moons_velocity_step = sum_vel_lst.copy()
            print(moons_velocity_step)
        count += 1
        print()

print("Initial Moons Positions")
print(moons_positions)
print("Initial Moons Velocities")
print(moons_velocity)
print()

steps = 4
motion_simulation(steps)



# for i, sublist in enumerate(moons_positions_step):
#     apply_velocity(sublist, moons_velocity)

# [sum(x) for x in zip(list1, list2)]

# sum_lst = list( map(add, moons_positions_step, moons_velocity_step) )


