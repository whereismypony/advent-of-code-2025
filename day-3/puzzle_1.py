with open('day-3\input.txt') as file:
    lines = [line.strip() for line in file]

total = 0

def get_largest_number(number_string):
    target_length = 2
    stack = []
    removals_allowed = len(number_string) - target_length
    
    for digit in number_string:
        while stack and removals_allowed > 0 and stack[-1] < digit:
            stack.pop()
            removals_allowed -= 1
        stack.append(digit)
        
    return ''.join(stack[:target_length])


for line in lines:
    Largest_number = int(get_largest_number(line))
    total += Largest_number
    print(f"Largest number in line: {line} is {Largest_number}")
    
    
print(f"Final total: {total}")
    