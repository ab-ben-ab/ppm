from sys import argv
from datetime import date, datetime
from encrypt import encrypt
from decrypt import decrypt


def read_data():
    decrypt()
    with open("sec.txt", "rb") as f:
        content = f.read()
        print(content.decode())


def add_password(key, site, password):
    with open("sec.txt", "a") as f:
        f.write(f"{site} :: {password}\n")
    encrypt(key)

    print("successfully added a new password")


def main():
    try:
        # adding password case
        if "-r" not in argv: 
            key = argv[1]
            site = argv[2]
            password = argv[3]
            add_password(key, site, password)

        # reading passwords case
        else: 
            read_data()
    except IndexError:
        print("key | -r if reading | password if adding")
    finally:
        print("="*15)


if __name__ == '__main__':
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")

    print("="*15, f"Password_manager - {date}", sep="\n")
    main()