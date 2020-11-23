from operator import add
from datetime import datetime

startTime = datetime.now()

# moons_positions = [[14, 2, 8], [7, 4, 10], [1, 17, 16], [-4, -1, 1]]

# First Example
moons_positions = [[-1, 0, 2], [2, -10, -7], [4, -8, 8], [3, 5, -1]]
# Second Example
# moons_positions = [[-8, -10, 0], [5, 5, 10], [2, -7, 3], [9, -8, -3]]

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

def motion_simulation():
    global moons_positions_step
    global moons_velocity_step
    steps = 0
    flag = 0
    while flag < 4:
    # while count < 1000:
        # print("Simulation : Moons Positions Step")
        # print(moons_positions_step)
        moons_positions_new[:] = []
        moons_velocity_new[:] = []
        for i, sublist in enumerate(moons_positions_step):
            # print ("index_i : ", index, " sublist = ", sublist)
            moons_positions_new.append([])
            moons_velocity_new.append([])
            for j, nums in enumerate(sublist):
                # print()
                # print ("NEXT NUM : ", moons_positions[i][j], " coordinates : ", i, j)
                # print(moons_positions_copy)
                apply_gravity(i, j, sublist)
        if steps != 0:
            sum_vel_lst = [[sum(x) for x in zip(moons_velocity_new[i], moons_velocity_step[i])] for i in range(len(moons_velocity_new))]
            sum_lst = [[sum(x) for x in zip(moons_positions_new[i], moons_velocity_step[i])] for i in range(len(moons_positions_new))]
            # print("SUM")
            # print(sum_lst)
        moons_positions_step[:] = []
        moons_positions_step = moons_positions_new.copy()
        moons_velocity_step[:] = []
        moons_velocity_step = moons_velocity_new.copy()
        # if steps == 0:
        #     print("Moons Positions after STEP ", steps + 1)
        #     print(moons_positions_step)
        #     print("Moons Velocities after STEP ", steps + 1)
        #     print(moons_velocity_step)
        if steps != 0:
            # print("Moons Positions Final (velocity applied) after STEP ", steps + 1)
            moons_positions_step = sum_lst.copy()
            # print(moons_positions_step)
            # print("Moons Velocity Final (velocity applied) after STEP ", steps + 1)
            moons_velocity_step = sum_vel_lst.copy()
            # print(moons_velocity_step)
            # print()
        steps += 1
        if (moons_positions_step == moons_positions) and (moons_velocity_step == moons_velocity):
            print("Returns in Initial State after : ", steps, " steps")
            flag += 1
    print("Returns in Initial State after : ", steps, " steps")

print("Initial Moons Positions")
print(moons_positions)
print("Initial Moons Velocities")
print(moons_velocity)
print()

motion_simulation()

def total_energy_per_moon():
    potential_energy = 0
    kinetic_energy = 0
    total_energy = 0
    for poslst, velst in zip(moons_positions_step, moons_velocity_step):
        # print(i)
        # print(j)
        poslst_abs =  [abs(ele) for ele in poslst]
        potential_energy = sum(poslst_abs)
        # print(list_abs)
        # potential_energy += poslst_sum
        print("Potential Energy")
        print(potential_energy)
        velst_abs =  [abs(ele) for ele in velst]
        kinetic_energy = sum(velst_abs)
        # print(list_abs)
        # kinetic_energy += sum_abs
        print("Kinetic Energy")
        print(kinetic_energy)
        total_energy += potential_energy * kinetic_energy
        print("Total Energy")
        print(total_energy)
        print()
    return (total_energy)

total_energy_system = 0
total_energy_system += total_energy_per_moon()
print("Total Energy in the System")
print(total_energy_system)

print()
print("Time needed for the executable to run")
print(datetime.now() - startTime)