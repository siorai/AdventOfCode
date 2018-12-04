#for eachTS in data.splitlines():
#    splitUp = re.split(r'\[|-| |]|Guard #|up|falls', eachTS)
#    date = f"{splitUp[2]}-{splitUp[3]}"
#    guard = splitUp[7]
#    if splitUp[7] not in logDict.keys():
#        logDict[splitUp[7]] = {}
#    if splitUp[8] == 'begins':
#        logDict[date].update({'date': date,
#                              'beginsShift': splitUp[4]})
#        continue
#    elif splitUp[8] == 'asleep':
#        logDict[].update({'asleep': splitUp[4]})
#        continue 
#    elif splitUp[6] == 'wakes':
#        logDict[date].update({'wakes': splitUp[4]})
#        continue
#
#
#
#for eachTS in data.splitlines():
#    splitUp = re.split(r'\[|-| |]|Guard #|up|falls', eachTS)
#    date = f"{splitUp[2]}-{splitUp[3]}"
#    if date not in logDict.keys():
#        logDict[date] = {}
#    if splitUp[8] == 'begins':
#        logDict[date].update({'guardNumber': splitUp[7],
#                              'beginsShift': splitUp[4]})
#        continue
#    elif splitUp[8] == 'asleep':
#        logDict[date].update({'asleep': splitUp[4]})
#        continue
#    elif splitUp[6] == 'wakes':
#        logDict[date].update({'wakes': splitUp[4]})
#        continue
#
#for eachEntry in logDict.keys():
#    if 'guardNumber' not in logDict[eachEntry].keys():
#        continue 
#    eachDate = logDict[eachEntry]
#    guardNumber = eachDate['guardNumber']
#    try:
#        minutesAsleep = int(eachDate['wakes'].split(r':')[1]) - int(eachDate['asleep'].split(r':')[1])
#    except KeyError:
#        continue 
#    if guardNumber not in guardStats.keys():
#        guardStats[guardNumber] = 0
#    guardStats[guardNumber] += minutesAsleep
#
#def seeTimes():
#    print("""
#Time: 000000000011111111112222222222333333333344444444445555555555
#      012345678901234567890123456789012345678901234567890123456789
#    """)
#    for eachDate in logDict.keys():
#        try:
#            if logDict[eachDate]['guardNumber'] == '2467':
#                minuteCounter = 0
#                awake = True
#                printingString = f"{eachDate} "
#                asleep = int(logDict[eachDate]['asleep'].split(r':')[1])
#                wakes = int(logDict[eachDate]['wakes'].split(r':')[1])
#                while minuteCounter < 60:
#                    if minuteCounter == asleep:
#                        awake = False
#                    elif minuteCounter == wakes:
#                        awake = True
#                    if awake:
#                        printingString = printingString + "A"
#                    else:
#                        printingString = printingString + "S"
#                    minuteCounter += 1
#                print(printingString)
#        except KeyError:
#            continue
#
#
#                    


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


    
