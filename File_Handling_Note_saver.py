def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!\n")



def main():
    while True:
        print("\nNote Saver Menu:")
        print("1. Add Note")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        match choice:
            case "1":
                add_note()

            case "2":
                print("Exiting....")
                break
            case _:
                print("Invalid choice. ")

main()
