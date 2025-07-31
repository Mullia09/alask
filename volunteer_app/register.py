import csv
import os

CSV_FILE = os.path.join(os.path.dirname(__file__), 'volunteers.csv')

FIELDNAMES = ['name', 'email', 'phone']

def add_volunteer():
    name = input('Name: ').strip()
    email = input('Email: ').strip()
    phone = input('Phone: ').strip()
    write_header = not os.path.exists(CSV_FILE)
    with open(CSV_FILE, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow({'name': name, 'email': email, 'phone': phone})
    print('Volunteer registered.')


def list_volunteers():
    if not os.path.exists(CSV_FILE):
        print('No volunteers registered yet.')
        return
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader, 1):
            print(f"{i}. {row['name']} - {row['email']} - {row['phone']}")


def main():
    while True:
        print('\nVolunteer Registration')
        print('1. Add volunteer')
        print('2. List volunteers')
        print('3. Exit')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            add_volunteer()
        elif choice == '2':
            list_volunteers()
        elif choice == '3':
            break
        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
