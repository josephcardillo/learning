import random

# create an empty list for the flips
flips = []

# flip coin 10000 times
for flip in range(10000):
    # if the random flip is 0, it's heads
    if random.randint(0, 1) == 0:
        # append "H" to the flips list
        flips.append("H")
    else:
        # append "T" to the flips list
        flips.append("T")

# create streak variabled to track number of streaks of six heads or tails
streak = 0

# use a for loop to run through the flips list
for i in range(len(flips)):
    # [i:i + 6] gets a slice of six elements from flips list
    # if that slice of six equals six H's or six T's, add 1 to our streak
    if " ".join(flips[i:i + 6]) == "H H H H H H" or " ".join(flips[i:i + 6]) == "T T T T T T":
        streak += 1

print(f"Chance of streak of six is: {streak / 100}%.")
