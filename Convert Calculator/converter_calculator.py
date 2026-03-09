#Convert USD to Euro 

def main():
    amount = float(input("How many US Dollars do you have?  "))
    total_euro = euro_total(amount)
    print(f"You have {total_euro} in Euro's")

def euro_total(amount):
    return amount * 0.85

main()
