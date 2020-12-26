import math
geo_figura = input()
if geo_figura == "square":
    a = float(input())
    litse = a * a
    print(f"{litse:.3f}")
elif geo_figura == "rectangle":
    a = float(input())
    b = float(input())
    litse = a * b
    print(f"{litse:.3f}")
elif geo_figura == "circle":
    r = float(input())
    litse = math.pi * r * r
    print(f"{litse:.3f}")
elif geo_figura == "triangle":
    a = float(input())
    h = float(input())
    litse = a * h / 2
    print(f"{litse:.3f}")

