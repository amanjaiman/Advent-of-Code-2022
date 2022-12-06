scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

total_score = 0
with open("d2.input", "r") as f:
    for line in f:
        opp = line.split(" ")[0]
        you = line.split(" ")[1].strip()

        total_score += scores[you]

        if scores[you] == scores[opp]:
            total_score += 3
        elif (you == "X" and opp == "C") or (you == "Y" and opp == "A") or (you == "Z" and opp == "B"):
            total_score += 6

print(total_score)