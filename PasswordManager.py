import random
import string

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def add_password(self, website, username, password):
        if website in self.passwords:
            print(f"Password for {website} already exists. Overwriting...")
        self.passwords[website] = {'username': username, 'password': password}
        print(f"Password for {website} added/updated.")

    def get_password(self, website):
        if website in self.passwords:
            account = self.passwords[website]
            print(f"Website: {website}")
            print(f"Username: {account['username']}")
            print(f"Password: {account['password']}")
        else:
            print(f"Password for {website} not found in the manager.")

    def list_websites(self):
        if self.passwords:
            print("Saved Websites:")
            for website in self.passwords:
                print(website)
        else:
            print("No passwords saved in the manager.")

def main():
    password_manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add or Update Password")
        print("2. Get Password")
        print("3. List Websites")
        print("4. Generate Random Password")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            website = input("Enter the website: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            password_manager.add_password(website, username, password)
        elif choice == "2":
            website = input("Enter the website to get the password: ")
            password_manager.get_password(website)
        elif choice == "3":
            password_manager.list_websites()
        elif choice == "4":
            password = password_manager.generate_password()
            print(f"Generated Password: {password}")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
