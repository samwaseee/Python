def poly_eval(coeffs, x):
    res = coeffs[0]
    for c in coeffs[1:]:
        res = res * x + c
    return res

def poly_deriv(coeffs):
    n = len(coeffs) - 1
    if n == 0:
        return [0.0]
    dcoeffs = [(n - i) * coeffs[i] for i in range(n)]
    return dcoeffs

def newton_raphson(coeffs, x0, tol=1e-5, max_iter=100):
    f = lambda x: poly_eval(coeffs, x)
    df_coeffs = poly_deriv(coeffs)
    df = lambda x: poly_eval(df_coeffs, x)
    x = float(x0)
    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(dfx) < 1e-10:
            raise ValueError("Derivative is zero")
        delta = fx / dfx
        x_new = x - delta
        if abs(delta) < tol:
            return round(x_new, 3) 
        x = x_new
    raise ValueError("Did not converge")

def synthetic_divide(coeffs, root):
    new_coeffs = []
    accum = coeffs[0]
    new_coeffs.append(accum)
    for coef in coeffs[1:]:
        accum = accum * root + coef
        new_coeffs.append(accum)
    remainder = new_coeffs.pop()
    return new_coeffs, remainder

if __name__ == "__main__":
    coeffs = [1.0, 0.0, -6.0, 4.0] 
    roots = []

    try:
        r1 = newton_raphson(coeffs, -3.0)
        roots.append(r1)
        coeffs, rem = synthetic_divide(coeffs, r1)
        print(f"First root: {r1}, Remainder: {rem:.2e}")
    except ValueError as e:
        print(e)

    try:
        r2 = newton_raphson(coeffs, 0.0)
        roots.append(r2)
        coeffs, rem = synthetic_divide(coeffs, r2)
        print(f"Second root: {r2}, Remainder: {rem:.2e}")
    except ValueError as e:
        print(e)

    if len(coeffs) == 2:
        r3 = round(-coeffs[1] / coeffs[0], 3)
        roots.append(r3)
        print(f"Third root: {r3}")


    roots.sort()
    print("\nRoots correct to 3 decimal places:")
    for root in roots:
        print(root)