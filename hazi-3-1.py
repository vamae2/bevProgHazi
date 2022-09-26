def istriangle():
    a = int(input('Give the side of the triangle in cm:\na side (cm): '))
    b = int(input('b side (cm): '))
    c = int(input('c side (cm): '))
    if (a + b > c) and (a + c > b) and (b + c > a):
        print(f"The {a}, {b} and {c} sided triangle is possible.")
    else:
        print(f"The {a}, {b} and {c} sided triangle is NOT possible.")

if __name__ == '__main__':
    istriangle()