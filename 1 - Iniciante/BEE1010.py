p1 = input().split()
c1 = int(p1[0])
n1 = int(p1[1])
v1 = float(p1[2])
t1 = n1 * v1

p2 = input().split()
c2 = int(p2[0])
n2 = int(p2[1])
v2 = float(p2[2])
t2 = n2 * v2

print(f"VALOR A PAGAR: R$ {t1 + t2:.2f}")