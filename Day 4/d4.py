import sys

def get_sets(pairs):
    p1 = pairs[0].split("-")
    p2 = pairs[1].split("-")
    s1 = set(range(int(p1[0]), int(p1[1])+1))
    s2 = set(range(int(p2[0]), int(p2[1])+1))

    return s1, s2

def d4_p1(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            pairs = line.strip().split(",")
            s1, s2 = get_sets(pairs)

            if s1.issubset(s2) or s2.issubset(s1):
                total += 1
    
    return total

def d4_p2(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            pairs = line.strip().split(",")
            s1, s2 = get_sets(pairs)

            if s1 & s2:
                total += 1

    return total

def main():
    n = len(sys.argv)
    if n != 3:
        return "Usage: d4.py <input_file> <p1 | p2>"
    
    input_file = sys.argv[1]
    part = sys.argv[2]
    if part == "p1":
        return d4_p1(input_file)
    elif part == "p2":
        return d4_p2(input_file)
    else:
        return "Invalid problem part. Must be either p1 or p2"

if __name__ == "__main__":
    out = main()
    print(out)