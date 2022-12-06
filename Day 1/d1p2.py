from sortedcontainers import SortedList

x = SortedList([])

with open("d1.input", "r") as f:
    curr_total = 0
    for line in f:
        if line == '\n':
            x.add(curr_total)
            curr_total = 0
        else:
            curr_total += int(line.strip())

print(sum(x[-3:]))