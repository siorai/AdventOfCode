def part1(data):
    houses = {}
    x = 0
    y = 0
    for eachDirection in data:
        if eachDirection == "v":
            y += -1
        elif eachDirection == ">":
            x += 1
        elif eachDirection == "<":
            x += -1
        elif eachDirection == "^":
            y += 1
        currentHouse = f"{x},{y}"
        if currentHouse not in houses.keys():
            houses[currentHouse] = 1
        else:
            houses[currentHouse] += 1
    return len(houses)


def part2(data):
    santa = []
    roboSanta = []
    for directionIter, direction in enumerate(data):
        if directionIter == 0 or directionIter % 2 == 0:
            santa.append(direction)
        else:
            roboSanta.append(direction)
    houses = {}
    x = 0
    y = 0
    for eachDirection in santa:
        if eachDirection == "v":
            y += -1
        elif eachDirection == ">":
            x += 1
        elif eachDirection == "<":
            x += -1
        elif eachDirection == "^":
            y += 1
        currentHouse = f"{x},{y}"
        if currentHouse not in houses.keys():
            houses[currentHouse] = 1
        else:
            houses[currentHouse] += 1
    x = 0
    y = 0
    for eachDirection in roboSanta:
        if eachDirection == "v":
            y += -1
        elif eachDirection == ">":
            x += 1
        elif eachDirection == "<":
            x += -1
        elif eachDirection == "^":
            y += 1
        currentHouse = f"{x},{y}"
        if currentHouse not in houses.keys():
            houses[currentHouse] = 1
        else:
            houses[currentHouse] += 1
    return len(houses)


