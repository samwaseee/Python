coefs = list(map(float, input("Enter the coefficients of the polynomial separated by spaces: ").strip().split()))
a, b = map(float, input("Enter the interval [a, b] separated by a space: ").strip().split())



def func(x):
    result = 0
    degree = len(coefs) - 1
    for coef in coefs:
        result += coef * (x ** degree)
        degree -= 1
    return result

if func(a) * func(b) >= 0:
    print("The bisection method requires that f(a) and f(b) have opposite signs.")
    exit()

def bisection(a,b, tol=1e-5):
    while True:
        c = (a + b) / 2
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
        if abs(b - a) < tol:
            break
    return (a + b) / 2

print(f"The root is approximately: {bisection(a, b)}")
