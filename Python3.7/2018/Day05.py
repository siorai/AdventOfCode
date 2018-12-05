def part1(data):
    existingString = None
    while existingString != data:
        existingString = data
        for eachLetter in range(0, 26): 
            data = data.replace(chr(ord("a") + eachLetter) + chr(ord("A") + eachLetter), '')
            data = data.replace(chr(ord("A") + eachLetter) + chr(ord("a") + eachLetter), '')
    return data


def part2(data):
    currentWinner = len(data)
    for eachLetter in range(0, 26):
        subString = data.replace(chr(ord("a") + eachLetter), '').replace(chr(ord("A") + eachLetter),'')
        shorten = len(part1(subString))
        if shorten < currentWinner:
            currentWinner = shorten
    return currentWinner
