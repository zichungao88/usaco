# import sys


def main(name):
    # sys.stdin = open(name + '.in', 'r')
    # sys.stdout = open(name + '.out', 'w')

    alphabet = input()
    string = input()
    new_alphabet = ''
    time = 0
    for i in string:
        if i not in new_alphabet:
            time += 1
        j = alphabet.index(i)
        new_alphabet = alphabet[j+1:]
    print(time)


if __name__ == "__main__":
    main('cowphabet')
