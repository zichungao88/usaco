# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    n = int(input())
    count = 0
    pedals = list(map(int, input().split()))

    for i in range(n):
        for j in range(i, n):
            sliced = pedals[i:j+1]
            average = sum(sliced) / len(sliced)
            if average in sliced:
                count += 1
    print(count)


if __name__ == "__main__":
    main('flowers')
