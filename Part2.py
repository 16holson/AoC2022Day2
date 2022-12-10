def readFile():
    file = open("InputData.txt", "r")
    return file


"""
A, X = Rock
B, Y = Paper
C, Z = Scissors
Points: 
Rock: 1
Paper: 2
Scissors: 3
Lose: 0
Tie: 3
Win: 6
"""


def findResults(line, points):
    # Tie
    if (line[0] == line[1]):
        return (points["Tie"] + int(line[1]) + 1)
    # Win
    elif ((int(line[0]) + 1) % 3 == int(line[1])):
        return (points["Win"] + int(line[1]) + 1)
    # Lost
    else:
        return (points["Lose"] + int(line[1]) + 1)


def replaceInput(line):
    replace = [("A", "0"), ("B", "1"), ("C", "2"), ("X", "0"), ("Y", "1"), ("Z", "2")]
    for (a, b) in replace:
        line = line.replace(a, b)
    return rigInput(line)


def rigInput(line):
    # Lose
    if (line[1] == "0"):
        if (line[0] == "0"):
            line = line[0] + "2"
        elif (line[0] == "1"):
            line = line[0] + "0"
        else:
            line = line[0] + "1"
        return line
    # Tie
    elif (line[1] == "1"):
        line = line[0] + line[0]
        return line
    # Win
    else:
        if (line[0] == "0"):
            line = line[0] + "1"
        elif (line[0] == "1"):
            line = line[0] + "2"
        else:
            line = line[0] + "0"
        return line


def main():
    file = readFile()
    total = 0
    points = {"Lose": 0, "Tie": 3, "Win": 6}
    for line in file:
        total += findResults(replaceInput(line.strip().replace(" ", "")), points)
    print(f"Total points: {total}")
    file.close()

if (__name__ == "__main__"):
    main()
