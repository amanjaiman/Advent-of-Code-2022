scores = {0: 1, 1: 2, 2: 3}
opps = {"A": 0, "B": 1, "C": 2}
results = {"X": 0, "Y": 3, "Z": 6}

total_score = 0
with open("d2.sample.input", "r") as f:
    for line in f:
        opp = line.split(" ")[0]
        result = line.split(" ")[1].strip()

        total_score += results[result]

        opp_num = opps[opp]
        if result == "X":
            your_num = (opp_num-1)%3
            total_score += scores[your_num]
        elif result == "Y":
            total_score += scores[opp_num]
        elif result == "Z":
            your_num = (opp_num+1)%3
            total_score += scores[your_num]

print(total_score)