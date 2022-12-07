import os
import sys

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
    
    # wanted to download the input as well but you cannot without logging in

    return

if __name__ == "__main__":
    main()