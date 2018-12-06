def part1(data):
    coordinateData = {}
    coordinateData2 = {}
    coordinates = set()
    xmin, xmax, ymin, ymax = 1000, 0, 1000, 0
    for eachLine in data.splitlines():
        splitLine = eachLine.split(', ')
        coordinates.add((int(splitLine[0]), int(splitLine[1])))
        coordinateData[f"{int(splitLine[0])},{int(splitLine[1])}"] = 0
        coordinateData2[f"{int(splitLine[0])},{int(splitLine[1])}"] = 0
    for eachCoord in coordinates:
        if eachCoord[0] > xmax:
            xmax = eachCoord[0]
        elif eachCoord[0] < xmin:
            xmin = eachCoord[0]
        if eachCoord[1] > ymax:
            ymax = eachCoord[1]
        elif eachCoord[1] < ymin:
            ymin = eachCoord[1]
    def _absDistance(firstCoord, secondCoord):
        return abs(firstCoord[0] - secondCoord[0]) + abs(firstCoord[1] - secondCoord[1])
    startingGrid = set()
    for eachX in range(xmin, xmax):
        for eachY in range(ymin, ymax):
            startingGrid.add((eachX, eachY))
    for eachCoord in startingGrid:
        closestCoordDistance = 400
        currentClosest = None
        for eachLocation in coordinates:
            distance = _absDistance(eachCoord, eachLocation)
            if distance < closestCoordDistance:
                closestCoordDistance = distance 
                currentClosest = eachLocation 
            elif distance == closestCoordDistance:
                currentClosest = 'multiple'
        if currentClosest != 'multiple':
            coordinateData[f"{currentClosest[0]},{currentClosest[1]}"] += 1
    startingGrid2 = set()
    for eachX in range(0, 400):
        for eachY in range(0, 400):
            startingGrid2.add((eachX, eachY))
    for eachCoord in startingGrid2:
        closestCoordDistance = 400
        currentClosest = None
        for eachLocation in coordinates:
            distance = _absDistance(eachCoord, eachLocation)
            if distance < closestCoordDistance:
                closestCoordDistance = distance 
                currentClosest = eachLocation 
            elif distance == closestCoordDistance:
                currentClosest = 'multiple'
        if currentClosest != 'multiple':
            coordinateData2[f"{currentClosest[0]},{currentClosest[1]}"] += 1
    winnerwinnerchickendinner = 0
    for eachKey in coordinateData.keys():
        if coordinateData[eachKey] == coordinateData2[eachKey]:
            if coordinateData[eachKey] > winnerwinnerchickendinner:
                winnerwinnerchickendinner = coordinateData[eachKey]
    return winnerwinnerchickendinner


def part2(data):
    totalArea = 0
    coordinates = set()
    for eachLine in data.splitlines():
        splitLine = eachLine.split(', ')
        coordinates.add((int(splitLine[0]), int(splitLine[1])))
    startingGrid = set()
    for eachX in range(0, 400):
        for eachY in range(0, 400):
            startingGrid.add((eachX, eachY))
    def _absDistance(firstCoord, secondCoord):
        return abs(firstCoord[0] - secondCoord[0]) + abs(firstCoord[1] - secondCoord[1])
    for eachCoord in startingGrid:
        totalDistance = 0
        for eachLocation in coordinates:
            totalDistance += _absDistance(eachCoord, eachLocation)
        if totalDistance < 10000:
            totalArea += 1
    return totalArea


