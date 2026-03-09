#Calculate the shipping cost of a purchase

def main():
    item_cost = int(input("Enter the numeric value of this item:  "))
    total = add_shipping(item_cost)
    print(f"Including shipping, your total is {total}")

def add_shipping(item_cost):
    return item_cost + 5


main()
