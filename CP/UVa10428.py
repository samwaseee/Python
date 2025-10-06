from sys import stdin

def poly_eval(coeffs, x):
    res = coeffs[0]
    for c in coeffs[1:]:
        res = res * x + c
    return res

def poly_deriv(coeffs):
    n = len(coeffs) - 1
    return [coeffs[i] * (n - i) for i in range(n)]

def newton_raphson(coeffs, x0, tol=1e-10, max_iter=100):
    for _ in range(max_iter):
        f = poly_eval(coeffs, x0)
        df = poly_eval(poly_deriv(coeffs), x0)
        if abs(df) < 1e-12:
            x0 += 1e-3  
            continue
        x1 = x0 - f / df
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    return x0

def synthetic_divide(coeffs, root):
    n = len(coeffs)
    new_coeffs = [coeffs[0]]
    for i in range(1, n):
        new_coeffs.append(new_coeffs[-1] * root + coeffs[i])
    return new_coeffs[:-1] 

def solve(coeffs, n):
    roots = []
    temp_coeffs = coeffs[:]
    guesses = [-20, -10, 0, 10, 20]  
    for i in range(n):
        for guess in guesses:
            root = newton_raphson(temp_coeffs, guess)
            if all(abs(root - r) > 1e-5 for r in roots) and abs(root) <= 25.1:
                break
        roots.append(root)
        temp_coeffs = synthetic_divide(temp_coeffs, root)
    roots.sort()
    print(''.join(f' {r:.4f}' for r in roots))

T = 1
for line in stdin:
    if not line.strip():
        continue
    parts = line.strip().split()
    n = int(parts[0])
    if n == 0:
        break
    coeffs = list(map(float, parts[1:]))
    print(f'Equation {T}:', end='')
    solve(coeffs, n)
    T += 1