import sys

def poly_derivative_eval(coeffs, x):
    n = len(coeffs) - 1
    if n == 0:
        return 0
    deriv_coeffs = [coeffs[i] * (n - i) for i in range(n)]
    result = deriv_coeffs[0]
    for c in deriv_coeffs[1:]:
        result = result * x + c
    return result

while True:
    try:
        x = int(input())
        coeffs = list(map(int, input().split()))
        print(poly_derivative_eval(coeffs, x))
    except EOFError:
        break