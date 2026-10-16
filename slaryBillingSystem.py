"""Salary and Billing System using object-oriented programming."""

class Employee:
    def __init__(self, employee_id, name, base_salary):
        if base_salary < 0:
            raise ValueError('Salary cannot be negative.')
        self.employee_id = employee_id
        self.name = name
        self.base_salary = base_salary

    def net_salary(self, bonus=0, deductions=0):
        if bonus < 0 or deductions < 0:
            raise ValueError('Bonus and deductions cannot be negative.')
        return self.base_salary + bonus - deductions


class BillingSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        if price < 0 or quantity <= 0:
            raise ValueError('Price must be nonnegative and quantity positive.')
        self.items.append((name, price, quantity))

    def print_bill(self):
        total = 0
        print('\n--- BILL ---')
        for name, price, quantity in self.items:
            subtotal = price * quantity
            total += subtotal
            print(f'{name}: {quantity} x {price:.2f} = {subtotal:.2f}')
        print(f'TOTAL: {total:.2f}')


def main():
    bill = BillingSystem()
    while True:
        print("\n1. Calculate employee salary  2. Add bill item  3. Print bill  0. Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1":
                employee = Employee(input("Employee ID: ").strip(), input("Name: ").strip(), float(input("Base salary: ")))
                bonus = float(input("Bonus: "))
                deductions = float(input("Deductions: "))
                print(f"Net salary for {employee.name}: {employee.net_salary(bonus, deductions):.2f}")
            elif choice == "2":
                bill.add_item(input("Item name: ").strip(), float(input("Price: ")), int(input("Quantity: ")))
                print("Item added.")
            elif choice == "3":
                bill.print_bill()
            elif choice == "0":
                break
            else:
                print("Invalid option.")
        except ValueError as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()
