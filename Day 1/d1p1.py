max_cal = 0
with open("d1.input", "r") as f:
    curr_total = 0
    for line in f:
        if line == '\n':
            if curr_total > max_cal:
                max_cal = curr_total
            curr_total = 0
        else:
            curr_total += int(line.strip())

print(max_cal)