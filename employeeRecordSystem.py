"""A simple employee record system that saves records in a CSV file."""
import csv
from pathlib import Path

FILE = Path(__file__).with_name('employees.csv')
FIELDS = ['employee_id', 'name', 'department', 'designation', 'salary']


def load_records():
    if not FILE.exists():
        return []
    with FILE.open('r', newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))


def save_records(records):
    with FILE.open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)


def add_employee():
    records = load_records()
    employee_id = input('Employee ID: ').strip()

    if employee_id == '':
        print('Employee ID cannot be empty.')
        return

    for record in records:
        if record['employee_id'] == employee_id:
            print('That employee ID is already in use.')
            return

    name = input('Name: ').strip()
    department = input('Department: ').strip()
    designation = input('Designation: ').strip()

    try:
        salary = float(input('Salary: '))
    except ValueError:
        print('Enter a valid nonnegative salary.')
        return

    if salary < 0:
        print('Enter a valid nonnegative salary.')
        return

    records.append({
        'employee_id': employee_id,
        'name': name,
        'department': department,
        'designation': designation,
        'salary': f'{salary:.2f}',
    })
    save_records(records)
    print('Employee saved.')


def view_employees():
    records = load_records()

    if not records:
        print('No employee records yet.')
        return

    for record in records:
        print(
            f"{record['employee_id']} | {record['name']} | "
            f"{record['department']} | {record['designation']} | "
            f"{record['salary']}"
        )


def search_employee():
    employee_id = input('Employee ID to search: ').strip()
    records = load_records()

    for record in records:
        if record['employee_id'] == employee_id:
            for field in FIELDS:
                print(f'{field}: {record[field]}')
            return

    print('Employee not found.')


def delete_employee():
    employee_id = input('Employee ID to delete: ').strip()
    records = load_records()
    remaining_records = []
    employee_was_found = False

    for record in records:
        if record['employee_id'] == employee_id:
            employee_was_found = True
        else:
            remaining_records.append(record)

    if employee_was_found:
        save_records(remaining_records)
        print('Employee deleted.')
    else:
        print('Employee not found.')


def main():
    while True:
        print('\nEMPLOYEE RECORD SYSTEM')
        print('1. Add employee')
        print('2. View employees')
        print('3. Search employee')
        print('4. Delete employee')
        print('5. Exit')

        choice = input('Choose: ').strip()

        if choice == '5':
            break

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            delete_employee()
        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
