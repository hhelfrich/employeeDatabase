import personEmploy
you = personEmploy.Person()

running = True
employees = [] * 2
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
        inFile = open("employeeDatabase.txt", "r")
        for line in inFile:
            print(line)
            firstname, lastname, number, email, dateemployed, department, jobtitle = line.split(" ")
            emp = personEmploy.Person(firstname, lastname, number, email, dateemployed, department, jobtitle)
            employees.append(emp)
f = open("employeeDatabase.txt", "w")
for employee in employees:
    f.write(str(employee.firstname) + " " + str(employee.lastname) + " " + str(employee.number) + " " + str(employee.email) + " " + str(employee.dateemployed) + " " + str(employee.department) + " " + str(employee.jobtitle) + "\n")
f.close()

 