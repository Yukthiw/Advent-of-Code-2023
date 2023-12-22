import re
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def parse_game(line):
    match = re.search(r'Game (\d+): (.+)', line)
    id = match.group(1)
    line = match.group(2)

    games = line.split(';')

    for game in games:
        if not check_grab(game):
            return 0

    return int(id)


def check_grab(game):
    blue = int(re.search('(\d+) blue', game).group(1)) if re.search(
        '(\d+) blue', game) else 0
    red = int(re.search('(\d+) red', game).group(1)) if re.search(
        '(\d+) red', game) else 0
    green = int(re.search('(\d+) green', game).group(1)) if re.search(
        '(\d+) green', game) else 0

    if (blue > MAX_BLUE or red > MAX_RED or green > MAX_GREEN):
        return False
    else:
        return True


def main():
    id_count = 0
    with open("Day2/input.txt", "r") as f:
        for line in f:
            id_count += parse_game(line)

    return print(id_count)


main()
