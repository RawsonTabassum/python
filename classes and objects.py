class Classmates():
    total_semesters = 8

    def student(self, name):
        if name is 'ariful':
            print("rip ariful :( ")
        elif name is 'logno':
            print("logno went abroad")
        elif name is 'paroma':
            print("paroma in usa")
        elif name is 'shaheen':
            print("shaheen left cse to become pilot")
        elif name is 'firoz':
            print("dropped semester")
        else:
            print("still stuck in ruet man :')")

    def still_student(self):
        if self.total_semesters <= 0:
            print("not a student anymore")
        else :
            print("still a student")

    def semesters_passed (self, year):
        if year is 1:
            self.total_semesters -= year * 2
            self.still_student()
        elif year is 2:
            self.total_semesters -= year * 2
            self.still_student()
        elif year is 3:
            self.total_semesters -= year * 2
            self.still_student()
        elif year is 4:
            self.total_semesters -= year * 2
            self.still_student()


Student = []
for number in range (11):
    Student.append(Classmates())

n1 = 'esha'
n2 = 'shaheen'
n3 = 'paroma'

for x in range (0, 11, 1):
    if x is 2 or x is 3 or x is 5 or x is 7:
        print(Student[x].student(n2))
    elif x is 6 or x is 8 or x is 10:
        print(Student[x].student(n3))
    elif x is 1 or x is 4 or x is 9:
        print(Student[x].student(n1))