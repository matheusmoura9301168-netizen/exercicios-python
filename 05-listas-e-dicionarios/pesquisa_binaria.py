# Pesquisa binária numa lista ordenada.

a = list(map(int, input().split()))  # lista ordenada
x = int(input())
l, r = 0, len(a) - 1
pos = -1
while l <= r:
    m = (l + r) // 2
    if a[m] == x:
        pos = m
        break
    elif a[m] < x:
        l = m + 1
    else:
        r = m - 1
print(pos)
