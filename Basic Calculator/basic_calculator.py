def main():
    expression = input("Expressions:  ")
    x_str, operator, z_str = expression.split(" ")
    x = int(x_str)
    z = int(z_str)

    if operator == "+":
        result = float(x + z)
    elif operator == "-":
        result = float(x - z)
    elif operator == "*":
        result = float(x * z)
    elif operator == "/":
        result = float(x / z)

    print(f"{result:.1f}")

main()
