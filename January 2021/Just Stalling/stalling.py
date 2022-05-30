# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    cows = [int(i) for i in input().split()]
    stalls = [int(i) for i in input().split()]

    stalls.sort()
    answer = 1
    for i in range(n):
        cow = 0
        for j in range(n):
            if stalls[i] >= cows[j]:
                cow += 1
        cow -= i
        answer *= cow
    print(answer)


if __name__ == "__main__":
    main('stalling')
