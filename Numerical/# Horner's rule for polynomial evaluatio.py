def horner(coeffs, x):
    result = coeffs[0]
    print(f"P3 = {result}")
    for i, c in enumerate(coeffs[1:], 1):
        result = result * x + c
        print(f"P{3-i}: {result}")
    return result

coeffs = [1, -2, 5, 10]  
x = 5
final_result = horner(coeffs, x)
print("f(5) =", final_result)