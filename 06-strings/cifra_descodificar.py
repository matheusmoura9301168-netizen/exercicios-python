# Descodifica o texto da cifra anterior.

s = input()
print(''.join(chr(ord(c) - 3) for c in s))
