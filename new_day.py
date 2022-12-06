import os
import sys

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

def main():
    n = len(sys.argv)
    if n != 2:
        print("Usage: new_day.py <day_number>")
        return

    day = sys.argv[1]
    os.mkdir("Day %s"%day)
    os.chdir("Day %s"%day)

    prefix = "d%s"%day
    with open(prefix+".py", "w+") as f:
        with open("../template.txt", "r") as g:
            contents = g.read()
            new_contents = contents.replace("${day}", prefix)
            f.write(new_contents)
    
    with open(prefix+".sample.input", "w+") as f:
        f.write("")
    
    return

if __name__ == "__main__":
    main()