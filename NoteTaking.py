class NoteTaker:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)
        print("Note added successfully.")

    def view_notes(self):
        if self.notes:
            print("Your Notes:")
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")
        else:
            print("You don't have any notes yet.")

    def delete_note(self, note_number):
        if 1 <= note_number <= len(self.notes):
            deleted_note = self.notes.pop(note_number - 1)
            print(f"Note deleted: {deleted_note}")
        else:
            print("Invalid note number. Please try again.")

def main():
    note_taker = NoteTaker()

    while True:
        print("\nNote-Taking Menu:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            note = input("Enter your note: ")
            note_taker.add_note(note)
        elif choice == "2":
            note_taker.view_notes()
        elif choice == "3":
            note_taker.view_notes()
            note_number = int(input("Enter the number of the note to delete (0 to cancel): "))
            if note_number != 0:
                note_taker.delete_note(note_number)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
