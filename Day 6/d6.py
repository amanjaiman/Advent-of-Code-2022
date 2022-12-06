import sys

def all_diff(sub, length):
    if len(set(sub)) == length:
        return True

def d6(input_file, length):
    data = open(input_file, "r").readline().strip()
    s, e = 0, length
    sub = data[s:e]
    while not all_diff(sub, length):
        s += 1
        e += 1
        sub = data[s:e]
    
    return e

def main():
    n = len(sys.argv)
    if n != 3:
        return "Usage: d6.py <input_file> <p1 | p2>"
    
    input_file = sys.argv[1]
    part = sys.argv[2]
    if part == "p1":
        return d6(input_file, 4)
    elif part == "p2":
        return d6(input_file, 14)
    else:
        return "Invalid problem part. Must be either p1 or p2"

if __name__ == "__main__":
    out = main()
    print(out)