user_input = ""
with open("input.txt") as my_file:
    for line in my_file:
        user_input += line

def mul(num1: int, num2: int) -> int:
    return num1 * num2

import re
filtered = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", user_input)

sum = 0

is_counted = True
for item in filtered:
    if item == "don't()":
        is_counted = False
        continue
    elif item == "do()":
        is_counted = True
        continue
    
    if is_counted:
        sum += eval(item)

print(sum)