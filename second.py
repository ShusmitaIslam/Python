print("Problem 1:")
name = input("Enter user's name: ")
print("Hello, " + name +"! Welcome to QA Automation")


print("\n")
print("Problem 2:")
number1 = int(input("Enter integer number: "))
number2 = float(input("Enter float number: "))
print("Sum: " + str(number1 + number2))
print("Multiplication: " + str(number1 * number2))


print("\n")
print("Problem 3:")
number = []
TotalNumber = 0
n = int(input("Enter the number of input: "))
for i in range(n):
    num = int(input("Enter the number: "))
    number.append(num)
    TotalNumber += num
print("All numbers: ")
for num in number:
    print(num)
print("Total sum: ", str(TotalNumber))


print("\n")
print("Problem 4:")
num1 = int(input("Enter the number: "))
if num1%2 == 0:
  print("Even number")
else:
   print("Odd number")


print("\n")
print("Problem 5:")
tests = []
tests.append({
   "name" : "Login Test",
   "status" : "fail",
   "time" : 3
})
for test in tests:
   print("Test name: ",test["name"])
   print("Status: ",test["status"])
   if test['status'] == "fail":
      print("Fix required")


print("\n")
print("Problem 6:")
status = input("Enter the status: ")
def check_status(status):
   if status == "pass":
      print("Passed")
   else:
      print("Failed")
check_status(status)
check_status(status)


print("\n")
print("Problem 7:")
statuses = []
passed = 0
failed = 0
n = int(input("Enter the number of input you want to take: "))
for i in range(n):
   status = input("Enter the input: ").lower()
   statuses.append(status)
   if statuses[i] == "pass":
      passed += 1
   else:
      failed += 1
print("total pass: ",passed)
print("total fail: ",failed)


print("\n")
print("Problem 8:")
browsers = []
n = int(input("Enter the number of input: "))
for i in range(n):
   browser = input("Enter the name of the browser: ").lower()
   browsers.append(browser)
browser_tuple = tuple(browsers)
unique_set = set(browser_tuple)
print(unique_set)


print("\n")
print("Problem 9:")
n = int(input("Enter the number of input: "))
print("Even numbers: ")
for i in range(1,n+1):
   if i % 2 == 0:
      print(i)


print("\n")
print("Problem 10:")
tests = []
passed = 0
failed = 0
n = int(input("Enter the number of input: "))
for i in range(1,n+1):
   name = input(f"Enter the name #{i}: ")
   status = input(f"Enter the status #{i} (pass/fail): ").lower()

   dictionary = { "name" : name, "status" : status}
   tests.append(dictionary)

   if status == "pass":
      passed += 1
   elif status == "fail":
      print("\nFailed test name: ",name)
      failed += 1
   
if failed > 0 :
   print("Testing Failed")
else:
   print("All Passed")





