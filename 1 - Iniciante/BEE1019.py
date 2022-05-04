v = int(input())

h = v//3600
r = v%3600

m = r//60
s = r%60

print(f"{h}:{m}:{s}")