#Calculate the area of a room

def main():
    length = float(input("What is the length?  "))
    width = float(input("What is the Width?  "))
    area_result = calculate_area(length, width,)
    print(f"The area is: {area_result:.2f}")


def calculate_area(length, width):
    return length * width

main()
