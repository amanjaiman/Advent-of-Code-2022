import sys

def parse_file(input_file):
    lines = open(input_file, "r").read()
    l = lines.split("\n\n")
    return l[0].split("\n"), l[1].split("\n")

def create_stacks(crate_lines):
    num_of_stacks = int((len(crate_lines[-1])+1)/4)
    stacks = []

    for i in range(num_of_stacks):
        stacks.append(list(reversed([line[i*4+1] for line in crate_lines if line[i*4+1].isalpha()])))

    return stacks

def perform_inst_p1(inst, stacks):
    for line in inst:
        l = line.strip().split(" ")
        num_of_ops, source, dest = int(l[1]), int(l[3])-1, int(l[5])-1
        
        for i in range(num_of_ops):
            stacks[dest].append(stacks[source].pop())

    return stacks

def perform_inst_p2(inst, stacks):
    for line in inst:
        l = line.strip().split(" ")
        num_of_ops, source, dest = int(l[1]), int(l[3])-1, int(l[5])-1

        stacks[dest] += stacks[source][-num_of_ops:]
        stacks[source] = stacks[source][0:-num_of_ops]
    
    return stacks

def d5_p1(input_file):
    crate_lines, inst = parse_file(input_file)
    stacks = create_stacks(crate_lines)
    stacks = perform_inst_p1(inst, stacks)

    return ''.join([stack[-1] for stack in stacks])

def d5_p2(input_file):
    crate_lines, inst = parse_file(input_file)
    stacks = create_stacks(crate_lines)
    stacks = perform_inst_p2(inst, stacks)

    return ''.join([stack[-1] for stack in stacks])

def main():
    n = len(sys.argv)
    if n != 3:
        return "Usage: d5.py <input_file> <p1 | p2>"
    
    input_file = sys.argv[1]
    part = sys.argv[2]
    if part == "p1":
        return d5_p1(input_file)
    elif part == "p2":
        return d5_p2(input_file)
    else:
        return "Invalid problem part. Must be either p1 or p2"

if __name__ == "__main__":
    out = main()
    print(out)