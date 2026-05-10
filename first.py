test_result = []
passed = 0
failed = 0
TotalTime = 0

n = int(input("Enter the number of test cases: "))

for i in range(n):
    name = input("Enter the name: ")
    status = input("Enter the status: ")
    time = int(input("Enter the time: "))

    test_result.append({
        "name" : name,
        "status" : status,
        "time" : time
        })
    
    TotalTime += time
    
    SlowedTime = time
    if time < SlowedTime:
        SlowedTime = time

    if status.lower() == "passed":
        passed += 1
    else:
        failed += 1

print("\n")
print("Expected Output: ")
print("Total: "+str(n))
print("Passed: "+str(passed))
print("Failed: "+str(failed))
print("\n")

if failed > 0:
    print("Failed Tests: ")
    for test in test_result:
        if test['status'].lower() == "failed":
            print("- " + test['name'])

print("\n")
print("Total Time: " + str(TotalTime) + "s")
print("Average Time: " + str(TotalTime/n) + "s")

print("\n")
print("Slowed Test: " + str(SlowedTime))

print("\n")
if failed > 0 :
    print("⚠️ Some tests are failing!")
else:
    priint("✅ All tests passed!")