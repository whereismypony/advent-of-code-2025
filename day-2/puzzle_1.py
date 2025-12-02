id_ranges = open('day-2\input.txt').read().split(',')
total_matching_ids = 0
total_sum = 0


for range in id_ranges:
    start, end = map(int, range.split('-'))
    while(start <= end):
        start_string = str(start)
        mid = len(start_string) // 2
        s_1 = start_string[:mid]
        s_2 = start_string[mid:]
        if s_1 == s_2:
            print(f"Matching ID found: {start_string}")
            total_matching_ids += 1
            total_sum += start
        
        start += 1
        
print(f"Total of matching IDs: {total_matching_ids}")
print(f"Sum of matching IDs: {total_sum}")