import re

def part1(data):
    niceString = 0
    naughtyList = ['ab', 'cd', 'pq', 'xy']
    doubleList = []
    for eachChar in range(0,26):
        doubleList.append(f"{chr(ord('a') + eachChar)}{chr(ord('a') + eachChar)}")
    vowels = ['a','e','i','o','u']
    for eachLine in data.splitlines():
        Naughty = True
        Double = False
        vowelCount = 0
        for eachLetter in eachLine:
            if eachLetter in vowels:
                vowelCount += 1
        for eachDouble in doubleList:
            if eachDouble in eachLine:
                Double = True 
        if vowelCount >= 3 and Double == True:
            Naughty = False
        for eachNaught in naughtyList:
            if eachNaught in eachLine:
                Naughty = True
        if Naughty == False:
            niceString += 1
    return niceString



def part2(data):
    niceString = 0
    for eachLine in data:
        if re.search(r"(..).*\1", eachLine) and re.search(r"(.).\1", eachLine):
            niceString += 1
    return niceString

