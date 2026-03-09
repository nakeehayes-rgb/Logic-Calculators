#This is technique is called Modular Programming


def run_payroll():
    hours_worked = float(input("How many hours did you work?  "))
    hourly_rate = float(input("What is your hourly pay?  "))
    total_pay = calculate_gross_pay(hours_worked , hourly_rate)
    print(f"Your gross pay is ${total_pay:.2f}. ")


def calculate_gross_pay(hours_worked, hourly_rate):
    return hours_worked * hourly_rate

run_payroll()


