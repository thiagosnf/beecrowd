x1, y1 = [float(x) for x in input().split()]
x2, y2 = [float(x) for x in input().split()]

print(f"{( (x2 - x1)**(2) + (y2 - y1)**(2) ) **(1/2):.4f}")