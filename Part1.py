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
        print(f"Tie {line[0]} = {line[1]}")
        return (points["Tie"] + int(line[1]) + 1)
    # Win
    elif ((int(line[0]) + 1) % 3 == int(line[1])):
        print(f"Win {line[0]} , {line[1]}")
        return (points["Win"] + int(line[1]) + 1)
    # Lost
    else:
        print(f"Lost {line[0]} , {line[1]}")
        return (points["Lose"] + int(line[1]) + 1)


def replaceInput(line):
    replace = [("A", "0"), ("B", "1"), ("C", "2"), ("X", "0"), ("Y", "1"), ("Z", "2")]
    for (a, b) in replace:
        line = line.replace(a, b)
    return line


def main():
    file = readFile()
    total = 0
    points = {"Lose": 0, "Tie": 3, "Win": 6}
    for line in file:
        total += findResults(replaceInput(line.strip().replace(" ", "")), points)
    print(f"Total points: {total}")


if (__name__ == "__main__"):
    main()
