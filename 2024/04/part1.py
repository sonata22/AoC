import re
#diagonal, written backwards, or even overlapping other words
def find_horizontal_matches(my_list: list, word: str) -> int:
    counter = 0
    for line in my_list:
        len_of_matches_found = len(re.findall(f"{word}", line))
        counter += len_of_matches_found
        # print(f"{len_of_matches_found} matches of {word} found")
    return counter

def find_vertical_matches(my_list: list, word: str) -> int:
    counter = 0
    for x in range(len(my_list)-3):
        for y in range(len(my_list)):
            if my_list[x][y] == word[0]:
                if my_list[x+1][y] == word[1]:
                    if my_list[x+2][y] == word[2]:
                        if my_list[x+3][y] == word[3]:
                            counter += 1
    return counter

def find_diagonal_matches(my_list: list, word: str) -> int:
    counter = 0
    for x in range(len(my_list)-3):
        for y in range(len(my_list)-3):
            if my_list[x][y] == word[0]:
                if my_list[x+1][y+1] == word[1]:
                    if my_list[x+2][y+2] == word[2]:
                        if my_list[x+3][y+3] == word[3]:
                            counter += 1

    for x in range(1, len(my_list)-2):
        for y in range(1, len(my_list)-2):
            if my_list[-x][-y] == word[0]:
                if my_list[-x-1][-y-1] == word[1]:
                    if my_list[-x-2][-y-2] == word[2]:
                        if my_list[-x-3][-y-3] == word[3]:
                            counter += 1
    return counter
    
if __name__ == "__main__":
    lines = []
    with open("input.txt") as lines_file:
        for line in lines_file:
            lines.append(line.replace("\n", ""))

    total = 0

    total += find_horizontal_matches(lines, "XMAS")
    total += find_horizontal_matches(lines, "SAMX")
    total += find_vertical_matches(lines, "XMAS")
    total += find_vertical_matches(lines, "SAMX")
    total += find_diagonal_matches(lines, "XMAS")
    total += find_diagonal_matches(lines, "SAMX")

    print(total)