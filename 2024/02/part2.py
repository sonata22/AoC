def validate_line(line:str) -> bool:

    if len(line) != len(set(line)):
        return False
    for index in range(len(line)):
        line[index] = int(line[index])

    order_valid = False
    if line == sorted(line):
        order_valid = True
    elif line == sorted(line, reverse=True):
        order_valid = True
    if order_valid == False:
        return False
    
    distance_valid = True
    for index in range(len(line)-1):
        if abs(line[index] - line[index+1]) > 3:
            distance_valid = False
    if distance_valid == False:
        return False
    
    return True
    
def main():
    with open("input.txt") as file_opened:
        counter = 0
        for line in file_opened:
            line = line.replace("\n", "").split(" ")
            
            if validate_line(line):
                counter += 1
            else:
                for index in range(len(line)):
                    new_line = line[:]
                    del new_line[index]
                    if validate_line(new_line):
                        counter += 1
                        break

        print(counter)

main()
