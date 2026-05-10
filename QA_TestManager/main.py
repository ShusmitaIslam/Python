from utils import add_test, show_all, show_failed

while True:
    print("1. Add Test Result")
    print("2. Show All Results")
    print("3. Show Failed Tests")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_test()
    elif choice == "2":
        show_all()
    elif choice == "3":
        show_failed()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")