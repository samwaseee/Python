# Horner's rule for polynomial evaluation
def horner(coeffs, x):
    result = coeffs[0]
    for c in coeffs[1:]:
        result = result * x + c
    return result

coeffs = [1, -2, 5, 10]  # x^3 - 2x^2 + 5x + 10
x = 5
print("f(5) =", horner(coeffs, x))