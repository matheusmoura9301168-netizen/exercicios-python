# Troca as chaves pelos valores de um dicionário.

# entrada exemplo: "a:1 b:2 c:3"
pairs = input().split()
d = {}
for x in pairs:
    if ':' in x:
        k, v = x.split(':', 1)
        d[k] = v
print({v: k for k, v in d.items()})
