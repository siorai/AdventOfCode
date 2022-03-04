import aocd

aocd_data = aocd.get_data(day=3, year=2021)
data_split = aocd_data.splitlines()

def part1(data):
    gammabit = ''
    epsilonbit = ''
    for i in range(len(data[0])):
        zeros = 0
        for k in range(len(data)):
            if data[k][i] == '0':
                zeros += 1
        if int(zeros) > 500:
            gammabit = gammabit + '0'
            epsilonbit = epsilonbit + '1'
        else:
            gammabit = gammabit + '1'
            epsilonbit = epsilonbit + '0'
    return int(gammabit, 2) * int(epsilonbit, 2)

