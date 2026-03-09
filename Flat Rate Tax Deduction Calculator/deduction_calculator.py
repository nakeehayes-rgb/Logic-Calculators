# Calculate a worker's take-home pay after a flat tax deduction.

def main():
    hours_worked = float(input("Hours Worked:  "))
    if hours_worked < 40:
        print("You worked overtime this week!")
    else:
        print("standard hours worked")
    hourly_rate = float(input("Hourly Rate:  "))
    if hourly_rate < 15:
        print("Warning: This is less than the $15 minimum wage!")
    tax = float(input("Flat Rate Tax Amount:  "))
    gross_pay = convert(tax,hours_worked, hourly_rate)
    print(f"Your take home pay is:{gross_pay: .2f}.")

def convert(taxes, hours, hourly):
    results = (hours * hourly) - taxes
    return results

main()

