class Programmer:
    name = "N/A"
    main_language = ""
    salary = 0
    age = 0
    role = ""
    overall = ""

    def __init__(self):
        print(f"Hi {self.name}, Fill out the roles.")

    def GetAllInfo(self):
        print(f"The Employee's age is {self.age}")
        print(f"The Employee's main Programming Language is {self.main_language}")
        print(f"The Employee's Name is {self.name}")
        print(f"The Employee's Overall is {self.overall}")
        print(f"The Employee's role is {self.role}")
        print(f"The Employee's salary is {self.salary}")

hamoodiah = Programmer()

hamoodiah.age = 42
hamoodiah.main_language = "Python 3.12"
hamoodiah.name = "Hamoodiah"
hamoodiah.overall = "Best Empolayeee"
hamoodiah.role = "Bloddy CEO"
hamoodiah.salary = 1_000_000_000_000_000

hamoodiah.GetAllInfo()