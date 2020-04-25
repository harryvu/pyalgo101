class Student:
    class Address:
        """1149 E Plymouth St, Long Beach, CA 908085"""
        def __init__(self):
            self.street = "Main Street"
            self.number = "1"
            self.city = "Big City"
            self.state = "CA"
            self.zip = "90805"

    def __init__(self, fname, lname, email):
        self.firstname = fname
        self.lastname = lname
        self.email = email
        self.address = self.Address()

aStudent = Student("Harry", "Vu", "hvu@outlook.com")
print(aStudent.address.street)
