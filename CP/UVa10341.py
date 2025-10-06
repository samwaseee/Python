import sys
import math

def f(x, p, q, r, s, t, u):
    return p * math.exp(-x) + q * math.sin(x) + r * math.cos(x) + s * math.tan(x) + t * x * x + u

for line in sys.stdin:
    if not line.strip():
        continue
    parts = list(map(float, line.strip().split()))
    if len(parts) != 6:
        continue
    p, q, r, s, t, u = parts
    a, b = 0.0, 1.0
    fa = f(a, p, q, r, s, t, u)
    fb = f(b, p, q, r, s, t, u)
    if abs(fa) < 1e-9:
        print("0.0000")
    elif abs(fb) < 1e-9:
        print("1.0000")
    elif fa * fb > 0:
        print("No solution")
    else:
        for _ in range(100):
            mid = (a + b) / 2
            fm = f(mid, p, q, r, s, t, u)
            if abs(fm) < 1e-7:
                break
            if fa * fm < 0:
                b = mid
                fb = fm
            else:
                a = mid
                fa = fm
        print("{:.4f}".format((a + b) / 2))