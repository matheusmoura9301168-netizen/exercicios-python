# Depósitos, levantamentos e saldo.

s=0
while True:
 op=input()
 if op=='d':s+=float(input())
 elif op=='r':s-=float(input())
 elif op=='s':print(s);break
