from bug_utils import add_bug, show_all, show_open, close_bug

while(True):
    print("1. Add Bug")
    print("2. Show All Bugs")
    print("3. Show Open Bugs")
    print("4. Close a Bug")
    print("5. Exit")
    choice = input("Choose the option: ")

    if choice == "1":
        add_bug()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_open()
    elif choice == "4":
        close_bug()
        break
    else:
        print("Invalid choice! Try again.\n")