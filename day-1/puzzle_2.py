dial = 50
count = 0

with open('day-1\input.txt') as file:
    lines = [line.strip() for line in file]

print(f"Starting Dial: {dial}")

for line in lines:
    direction = line[:1]
    amount = int(line[1:])
    
    count += amount // 100
    remainder = amount % 100
    
    if direction == 'R':
        if dial + remainder >= 100:
            count += 1
        dial = (dial + remainder) % 100
        
    elif direction == 'L':
        if dial == 0:
            pass
        elif dial - remainder <= 0:
            count += 1
        dial = (dial - remainder) % 100
        
    
            
    print(f"Direction: {direction} | Amount: {amount} | New Dial: {dial} | Count: {count}")

    
    