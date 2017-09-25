import sys

# inf = sys.stdin
# inf = open("с-example-1.txt")
# inf = open("с-example-2.txt")
inf = open("с-my-example-3.txt")

table = {}


def lenstr(o):
    return str(len(str(o)))


def printsep(firstlen, secondlen, teams, lastlen):
    print("+" + ("-" * int(firstlen)) + "+" + ("-" * int(secondlen)), end='')
    while teams > 0:
        print("+-", end='')
        teams -= 1
    print("+" + ("-" * int(lastlen)) + "+-+\n", end='')


def save(ta, tb, a, b):
    if ta not in table:
        table[ta] = {"name": ta}
    if "points" not in table[ta]:
        table[ta]["points"] = 0
    if "wins" not in table[ta]:
        table[ta]["wins"] = 0
    table[ta][ta] = "X"
    if a == b:
        table[ta][tb] = "D"
        table[ta]["points"] += 1
    elif a > b:
        table[ta][tb] = "W"
        table[ta]["points"] += 3
        table[ta]["wins"] += 1
    elif a < b:
        table[ta][tb] = "L"


for line in inf:
    line = line.rstrip()
    ta, tb, ab = line.split(" - ")
    a, b = map(int, ab.split(":"))
    save(ta, tb, a, b)
    save(tb, ta, b, a)

teams = sorted(table.keys())
teamslen = len(teams)


places = sorted([table[t] for t in teams], key=lambda t: (t['points'], t['wins']), reverse=True)
placeno = 1
pointsprev = None
winsprev = None
for team in places:
    name = team["name"]
    points = team["points"]
    wins = team["wins"]
    if pointsprev is None and winsprev is None:
        table[name]["place"] = placeno
        pointsprev = points
        winsprev = wins
        continue
    if points == pointsprev and wins == winsprev:
        table[name]["place"] = placeno
        continue
    placeno += 1
    if placeno > 3:
        break
    table[name]["place"] = placeno
    pointsprev = points
    winsprev = wins


maxpoints = max([table[t]["points"] for t in teams])

nolen = lenstr(teamslen)
namelen = str(max([len(t) for t in teams]) + 1)
pointslen = lenstr(maxpoints)

printsep(nolen, namelen, teamslen, pointslen)

no = 1
for ta in teams:
    print(("|{:>" + nolen + "}|{:" + namelen + "}|").format(no, ta), end='')
    for tb in teams:
        result = table[ta][tb] if tb in table[ta] else " "
        print("{}|".format(result), end='')
    points = table[ta]["points"] if "points" in table[ta] else 0
    print(("{:>" + pointslen + "}|").format(points), end='')
    place = table[ta]["place"] if "place" in table[ta] else " "
    print("{}|\n".format(place), end='')

    printsep(nolen, namelen, teamslen, pointslen)

    no += 1
