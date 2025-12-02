dial = 50
count = 0

with open('day-1\input.txt') as file:
    lines = [line.strip() for line in file]

print(f"Starting Dial: {dial}")

for line in lines:
    direction = line[:1]
    amount = int(line[1:])
    
    if direction == 'R':
        dial += amount
        while(dial > 99):
            dial -= 100
    elif direction == 'L':
        dial -= amount
        while(dial < 0):
            dial += 100
    
    if dial == 0:
        count += 1
        
    
            
    print(f"Direction: {direction} | Amount: {amount} | New Dial: {dial} | Count: {count}")

    
    