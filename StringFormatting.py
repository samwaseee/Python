price = 49

txt = f"The price is {price} dollars"

print(txt)

# The f-string (formatted string literal) is a way to format strings in Python. It allows you to embed expressions inside string literals, using curly braces {}.

txt = f"The price is {95:.2f} dollars"
print(txt)

txt = f"The price is very {'expensive' if price > 50 else 'cheap'}"
print(txt)