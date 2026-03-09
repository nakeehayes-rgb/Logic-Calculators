# Python Logic & Syntax Calculator

A highly readable logic engine designed to evaluate Boolean operations, control flow structures, and functional logic. Built with a focus on clean code and logical transparency.

## ⚡ Core Features
*   **Boolean Operations**: Full support for `AND`, `OR`, and comparison operators (`==`, `!=`).
*   **Control Flow**: Simulation of `if`, `elif`, and `else` conditional logic.
*   **Looping Logic**: Handles iterative processes and repeated logical evaluations.
*   **Function Definitions**: Supports `def` blocks and the `return` statement for modular logic.
*   **Clean Code Architecture**: Designed specifically for readability and easy debugging.

## 🛠️ Logic Overview
The calculator processes logic in a way that mirrors Python’s native syntax:
- **Conditionals**: Evaluates truthiness across nested statements.
- **Functions**: Tracks scope and returns values back to the main caller.
- **Comparisons**: Precise evaluation of equality and inequality.

## 📂 Featured Module: Tax Deduction Calculator
The **Flat Rate Tax Deduction Calculator** demonstrates how the engine processes real-world data using conditional warnings (e.g., minimum wage and overtime checks).

### Logic Implementation
```python
def main():
    hours_worked = float(input("Hours Worked:  "))
    # Conditional logic for work status
    if hours_worked < 40:
        print("You worked overtime this week!")
    else:
        print("standard hours worked")
    
    hourly_rate = float(input("Hourly Rate:  "))
    # Minimum wage safety check
    if hourly_rate < 15:
        print("Warning: This is less than the $15 minimum wage!")
        
    tax = float(input("Flat Rate Tax Amount:  "))
    gross_pay = convert(tax, hours_worked, hourly_rate)
    print(f"Your take home pay is: {gross_pay: .2f}.")

def convert(taxes, hours, hourly):
    # Functional return logic
    results = (hours * hourly) - taxes
    return results

main()



