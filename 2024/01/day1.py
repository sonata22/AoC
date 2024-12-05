left, right = [], []
with open("/home/sonata/Documents/repos/AoC/2024/01/input.txt") as file_read:
    for line in file_read:
        l, r = line.replace("\n", "").split("   ")
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()

# for index in range(len(left)):
#     print(f"left: {left[index]}, right: {right[index]}")

# counter = 0
# for index in range(len(left)):
#     counter += abs(left[index] - right[index])
# print(counter)

counter = 0
for x in range(len(left)):
    for y in range(len(right)):
        if left[x] == right[y]:
            counter += left[x]

print(counter)