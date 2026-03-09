# How much will gas cost based on distance and price per mile

def main():
    distance = float(input("Distance by miles:  "))
    price = float(input("Price per mile:  "))
    cost_of_gas = convert(distance, price)
    print(f" You'll spend approximatley: {cost_of_gas} in gas.")

def convert(miles, price_of_gas):
    total = miles * price_of_gas
    return total
main()
