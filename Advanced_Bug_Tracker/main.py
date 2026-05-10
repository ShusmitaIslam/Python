import os
print("Current working directory: ", os.getcwd())
class Bug:
    def __init__(self, id, title, severity, status):
        self.id = id
        self.title = title
        self.severity = severity
        self.status = status

def add_bug():
    n = int(input("How much bug you want to add: "))

    try:
        with open("bugs.txt", "a") as files:
            for i in range(n):
                id = input("Enter the id: ")
                title = input("Enter the title: ")
                severity = input("Enter the severity(low/medium/high): ").lower()
                status = input("Enter the status: ").lower()
                files.write(f"{id},{title},{severity},{status}\n")
            print("Bugs add successfully.\n")
    except FileNotFoundError:
        open("bugs.txt", "w").close()

def show_bugs():
    try:
        print("\nOpen bugs are listed below: ")
        found = False
        with open("bugs.txt", "r") as files:
            for line in files:
                id, title, severity, status = line.strip().split(",")

                if status == "open":
                    print(f"Bug title: {title}")
                    found = True

            if not found:
                print("No bug is in open status.")
    except FileNotFoundError:
        open("bugs.txt","w").close()

def filter():
    severity_level = input("\nEnter the severity level: ").lower()
    found = False
    try:
        with open("bugs.txt", "r") as files:
            print(f"The {severity_level} level bug title is: ")
            for line in files:
                id, title, severity, status = line.strip().split(",")

                if severity_level == severity:
                    print(title)
                    found = True
            if not found:
                print("No bug is exist with this severity.")
    except FileNotFoundError:
        open("bugs.txt", "w").close()

def Closed_bug():
    Closed_id = input("\nEnter the bug id you want to close: ")
    found = False
    try:
        with open("bugs.txt", "r") as files:
            for line in files:
                id, title, severity, status = line.strip().split(",")

                if Closed_id == id:
                    status = "closed"
                    found = True

                if status == "closed":
                    print(f"The closed bug title: {title}")

            if not found:
                print("No bug is exist with this id.")
    except FileNotFoundError:
        open("bugs.txt", "w").close()

def Delete_bug():
    import shutil
    shutil.copy("bugs.txt", "bugs_backup.txt")
    delete_id = input("\nEnter the bug id you want to delete: ")
    found = False
    try:
        with open("bugs.txt", "r") as files:
            lines = files.readlines()

        with open("bugs.txt", "w") as files:
            for line in lines:
                id, title, severity, status = line.strip().split(",")

                if delete_id.strip() != id.strip():
                    files.write(line)
                else:
                    found = True

        if found:
            print("Bug deleted successfully.")
        else:
            print("Bug Id not found.")
    except FileNotFoundError:
        print("No bug file found.")


add_bug()
show_bugs()
filter()
Closed_bug()
Delete_bug()