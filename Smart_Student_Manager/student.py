def add_student():
    existing_ids = set()
    try:
        with open("students.txt","r") as files:
            for line in files:
                id, _, _ = line.strip().split(",")
                existing_ids.add(id)

        n = int(input("How much student's information you want to store: "))
    except FileNotFoundError():
        open("students.txt", "w").close()

    try: 
        with open("students.txt", "a") as files:
            for i in range(n):
                id = input("Enter the id: ")

                if id in existing_ids:
                    print("Id already exists! Try again.")
                    continue

                name = input("Enter the name: ")
                marks = int(input("Enter the mark: "))

                files.write(f"{id},{name},{marks}\n")
        print("Test added successfully.\n")
    except FileNotFoundError():
        open("students.txt", "w").close()

def show_all_student():
    print("\nAll student: ")
    try:
        with open("students.txt", "r") as files:
            for lines in files:
                id, name, marks = lines.strip().split(",")
                print(f"ID: {id} | Name: {name} | Marks: {marks}")
    except FileNotFoundError:
        open("students.txt", "w").close()

def search():
    i = input("\n\nSearch with the student id: ")
    found = False
    
    try: 
        with open("students.txt", "r") as files:
            for line in files:
                id, name, marks = line.strip().split(",")

                if i == id:
                    print(f"ID: {id} | Name: {name} | Marks: {marks}\n")
                    found = True
                    break

        if not found:
            print("Invalid Id\n")
    except FileNotFoundError:
        open("students.txt", "w").close()

def update_marks():
    updated_list = []
    j = input("Enter the student id you want to update: ")
    updated = False

    try:
        with open("students.txt", "r") as files:
            for line in files:
                id, name, marks = line.strip().split(",")

                if j == id and not updated:
                    marks = input("Enter the new mark: ")
                    updated = True

                updated_list.append(f"{id},{name},{marks}\n")
    
        with open("students.txt", "w") as files:
            files.writelines(updated_list)
        print("Mark updated successfully.")
    except FileNotFoundError:
        open("students.txt", "w").close()

def sort_students():
    sort_list = []
    print("\nSort result:")
    try:
        with open("students.txt", "r") as files:
            for line in files:
                id, name, marks = line.strip().split(",")

                sort_list.append({
                    "id" : id,
                    "name" : name,
                    "marks" : int(marks)
                })

            sort_list.sort(key=lambda x: x["marks"], reverse=True)

        for s in sort_list:
            print(f"ID: {s['id']}, Name: {s['name']}, Marks: {s['marks']}")
    except FileNotFoundError:
        open("students.txt", "w").close()

def above_eighty():
    print("\nHigh score students list: ")
    above = False
    try:
        with open("students.txt", "r") as files:
            for line in files:
                id, name, marks = line.strip().split(",")

                if int(marks) > 80:
                    print(f"The student id: {id} and name: {name} and marks: {marks}")
                    above = True
            
            if not above:
                print("No sudent with above 80% marks.")
    except FileNotFoundError:
        open("students.txt", "w").close()

add_student()
show_all_student()
search()
update_marks()
sort_students()
above_eighty()