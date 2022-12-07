import sys

class Directory(object):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.sub_directories = {}
        self.files = []
    
    def get_size(self):
        curr_size = sum([f.size for f in self.files])
        for sub in self.sub_directories:
            curr_size += self.sub_directories[sub].get_size()
        
        return curr_size

    def to_string(self):
        self.to_string = self.name + ": " + str(self.sub_directories.keys()) + " " + str(self.files) + " " + str(self.get_size())
        return self.to_string + "\n\t" + ''.join([self.sub_directories[k].to_string() for k in self.sub_directories.keys()])

class File(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

def process_commands(input_file):
    root = Directory("/")
    with open(input_file, "r") as f:
        curr_dir = None
        for line in f:
            l = line.strip()
            if l.startswith("$ cd"):
                d = l.split(" ")[2]
                if d == "/":
                    curr_dir = root
                elif d == "..":
                    curr_dir = curr_dir.parent
                else:
                    curr_dir = curr_dir.sub_directories[d]
            elif l.startswith("$ ls"):
                continue
            elif l.startswith("dir"):
                d = l.split(" ")[1]
                curr_dir.sub_directories[d] = Directory(d, curr_dir)
            else:
                s = int(l.split(" ")[0])
                n = l.split(" ")[1]

                curr_dir.files.append(File(n, s))
    return root

def get_size_of_valid(root, valid_size):
    size = 0
    if root.get_size() <= valid_size:
        size += root.get_size()
    
    for child in root.sub_directories:
        size += get_size_of_valid(root.sub_directories[child], valid_size)
    
    return size

def get_size_of_removable(root, space_to_delete, curr_min):
    new_min = curr_min
    size = root.get_size()

    if size >= space_to_delete and size < curr_min:
        new_min = size

    if not bool(root.sub_directories):
        return new_min
    else:
        for child in root.sub_directories.keys():
            new_min = min(new_min, get_size_of_removable(root.sub_directories[child], space_to_delete, new_min))
        return new_min

def d7_p1(input_file):
    max_size = 100000
    root = process_commands(input_file)        
    return get_size_of_valid(root, max_size)

def d7_p2(input_file):
    total_space = 70000000
    min_space = 30000000
    root = process_commands(input_file)
    space_to_delete = min_space - total_space + root.get_size()
    return get_size_of_removable(root, space_to_delete, total_space)

def main():
    n = len(sys.argv)
    if n != 3:
        return "Usage: d7.py <input_file> <p1 | p2>"
    
    input_file = sys.argv[1]
    part = sys.argv[2]
    if part == "p1":
        return d7_p1(input_file)
    elif part == "p2":
        return d7_p2(input_file)
    else:
        return "Invalid problem part. Must be either p1 or p2"

if __name__ == "__main__":
    out = main()
    print(out)