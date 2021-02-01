class Person:
    def __init__(self, firstname = "J.", lastname = "Doe", number = "111-111-1111", email = "jdoe@company", dateemployed = "01/01/2000", department = "IT", jobtitle = "intern"):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.email = email
        self.dateemployed = deteemployed
        self.department = department
        self.jobtitle = jobtitle

    def getPerson(self):
        firstname, lastname = input("Hello! What is your full name?: ").split(" ")
        self.firstname = firstname
        self.lastname = lastname
        number = input("What is your phone number?: ")
        self.number = number
        email = input("What is your email address?: ")
        self.email = email
        dateemployed = input("What date were you employed? (mm/dd/yyyy): ")
        self.dateemployed = dateemployed
        department = input("What department are you in?: ")
        self.department = department
        jobtitle = input("What is your job title?: ")
        self.jobtitle = jobtitle
    
    def setFirstname(self, firstname):
        self.firstname = firstname
    
    def setLastname(self, lastname):
        self.lastname = lastname

    def setNumber(self, number):
        self.number = number
    
    def setEmail(self, email):
        self.email = email

    def setDateemployed(self, dateemployed):
        self.dateemployed = dateemployed
    
    def setDepartment(self, department):
        self.department = department

    def setJobtitle(self, jobtitle):
        self.jobtitle = jobtitle
        