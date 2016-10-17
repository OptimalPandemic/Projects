import math, sys


def calculatedigit(n):
    i = 0
    sum_hex = 0
    while i < n:
        sum_hex += math.pow(16, -i) * (4/(8*i+1) - 2/(8*i+4) - 1/(8*i+5) - 1/(8*i+6))
        i += 1

    return str(sum_hex)[:n+2]

j = 1
while j <= int(sys.argv[1]):
    print(calculatedigit(j))
    j += 1

