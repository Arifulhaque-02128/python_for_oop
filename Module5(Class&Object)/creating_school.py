class Student :
    def __init__(self, name, id, cls) -> None:
        self.name = name
        self.id = id
        self.cls = cls
    
    def __repr__(self) -> str:
        print('---------- OUR STUDENTS ----------')
        return f'Student Name : {self.name} \nClass : {self.cls} \nID : {self.id}'


class Teacher :
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.id = id
        self.subject = subject
    
    def __repr__(self) -> str:
        print('---------- OUR TEACHERS ----------')
        return f'Teacher Name : {self.name} \nID : {self.id} \nSubject : {self.subject}'

class School :
    name = 'Educare'
    def __init__(self) -> None:
        self.teachers = []
        self.students = []
    
    def add_teacher(self, teacher_name, subject) :
        id = len(self.teachers) + 101
        teacher = Teacher(teacher_name, subject, id)
        self.teachers.append(teacher)
    
    def enroll_student(self, std_name, cls) :
        id = len(self.students) + 1001
        std = Student(std_name, id, cls)
        self.students.append(std)


    def __repr__(self) -> str:
        print('---------- OUR TEACHERS ----------')
        for t in self.teachers :
            print(f'Name : {t.name} \nID : {t.id} \nSubject : {t.subject}')
            print()
        
        print('---------- OUR STUDENTS ----------')
        for s in self.students :
            print(f'Name : {s.name} \nID : {s.id} \nClass: {s.cls}')
            print()

        return 'Thank You'
        

batch1 = School()
batch1.enroll_student('Ashik', 6)
batch1.enroll_student('Asif', 5)
batch1.enroll_student('Abir', 6)
batch1.enroll_student('Karim', 6)
batch1.enroll_student('Sabera', 5)
batch1.enroll_student('Razzak', 5)

batch1.add_teacher('Mamun', 'Algorithm')
batch1.add_teacher('Anis', 'Data Structure')
batch1.add_teacher('Selim', 'Object Oriented Programming')

print(batch1)


