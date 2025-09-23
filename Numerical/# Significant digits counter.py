# Significant digits counter
def count_significant_digits(num_str):
    num_str = num_str.strip().lstrip('0')
    if '.' in num_str:
        num_str = num_str.rstrip('0').replace('.', '')
    else:
        num_str = num_str.rstrip('0')
    return len(num_str)

num = input("Enter a number: ")
print("Significant digits:", count_significant_digits(num))