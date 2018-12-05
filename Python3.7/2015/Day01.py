def part1(data):
    currentFloor = 0
    for eachParent in data:
        if eachParent == '(':
            currentFloor += 1
        else:
            currentFloor += -1
    return currentFloor


def part2(data):
    currentFloor = 0
    for parentPlace, eachParent in enumerate(data):
        if currentFloor == -1:
            return parentPlace
        if eachParent == '(':
            currentFloor += 1
        else:
            currentFloor += -1
            
