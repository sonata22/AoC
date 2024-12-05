with open("input.txt") as file_opened:
    counter = 0
    for line in file_opened:
        line = line.replace("\n", "").split(" ")
        # skip lines with duplicates
        if len(line) != len(set(line)):
            continue
        # str to int
        for index in range(len(line)):
            line[index] = int(line[index])
        # check order
        order_valid = False
        if line == sorted(line):
            order_valid = True
            # print(f"YES, o: {line}\n     s: {sorted(line)}")
        elif line == sorted(line, reverse=True):
            order_valid = True
            # print(f"YES, o: {line}\n    sr: {sorted(line, reverse=True)}")
        # else:
            # print(f"NO: {line}")
        # skip invalid order lines
        if order_valid == False:
            continue
        
        distance_valid = True
        # print(f"\nLINE: {line}")
        for index in range(len(line)-1):
            # print(f"{line[index]}-{line[index+1]}", end="=")
            if abs(line[index] - line[index+1]) > 3:
                # print(f"{abs(line[index] - line[index+1])}")
                distance_valid = False
            else:
                pass
            #     print(f"invalid: {abs(line[index] - line[index+1])}")
        # skip invalid distance lines
        if distance_valid == False:
            continue

        counter += 1
    print(counter)
