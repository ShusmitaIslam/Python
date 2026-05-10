class Bug:
    def __init__(self, id, title, severity, status):
        self.id = id
        self.title = title
        self.severity = severity
        self.status = status

def add_bug():
    id = input("Enter the id: ")
    title = input("Enter the title: ")
    severity = input("Enter the severity: ")
    status = input("Enter the status: ")

    with open("bugs.txt", "a") as file:
        file.write(f"{id},{title},{severity},{status}\n")
    print("Bugs added successfully.")

def show_all():
    with open("bugs.txt", "r") as files:
        for line in files:
            id, title, severity, status = line.strip().split(",")
            print(f"{id} - {title} - {severity} - {status}")
    print()

def show_open():
    print("Open Bugs: ")
    with open("bugs.txt", "r") as file:
        for line in file:
            id, title, severity, status = line.strip().split(",")
            if status.lower() == "open":
                print(title)
    print()

def close_bug():
    bug_id = input("Enter the bug id: ")
    updated_bugs = []
    with open("bugs.txt", "r") as file:
        for line in file:
            id, title, severity, status = line.strip().split(",")
            if bug_id == id:
                status = "closed"
            updated_bugs.append(f"{id},{title},{severity},{status}")

    with open("bugs.txt", "w") as file:
        for bug in updated_bugs:
            file.write(bug+"\n")

    print("Bug updated successfully!\n")


        
