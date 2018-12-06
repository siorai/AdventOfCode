def part1(data):
    totalSquareFeet = 0
    for eachPresent in data.splitlines():
        l, w, h = eachPresent.split('x')
        l, w, h = int(l), int(w), int(h)
        slack = min(l * w, w * h , h * l)
        l, w, h = 2 * l * w, 2 * w * h, 2 * h * l
        totalSquareFeet += l + w + h + slack
    return totalSquareFeet


def part2(data):
    totalRibbon = 0
    for eachPresent in data.splitlines():
        presentRibbon = 0
        l, w, h = eachPresent.split('x')
        l, w, h = int(l), int(w), int(h)
        bow = l * w * h 
        sides = [ l, w, h ]
        sides.remove(max(sides))
        for eachSide in sides:
            presentRibbon += eachSide * 2
        presentRibbon += bow 
        totalRibbon += presentRibbon 
    return totalRibbon


