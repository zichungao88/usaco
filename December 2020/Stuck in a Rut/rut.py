# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    cows = []
    step = []
    eaten = [0] * n
    moving = [True] * n

    for i in range(n):
        direction, x, y = input().split()
        x = int(x)
        y = int(y)
        cows.append((direction, [x, y]))

    while True:
        position = []
        for i in range(n):
            if not moving[i]:
                continue
            if cows[i][0] == 'E':
                position.append([cows[i][1][0] + 1, cows[i][1][1]])
                cows[i][1][0] += 1
            else:
                position.append([cows[i][1][0], cows[i][1][1] + 1])
                cows[i][1][1] += 1
            eaten[i] += 1
            if cows[i][1] in step:
                moving[i] = False
        step.extend(position)
        if max(eaten) > 100:
            for i in range(n):
                if eaten[i] == 101:
                    eaten[i] = 'Infinity'
            for i in eaten:
                print(i)
            break


if __name__ == "__main__":
    main('rut')
