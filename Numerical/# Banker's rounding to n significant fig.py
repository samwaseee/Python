# Banker's rounding to n significant figures
def round_banker(num, n):
    from decimal import Decimal, ROUND_HALF_EVEN
    if num == 0:
        return 0
    d = Decimal(str(num))
    shift = n - d.adjusted() - 1
    rounded = d.scaleb(shift).quantize(Decimal('1'), rounding=ROUND_HALF_EVEN).scaleb(-shift)
    return float(rounded)

num = float(input("Enter a number: "))
n = int(input("Enter significant figures: "))
print("Rounded:", round_banker(num, n))