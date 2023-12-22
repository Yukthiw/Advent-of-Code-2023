import re
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def parse_game(line):
    match = re.search(r'Game (\d+): (.+)', line)
    line = match.group(2)

    games = line.split(';')

    max_blue, max_red, max_green = 0, 0, 0
    for game in games:
        blue, red, green = grab(game)
        max_blue = max(max_blue, blue)
        max_red = max(max_red, red)
        max_green = max(max_green, green)

    return max_blue*max_red*max_green


def grab(game):
    blue = int(re.search('(\d+) blue', game).group(1)) if re.search(
        '(\d+) blue', game) else 0
    red = int(re.search('(\d+) red', game).group(1)) if re.search(
        '(\d+) red', game) else 0
    green = int(re.search('(\d+) green', game).group(1)) if re.search(
        '(\d+) green', game) else 0

    return (blue, red, green)


def main():
    power_count = 0
    with open("Day2/input.txt", "r") as f:
        for line in f:
            power_count += parse_game(line)

    return print(power_count)


main()
