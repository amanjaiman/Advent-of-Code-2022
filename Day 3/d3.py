import sys

def get_priority(c):
    return (ord(c)-96)%58

def d3_p1(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            h_index = int((len(line)-1)/2)
            h1 = set(line[0:h_index])
            h2 = set(line[h_index:])
            common = list(h1 & h2)[0]
            total += get_priority(common)
    
    return total

def d3_p2(input_file):
    total = 0
    lines = open(input_file, "r").readlines()

    for i in range(0, len(lines), 3):
        group = [set(lines[i].strip()), set(lines[i+1].strip()), set(lines[i+2].strip())]
        common = list(group[0] & group[1] & group[2])[0]
        total += get_priority(common)
    
    return total

def main():
    n = len(sys.argv)
    if n != 3:
        return "Usage: d3.py <input_file> <p1 | p2>"
    
    input_file = sys.argv[1]
    part = sys.argv[2]
    if part == "p1":
        return d3_p1(input_file)
    elif part == "p2":
        return d3_p2(input_file)
    else:
        return "Invalid problem part. Must be either p1 or p2"

if __name__ == "__main__":
    out = main()
    print(out)