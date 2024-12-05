import re

# horizontal, vertical, diagonal, written backwards, or even overlapping other words.
if __name__ == "__main__":
    lines = []
    with open("/home/sonata/Documents/repos/AoC/2024/04/input.txt") as lines_file:
        for line in lines_file:
            lines.append(line.replace("\n", "").split(""))
    lines_copy = lines[:]
    # add reversed horizontal lines
    # for line in lines_copy:
    #     lines.append(line[::-1])
    # add vertical lines
    for x in range(len(lines_copy)):
        new_str = ""
        for line in lines_copy:
            new_str += line[x]
        # print(new_str)
    # add diagonal lines
    new_str = ""
    for x in range(len(lines_copy)):
        new_str += lines_copy[x][len(lines_copy)-x]
        print(new_str)

    total = 0
    print(total)


# >>> var = [range(x, x+5) for x in range(0, 25, 5)]
# >>> print '\n'.join(' '.join('%2d' % c for c in r) for r in var)
#  0  1  2  3  4
#  5  6  7  8  9
# 10 11 12 13 14
# 15 16 17 18 19
# 20 21 22 23 24
# >>> [var[1+t][4-t] for t in range(4)]
# [9, 13, 17, 21]
# >>> [var[2+t][1+t] for t in range(3)]
# [11, 17, 23]