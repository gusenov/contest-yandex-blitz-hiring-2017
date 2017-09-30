import sys

DEBUGGING = False


def printfield(f):
    print("Минное поле:")
    for r in f:
        print(r)


def check(f, r, c):
    if f[r][c] != 1:
        f[r][c] = 1
        if r - 1 >= 0:
            check(f, r - 1, c)  # сверху
        if r + 1 < len(f):
            check(f, r + 1, c)  # снизу
        if c - 1 >= 0:
            check(f, r, c - 1)  # слева
        if c + 1 < len(f[r]):
            check(f, r, c + 1)  # справа


def check2(f, r, c):
    if (r < 0) or (r >= len(f)) or (c < 0) or (c >= len(f[r])):
        return
    elif f[r][c] == 0:
        f[r][c] = 1
        return check2(f, r - 1, c), check2(f, r + 1, c), check2(f, r, c - 1), check2(f, r, c + 1)


def check3(f, r, c):
    cells = [(r, c)]
    while len(cells) > 0:
        r, c = cells.pop()
        if (r >= 0) and (r < len(f)) and (c >= 0) and (c < len(f[r])):
            if f[r][c] == 0:
                f[r][c] = 1
                cells.append((r - 1, c))
                cells.append((r + 1, c))
                cells.append((r, c - 1))
                cells.append((r, c + 1))


def main():
    if DEBUGGING:
        # inf = open("a-example-1.txt")  # 2
        # inf = open("a-example-2.txt")  # 1
        inf = open("a-my-example-3.txt")
    else:
        inf = sys.stdin

    n, m = map(int, inf.readline().split(" "))

    rowscnt, colscnt = n, m
    f = [[0 for x in range(colscnt)] for y in range(rowscnt)]

    if DEBUGGING:
        printfield(f)

    k = int(inf.readline())
    for i in range(0, k):
        r, c = map(int, inf.readline().split(" "))
        f[r - 1][c - 1] = 1
        if DEBUGGING:
            print(r, c)

    if DEBUGGING:
        printfield(f)

    answer = 0
    for r in range(0, rowscnt):
        for c in range(0, colscnt):
            if f[r][c] == 0:
                answer += 1
                check3(f, r, c)

    if DEBUGGING:
        printfield(f)

    print(answer)


# if __name__ == "__main__":
main()
