import sys

# inf = sys.stdin
# inf = open("a-example-1.txt")  # Petya
inf = open("a-example-2.txt")  # Vasya

n = int(inf.readline())
a = [int(z) for z in inf.readline().rstrip().split()]

psum, vsum = 0, 0
pnum, vnum = 0, 0
pturn = True

idx = 0

while idx < n:
    if pturn:
        pnum = a[idx]
        psum += pnum
        pturn = False
    else:
        vnum = a[idx]
        vsum += vnum
        pturn = True

        if pnum < vnum:
            idx += 1
            psum += a[idx]
        elif vnum < pnum:
            idx += 1
            vsum += a[idx]

    idx += 1

if psum < vsum:
    print("Vasya")
elif vsum < psum:
    print("Petya")
