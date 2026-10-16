# Conta vogais e consoantes.

t = input().lower()
v = 'aeiou'
vogais = sum(1 for c in t if c in v)
consoantes = sum(1 for c in t if c.isalpha() and c not in v)
print(vogais, consoantes)
