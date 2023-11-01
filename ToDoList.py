class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the to-do list.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed from the to-do list.")
        else:
            print(f"Task '{task}' not found in the to-do list.")

    def list_tasks(self):
        if self.tasks:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

def main():
    to_do_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            to_do_list.add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            to_do_list.remove_task(task)
        elif choice == "3":
            to_do_list.list_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
