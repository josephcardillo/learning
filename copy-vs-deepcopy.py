# import random, time, copy

# WIDTH = 10

# binary = []
# # Randomly create 0 or 1 in a row of 10:
# for i in range(WIDTH):
#     if random.randint(0, 1) == 0: # create a random number of 0 or 1
#         binary.append(0) # if 0, append to binary list
#     else:
#         binary.append(1) # if 1, append to binary list

# # print(f"binary is:")
# # print(binary)

# while True:
# # for i in range(0, 3):
#     binary_copy = copy.copy(binary) # copy binary to give it a new ID, and a new place in the computers memory
#     for i in range(WIDTH):
#         print(binary_copy[i], end='') # print out the values in binary so they appear next to each other, without quotes around them
#     print() # print a newline

#     for i in range(len(binary)):
#         # print(f"i is: {i}, binary[thing] is {binary[i]}")
#         if binary[i] == 0:
#             binary[i] = 1
#         else:
#             binary[i] = 0
#     # print("after switching zeros and ones, binary is:")
#     # print(binary)

#     binary_shifted = []
#     for i in range(len(binary) - 1):
#         binary_shifted.append(binary[i + 1])
#     binary_shifted.append(binary[0])
#     binary = binary_shifted
#     # print("after shifting all the numbers to the left, binary is:")
#     # print(binary)

#     time.sleep(1)


# binary = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
# binary_copy = copy.copy(binary)
# print(binary_copy)

import random, time, copy

WIDTH = 10

binary = []
# Randomly create 0 or 1 in a row of 10:
for i in range(WIDTH):
    if random.randint(0, 1) == 0:
        binary.append(0)
    else:
        binary.append(1)

print(f"binary is:")
print(binary)

for i in range(0, 3):
    # copy binary to give it a new ID, and a new place in the computer's memory
    binary_copy = copy.copy(binary)

    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0
    print("after switching zeros and ones, binary is:")
    print(binary)
