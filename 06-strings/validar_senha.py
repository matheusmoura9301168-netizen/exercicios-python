# Verifica se uma senha é forte.

s = input().strip()
val = (
    len(s) >= 8
    and any(c.isdigit() for c in s)
    and any(c.isupper() for c in s)
    and any(c.islower() for c in s)
)
print(val)
