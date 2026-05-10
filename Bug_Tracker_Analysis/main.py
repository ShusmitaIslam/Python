bugs = []
opened = 0
high = 0
critical_found = False
open_bug = False
n = int(input("Enter the number of test case: "))
for i in range(n):
    id = int(input("Enter the id: "))
    title = input("Enter the title: ")
    severity = input("Enter the severity: ").strip()
    status = input("Enter the status: ").strip()
    bugs.append({
        "id" : id,
        "title" : title,
        "severity" : severity,
        "status" : status
    })

for bug in bugs:
    if bug["status"].lower() == "open":
        opened += 1

    if bug["severity"].lower() == "high":
        high += 1

    if bug["status"].lower() == "open" and bug["severity"].lower() == "high":
        critical_found = True

    if bug["status"].lower() == "open":
        open_bug = True

print("Open bug count: ",opened)
print("High severity bug count: ",high)

if open_bug:
    print("Open Bugs: ")

for bug in bugs:
    if bug["status"].lower() == "open":   
        print(bug["title"])

if critical_found:
    print("Critical Issue Found!")
