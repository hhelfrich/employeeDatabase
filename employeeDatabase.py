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
        inFile = open("employeeDatabase.rtf", "r")
        for line in inFile:
            print(line)
            firstname, lastname, number, email, dateemployed, department, jobtitle = line.split(" ")
            emp = Person(self, firstname, lastname, number, email, dateemployed, department, jobtitle)
            employees.append(emp)
f = open("employeeDatabase.rtf", "w")
f.write(str(employees.firstname) + " " + str(employees.lastname) + " " + str(employees.number) + " " + str(employees.email) + " " + str(employees.dateemployed) + " " + str(employees.department) + " " + str(employees.jobtitle) + "\n")
f.close()

 