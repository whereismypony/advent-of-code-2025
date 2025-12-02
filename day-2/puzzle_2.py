import re

id_ranges = open('day-2\input.txt').read().split(',')
total_matching_ids = 0
total_sum = 0

pattern = r"^(\d+)\1+$"

for range in id_ranges:
    start, end = map(int, range.split('-'))
    while(start <= end):
        if re.match(pattern, str(start)):
            print(f"Matching ID found: {start}")
            total_matching_ids += 1
            total_sum += start
            
        start += 1
        
print(f"Total of matching IDs: {total_matching_ids}")
print(f"Sum of matching IDs: {total_sum}")