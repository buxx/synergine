from math import degrees, acos, sqrt

def get_degree_from_north(a, b):
    ax, ay = a[1], a[2]
    bx, by = b[1], b[2]
    Dx, Dy = ax, ay-1
    ab = sqrt((bx-ax)**2 + (by-ay)**2)
    aD = sqrt((Dx-ax)**2 + (Dy-ay)**2)
    Db = sqrt((bx-Dx)**2 + (by-Dy)**2)

    degs = degrees(acos( ( ab**2 + aD**2 - Db**2 ) / ( 2 * ab * aD ) ))
    if bx < ax:
        return 360 - degs
    return degs
