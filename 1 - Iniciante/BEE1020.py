d = int(input())

a = d//365
r = d%365

m = r//30
dias = r%30

print(f"{a} ano(s)")
print(f"{m} mes(es)")
print(f"{dias} dia(s)")