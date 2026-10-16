# Codifica um texto deslocando cada carácter 3 posições.

s = input()
print(''.join(chr(ord(c) + 3) for c in s))
