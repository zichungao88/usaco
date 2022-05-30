# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    cows = []
    for i in range(n):
        count = 0
        x, y = [int(i) for i in input().split()]
        cows.append((x, y))
        if i >= 3:
            for j in cows:
                if (j[0] - 1, j[1]) in cows and (j[0], j[1] - 1) in cows and (j[0], j[1] + 1) in cows and (j[0] + 1, j[1]) not in cows:
                    count += 1
                elif (j[0] + 1, j[1]) in cows and (j[0], j[1] - 1) in cows and (j[0], j[1] + 1) in cows and (j[0] - 1, j[1]) not in cows:
                    count += 1
                elif (j[0], j[1] - 1) in cows and (j[0] - 1, j[1]) in cows and (j[0] + 1, j[1]) in cows and (j[0], j[1] + 1) not in cows:
                    count += 1
                elif (j[0], j[1] + 1) in cows and (j[0] - 1, j[1]) in cows and (j[0] + 1, j[1]) in cows and (j[0], j[1] - 1) not in cows:
                    count += 1
        print(count)


if __name__ == "__main__":
    main('comfortable')
