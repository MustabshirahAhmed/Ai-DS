"""A simple library system that saves books and members in CSV files."""
import csv
from pathlib import Path

BOOKS_FILE = Path(__file__).with_name('books.csv')
MEMBERS_FILE = Path(__file__).with_name('members.csv')

BOOK_FIELDS = ['book_id', 'title', 'author', 'available', 'borrowed_by']
MEMBER_FIELDS = ['member_id', 'name']


def load_books():
    if not BOOKS_FILE.exists():
        return []

    with BOOKS_FILE.open('r', newline='', encoding='utf-8-sig') as file:
        return list(csv.DictReader(file))


def save_books(books):
    with BOOKS_FILE.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=BOOK_FIELDS)
        writer.writeheader()
        writer.writerows(books)


def load_members():
    if not MEMBERS_FILE.exists():
        return []

    with MEMBERS_FILE.open('r', newline='', encoding='utf-8-sig') as file:
        return list(csv.DictReader(file))


def save_members(members):
    with MEMBERS_FILE.open('w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=MEMBER_FIELDS)
        writer.writeheader()
        writer.writerows(members)


def add_book():
    books = load_books()
    book_id = input('Book ID: ').strip()

    if book_id == '':
        print('Book ID cannot be empty.')
        return

    for book in books:
        if book['book_id'] == book_id:
            print('That book ID is already in use.')
            return

    title = input('Book title: ').strip()
    author = input('Author: ').strip()

    book = {
        'book_id': book_id,
        'title': title,
        'author': author,
        'available': 'Yes',
        'borrowed_by': '',
    }
    books.append(book)
    save_books(books)
    print('Book added.')


def view_books():
    books = load_books()

    if not books:
        print('No books have been added yet.')
        return

    for book in books:
        print(
            f"{book['book_id']} | {book['title']} | {book['author']} | "
            f"Available: {book['available']}"
        )


def search_book():
    book_id = input('Book ID to search: ').strip()

    for book in load_books():
        if book['book_id'] == book_id:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Available: {book['available']}")
            return

    print('Book not found.')


def add_member():
    members = load_members()
    member_id = input('Member ID: ').strip()

    if member_id == '':
        print('Member ID cannot be empty.')
        return

    for member in members:
        if member['member_id'] == member_id:
            print('That member ID is already in use.')
            return

    name = input('Member name: ').strip()
    members.append({'member_id': member_id, 'name': name})
    save_members(members)
    print('Member registered.')


def view_members():
    members = load_members()

    if not members:
        print('No members have been registered yet.')
        return

    for member in members:
        print(f"{member['member_id']} | {member['name']}")


def borrow_book():
    book_id = input('Book ID to borrow: ').strip()
    member_id = input('Member ID: ').strip()
    books = load_books()
    members = load_members()

    member_exists = False
    for member in members:
        if member['member_id'] == member_id:
            member_exists = True
            break

    if not member_exists:
        print('Member not found. Register the member first.')
        return

    for book in books:
        if book['book_id'] == book_id:
            if book['available'] == 'No':
                print('That book is already borrowed.')
                return

            book['available'] = 'No'
            book['borrowed_by'] = member_id
            save_books(books)
            print('Book borrowed.')
            return

    print('Book not found.')


def return_book():
    book_id = input('Book ID to return: ').strip()
    books = load_books()

    for book in books:
        if book['book_id'] == book_id:
            if book['available'] == 'Yes':
                print('That book has not been borrowed.')
                return

            book['available'] = 'Yes'
            book['borrowed_by'] = ''
            save_books(books)
            print('Book returned.')
            return

    print('Book not found.')


def main():
    while True:
        print('\nLIBRARY MANAGEMENT SYSTEM')
        print('1. Add a book')
        print('2. View all books')
        print('3. Search for a book')
        print('4. Register a member')
        print('5. View all members')
        print('6. Borrow a book')
        print('7. Return a book')
        print('8. Exit')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            add_member()
        elif choice == '5':
            view_members()
        elif choice == '6':
            borrow_book()
        elif choice == '7':
            return_book()
        elif choice == '8':
            print('Goodbye.')
            break
        else:
            print('Invalid choice. Please choose a number from 1 to 8.')


if __name__ == '__main__':
    main()