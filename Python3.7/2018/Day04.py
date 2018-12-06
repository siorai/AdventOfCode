def part1():
    guardData = {}
    guardNumber = ''
    for eachEntry in dataList:
        minutes = re.split(r':|]', eachEntry)[1]
        if 'Guard' in eachEntry:
            guardNumber = re.split(r'#| begins', eachEntry)[1]
            if guardNumber not in guardData.keys():
                guardData[guardNumber] = []
            continue 
        if 'falls asleep' in eachEntry:
            guardData[guardNumber].append(f'asleep at {minutes}')
        if 'wakes up' in eachEntry:
            guardData[guardNumber].append(f'wakes at {minutes}')
    guardTotal = {}
    guardSleepMinutes = 0
    for eachGuard in guardData.keys():
        minuteCounter = 0
        for eachLog in guardData[eachGuard]:
            minuteTime = int(eachLog.split(' ')[2])
            if 'asleep' in eachLog:
                minuteCounter -= minuteTime 
            if 'wakes' in eachLog:
                minuteCounter += minuteTime 
        guardTotal[eachGuard] = minuteCounter 
    mostAsleep = max(guardTotal, key=lambda k: guardTotal[k])
    guardSleptFrom = {}
    for eachMinute in range(0, 60):
        guardSleptFrom[eachMinute] = 0
    guardAwake = True
    for eachLog in guardData[mostAsleep]:
        minuteCounter = 0
        logMinute = int(eachLog.split(' ')[2])
        while minuteCounter < 60:
            if minuteCounter == logMinute:
                if 'asleep' in eachLog:
                    guardAwake = False 
                if 'wakes' in eachLog:
                    guardAwake = True
            if guardAwake == True:
                guardSleptFrom[minuteCounter] -= 1
            if guardAwake == False:
                guardSleptFrom[minuteCounter] += 1
            minuteCounter += 1
    mostAsleepHour = max(guardSleptFrom, key=lambda k: guardSleptFrom[k])
    return int(mostAsleep) * mostAsleepHour 





def part2():
    guardData = {}
    guardNumber = ''
    for eachEntry in dataList:
        minutes = re.split(r':|]', eachEntry)[1]
        if 'Guard' in eachEntry:
            guardNumber = re.split(r'#| begins', eachEntry)[1]
            if guardNumber not in guardData.keys():
                guardData[guardNumber] = []
            continue 
        if 'falls asleep' in eachEntry:
            guardData[guardNumber].append(f'asleep at {minutes}')
        if 'wakes up' in eachEntry:
            guardData[guardNumber].append(f'wakes at {minutes}')
    guardTotal = {}
    guardSleepMinutes = 0
    guardSleepSchedule = {}
    guardsAsleep = []
    for eachGuard in guardData.keys():
        guardSleptFrom = {}
        for eachMinute in range(0, 60):
            guardSleptFrom[eachMinute] = 0
        guardAwake = True
        for eachLog in guardData[eachGuard]:
            minuteCounter = 0
            logMinute = int(eachLog.split(' ')[2])
            while minuteCounter < 60:
                if minuteCounter == logMinute:
                    if 'asleep' in eachLog:
                        guardAwake = False 
                    if 'wakes' in eachLog:
                        guardAwake = True
                if guardAwake == True:
                    guardSleptFrom[minuteCounter] -= 1
                if guardAwake == False:
                    guardSleptFrom[minuteCounter] += 1
                minuteCounter += 1
        guardSleepSchedule[eachGuard] = guardSleptFrom 
    highestMinute = 0
    highestGuard = ''
    highestMinuteTime = 0
    for eachGuard in guardSleepSchedule.keys():
         guardMax = max(guardSleepSchedule[eachGuard].values())
         if guardMax > highestMinute:
             print(guardMax, int(eachGuard))
             highestMinute = guardMax 
             highestGuard = int(eachGuard)
             highestMinuteTime = max(guardSleepSchedule[eachGuard], key=lambda k: guardSleepSchedule[eachGuard][k])
    return highestMinuteTime * highestGuard 
