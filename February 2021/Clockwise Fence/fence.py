# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    for i in range(n):
        fence = input()
        if fence[0] == 'N':
            if fence[1] == 'E':
                answer = 'CW'
            elif fence[1] == 'W':
                answer = 'CCW'
        elif fence[0] == 'E':
            if fence[1] == 'S':
                answer = 'CW'
            elif fence[1] == 'N':
                answer = 'CCW'
        elif fence[0] == 'S':
            if fence[1] == 'W':
                answer = 'CW'
            elif fence[1] == 'E':
                answer = 'CCW'
        elif fence[0] == 'W':
            if fence[1] == 'N':
                answer = 'CW'
            elif fence[1] == 'S':
                answer = 'CCW'
        print(answer)


if __name__ == "__main__":
    main('fence')
