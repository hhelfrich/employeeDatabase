import personEmploy
you = personEmploy.Person()

running = True
employees = []
while (running):
    do = input("Options: \n AddNewEmployee \n DeleteEmployee \n SeeList \n UploadList \n Exit")
    if (do == "Exit"):
        running = False
    if (do == "AddNewEmployee"):
        you.getPerson()
        employees.append(you)
    if (do == "DeleteEmployee"):
        index = input("Type the index of the employee you wish to delete: ")
        array.pop(index)
    if (do == "SeeList"):
        print(*employees, sep = "\n")
    if (do == "UploadList"):
        with open("employeeDatabase.txt.rtf") as file:
            employees = file.readlines()

f = open("employeeDatabase.txt.rtf", "w")
f.write(employees)
f.close()

