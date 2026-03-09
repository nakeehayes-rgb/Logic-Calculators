#This Calculator is used to calculate the sales tax on a prodcut


def run_calculator():
    base_price = float(input("What is the cost of the product?  "))
    tax_rate = float(input("What is the State Sales Tax?  "))
    total = get_total_with_tax(base_price, tax_rate)
    print(f"The total cost is {total}")

def get_total_with_tax(base_price, tax_rate):
    return base_price + (base_price, tax_rate)

run_calculator()
