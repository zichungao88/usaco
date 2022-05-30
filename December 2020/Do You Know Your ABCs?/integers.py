# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    integers = list(map(int, input().split()))
    answer = []

    for a in integers:
        for b in integers:
            for c in integers:
                if a + b + c == max(integers):
                    x = a + b
                    y = b + c
                    z = a + c
                    if x in integers and y in integers and z in integers:
                        answer.append(a)
                        answer.append(b)
                        answer.append(c)
                        answer.sort()
                        for i in range(len(answer)):
                            if i == (len(answer) - 1):
                                print(answer[i])
                            else:
                                print(answer[i], end=' ')
                        quit()


if __name__ == "__main__":
    main('integers')
