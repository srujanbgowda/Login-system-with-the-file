def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password}\n")
    print("Registration successful!\n")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()
        for user in users:
            saved_username, saved_password = user.strip().split(",")
            if username == saved_username and password == saved_password:
                print("Login successful!\n")
                return
    print("Invalid username or password.\n")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice (1-3): ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

main()