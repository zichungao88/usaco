# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    cows = [int(i) for i in input().split()]
    even = []
    odd = []

    for i in cows:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if len(even) == len(odd):
        answer = n
    elif len(even) > len(odd):
        answer = len(odd) * 2 + 1
    else:
        if (len(odd) - len(even)) % 3 == 0:
            answer = len(even) * 2 + (len(odd) - len(even)) // 3 * 2
        elif (len(odd) - len(even)) % 3 == 1:
            answer = len(even) * 2 + (len(odd) - len(even)) // 3 * 2 - 1
        else:
            answer = len(even) * 2 + (len(odd) - len(even)) // 3 * 2 + 1
    print(answer)


if __name__ == "__main__":
    main('morephotos')
