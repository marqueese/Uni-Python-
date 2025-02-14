class Students:
    valid_courses = {'Computer Science', 'Software Engineering', 'Networks and Security', 'Data Science',
                     'Cybersecurity', 'Computing'}

    def __init__(self, course, up_number, year):
        self.course = course
        self.up_number = up_number
        self.year = year

    def new_course(self, course_name):
        if course_name in self.valid_courses:
            self.course = course_name
        else:
            print(f"{course_name} is not a valid course.")

    def new_up(self, up_number):
        if len(up_number) == 7:
            self.up_number = up_number
        else:
            print("Invalid UP number. It must be exactly 7 digits.")

    def __str__(self):
        return f"Student {self.up_number} studying {self.course} in Year {self.year}"


class PlacementStudents(Students):

    def __init__(self, up_number, course, year, company):
        super().__init__(course, up_number, year)
        self.company = company

    def __str__(self):
        return f"Placement student up{self.up_number} working at {self.company}"





def main():
    student1 = Students("Computer Science", "1234567", "1")
    student2 = Students("Software Engineering", "2345678", "2")
    student3 = Students("Cybersecurity", "3456789", "3")

    student4 = PlacementStudents("1234567", "horseshit", "2099", "The Brick")


    print(student1)
    print(student2)
    print(student3)
    print(student4)

main()
