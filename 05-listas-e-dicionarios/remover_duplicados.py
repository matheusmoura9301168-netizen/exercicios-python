# Remove elementos repetidos mantendo a ordem.

nums = list(map(int, input().split()))
print(list(dict.fromkeys(nums)))
