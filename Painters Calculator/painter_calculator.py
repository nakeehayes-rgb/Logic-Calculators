# help a painter estimate costs # area(h*w) area* square footage

def main():
    h = float(input("Height:  "))
    w = float(input("Width:  "))
    cost = float(input("Cost per square footage:  "))
    area = convert(cost, h, w)
    print(f"The total amount you should charge is:{area: .2f}.")

def convert(amount, height, width):
    total_area = amount * (height * width)
    return total_area

main()
