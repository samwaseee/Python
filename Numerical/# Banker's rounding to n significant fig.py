def round_banker(num, n):
    if num == 0:
        return 0
    import math

    sign = -1 if num < 0 else 1
    num = abs(num)
    order = int(math.floor(math.log10(num)))
    factor = 10 ** (n - 1 - order)
    shifted = num * factor

    # Banker's rounding (round half to even)
    int_part = int(shifted)
    frac_part = shifted - int_part

    if frac_part > 0.5:
        int_part += 1
    elif frac_part == 0.5:
        if int_part % 2 != 0:
            int_part += 1
    # else: int_part stays the same

    rounded = int_part / factor
    return sign * rounded

num = float(input("Enter a number: "))
n = int(input("Enter significant figures: "))
print("Rounded:", round_banker(num, n))