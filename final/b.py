import sys

DEBUGGING = True
inputdata = {}


class NodeLabel:
    LEAF_VICTORY, LEAF_DEFEAT, LEAF_NEUTRAL, NOT_LEAF = range(4)


class Turn:
    FIRST, SECOND = range(2)


def getnodelabel(s, i):
    if s[i] == '+':
        return NodeLabel.LEAF_VICTORY
    elif s[i] == '-':
        return NodeLabel.LEAF_DEFEAT
    elif s[i] == '0':
        return NodeLabel.LEAF_NEUTRAL
    elif s[i] == '.':
        return NodeLabel.NOT_LEAF


def printedges(e):
    print("Матрица:")
    for u in e:
        print(u)


def isedge(e, u, v):
    if (e[u][v] == 1):
        return True
    return False


def move(turn, curnode):
    # Входные данные, чтобы не тянут их через аргументы функции:
    n = inputdata["n"]
    edges = inputdata["edges"]
    s = inputdata["str"]

    if getnodelabel(s, curnode) == NodeLabel.LEAF_VICTORY:  # Если находимся на листе-победе:

        if curnode == 0:  # Если текущий лист первый, то сейчас очередь первого игрока
            return "First"  # и соответственно он побеждает.

        elif turn == Turn.FIRST:  # Иначе если сейчас ход первого игрока, то это означает, что на текущий лист
            return "Second"  # сделал ход второй игрок и соответственно он побеждает.

        elif turn == Turn.SECOND:  # Иначе если сейчас ход второго игрока, то это означает, что на текущий лист
            return "First"  # сделал ход первый игрок и соответственно он побеждает.

    elif getnodelabel(s, curnode) == NodeLabel.LEAF_DEFEAT:  # Если находимся на листе-поражении:

        # Вывод в зависимости от того, кто выиграет!

        if curnode == 0:  # Если текущий лист первый, то сейчас очередь первого игрока
            return "Second"  # и соответственно он проигрывает.

        elif turn == Turn.FIRST:  # Иначе если сейчас ход первого игрока, то это означает, что на текущий лист
            return "First"  # сделал ход второй игрок и соответственно он проигрывает.

        elif turn == Turn.SECOND:   # Иначе если сейчас ход второго игрока, то это означает, что на текущий лист
            return "Second"  # сделал ход первый игрок и соответственно он проигрывает.

    elif getnodelabel(s, curnode) == NodeLabel.LEAF_NEUTRAL:  # Если находимся на нейтральном листе, то ходов нет
        return "Draw"  # и соответственно наступает ничья.

    elif getnodelabel(s, curnode) == NodeLabel.NOT_LEAF:  # Если узел не является листом, то можно сделать ход:
        for i in range(0, n):  # Делаем обход
            if edges[curnode][i] == 1:  # всех потомков узла на котором сейчас находимся:

                if turn == Turn.FIRST:
                    move(Turn.SECOND, i)
                elif turn == Turn.SECOND:
                    move(Turn.FIRST, i)

def main():
    if DEBUGGING:
        inf = open("b-example-1.txt")  # First
        # inf = open("b-example-2.txt")  # Draw
    else:
        inf = sys.stdin

    n, k = map(int, inf.readline().split(" "))
    inputdata["n"] = n
    inputdata["k"] = k
    s = inf.readline().rstrip()
    inputdata["str"] = s

    if DEBUGGING:
        print("Количество вершин:", n)
        print("Глубина, на которой можно сделать «реверс»:", k)
        print("Строка из", n, "символов:", s)
        assert len(s) == n
        print("Ребра дерева:")

    edges = [[0 for v in range(n)] for u in range(n)]

    for i in range(0, n - 1):
        u, v = map(int, inf.readline().split(" "))
        edges[u - 1][v - 1] = 1
        if DEBUGGING:
            print(u, v)
            assert isedge(edges, u - 1, v - 1)

    if DEBUGGING:
        printedges(edges)

    inputdata["edges"] = edges

    move(Turn.FIRST, 0)

# if __name__ == "__main__":
main()
