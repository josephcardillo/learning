import random, time, copy

WIDTH = 30

# create empty list called binary
binary = []
# Randomly create a list of ten 0s and 1s:
for i in range(WIDTH):
    binary.append(random.randint(0, 1))

while True:
    # copy binary to give it a new id, and a new place in the computer's memory
    binary_copy = copy.copy(binary)
    # print out the values in binary list so they appear next to each other, without quotes around them
    for i in range(WIDTH):
        print(binary_copy[i], end='')
    print() # print a newline

    # switch the 0s and 1s in binary
    for i in range(len(binary)):
        if binary[i] == 0:
            binary[i] = 1
        else:
            binary[i] = 0

    # create empty list called binary_shifted
    binary_shifted = []
    # Shift all values to the left
    for i in range(len(binary) - 1):
        binary_shifted.append(binary[i + 1])
    # shift first value to last value
    binary_shifted.append(binary[0])
    binary = binary_shifted

    # sleep for one second
    time.sleep(1)