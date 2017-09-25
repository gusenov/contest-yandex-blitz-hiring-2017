def s(n):
    digsum = 0
    while n > 0:
        r = n % 10
        n = int(n / 10)
        digsum += r
    return digsum


lim = int(pow(2, 24))
arr = [True] * (lim + 1)

k = 1
while k < lim:
    numerator = 3 * k
    ds = s(k)
    denominator = ds * ds
    if numerator % denominator == 0:
        n = int(numerator / denominator)
        # print('3 * %d / S(%d)^2 = %d / %d^2 = %d / %d = %d' % (k, k, numerator, ds, numerator, denominator, n))
        if n <= lim:
            arr[n] = False
    k += 1

j = 1
while j < lim:
    if arr[j]:
        print(j) # 61
        break
    j += 1
