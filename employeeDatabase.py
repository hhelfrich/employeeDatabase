import personEmploy

running = True
employees = []
while (running):
    Print("Options: \n AddNewEmployee \n DeleteEmployee \n SeeList \n UploadList \n Exit")
    if (input() == "Exit"):
        running = False
    if (input() == "AddNewEmployee"):
        you.personEmploy.Person()
        you.getPerson()
        employees.append(you)
    if (input() == "DeleteEmployee"):

    if (input() == "SeeList"):
        Print(*employees, sep = "\n")
    if (input() == "UploadList"):
        with open("employeeDatabase") as file
            employees = file.readlines()

f = open("employeeDatabase", "w")
f.write(employees)
f.close()

