# Filtra os números maiores que um valor.

nums = list(map(int, input().split()))
x = int(input())
print([n for n in nums if n > x])
