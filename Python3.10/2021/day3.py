import aocd

aocd_data = aocd.get_data(day=3, year=2021).splitlines()

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

"""
def part2(data):
    oxygen = data
    for i in range(len(data[0])):
        oxygen = remove_rows(oxygen, i)
    return oxygen
"""

def oxygen_generator_rating(data: list) -> int:
    for i in range(len(data[0])):
        data = remove_rows(data, i)
    return int(data[0], 2)

def remove_rows(existing_list: list, column: int) -> list:
    new_list = []
    zeros = 0
    ones = 0
    lookingfor = ''
    for k in range(len(existing_list)):
        if existing_list[k][column] == '0':
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        lookingfor = '0'
    else:
        lookingfor = '1'
    for k in range(len(existing_list)):
        if existing_list[k][column] == lookingfor:
            new_list.append(existing_list[k])
    return new_list

        
                
