import hashlib

def part1(data):
    increment = 1
    while True:
        attempt = data + str(increment)
        if hashlib.md5(attempt.encode('utf-8')).hexdigest()[:5] != '00000':
            increment += 1
            pass
        else:
            return attempt


def part2(data):
    increment = 1
    while True:
        attempt = data + str(increment)
        if hashlib.md5(attempt.encode('utf-8')).hexdigest()[:6] != '000000':
            increment += 1
            pass
        else:
            return attempt
