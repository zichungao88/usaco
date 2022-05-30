import sys


def find_bessie(cows, name):
    age = 0
    for i in cows:
        if i[0] == name:
            if i[2] == 'younger':
                age -= i[1]
                if i[-1] == 'Bessie':
                    print(age)
                    quit()
                else:
                    name = i[-1]
                    find_bessie(cows, name)
            elif i[2] == 'older':
                age += i[1]
                if i[-1] == 'Bessie':
                    print(age)
                    quit()
                else:
                    name = i[-1]
                    find_bessie(cows, name)


def main(name):
    sys.stdin = open(name + '.in', 'r')
    sys.stdout = open(name + '.out', 'w')

    n = int(input())
    age = []
    zodiac = ['Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat']
    for i in range(n):
        line = input().split()
        age.append(line)

    cows = []
    for i in range(n):
        if age[i][3] == 'previous':
            if i == 0:
                cows.append((age[i][0], 12 - zodiac.index(age[i][4]), 'older', age[i][-1]))
            else:
                if zodiac.index(age[i][4]) > zodiac.index(age[i-1][4]):
                    cows.append((age[i][0], 12 - (zodiac.index(age[i][4]) - zodiac.index(age[i-1][4])), 'older', age[i][-1]))
                else:
                    cows.append((age[i][0], zodiac.index(age[i][4]) - zodiac.index(age[i-1][4]), 'younger', age[i][-1]))
        else:
            if i == 0:
                cows.append((age[i][0], zodiac.index(age[i][4]), 'younger', age[i][-1]))
            else:
                if zodiac.index(age[i][4]) > zodiac.index(age[i-1][4]):
                    cows.append((age[i][0], zodiac.index(age[i][4]) - zodiac.index(age[i-1][4]), 'younger', age[i][-1]))
                else:
                    cows.append((age[i][0], 12 - (zodiac.index(age[i][4]) - zodiac.index(age[i-1][4])), 'older', age[i][-1]))
    print(cows)

    name = 'Elsie'
    find_bessie(cows, name)


if __name__ == "__main__":
    main('year')
