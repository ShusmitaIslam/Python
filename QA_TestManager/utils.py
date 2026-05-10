class TestCase:
    def __init__(self, name, status, time):
        self.name = name
        self.status = status
        self.time = time

def add_test():
    name = input("Enter test name: ")
    status = input("Enter status (pass/fail): ")
    time = input("Enter time in seconds: ")

    with open("test_data.txt", "a") as file:
        file.write(f"{name},{status},{time}\n")
    print("Test added successfully!\n")

def show_all():
    print("\nAll Tests: ")
    with open("test_data.txt", "r") as file:
        for line in file:
            name, status, time = line.strip().split(",")
            print(f"{name} - {status} - {time}s")
    print()
    
def show_failed():
    print("\nFailed Tests: ")
    with open("test_data.txt", "r") as file:
        for line in file:
            name, status, time = line.strip().split(",")
            if status.lower() == "fail":
                print(name)
print()
    
    