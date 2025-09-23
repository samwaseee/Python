def synthetic_division(coeffs, r):
    n = len(coeffs)
    q = [coeffs[0]]
    for i in range(1, n-1):
        q.append(coeffs[i] + q[-1]*r)
    rem = coeffs[-1] + q[-1]*r
    return q, rem

coeffs = [1, -5, 10, -8]
q, rem = synthetic_division(coeffs, 2)
print("Quotient coefficients:", q)
print("Remainder:", rem)