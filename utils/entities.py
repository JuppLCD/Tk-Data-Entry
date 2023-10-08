class Student:
    def __init__(
        self,
        firstname,
        lastname,
        title,
        age,
        nationality,
        registration_status,
        num_courses,
        num_semesters,
        id: int | None = None,
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.age = age
        self.nationality = nationality
        self.registration_status = registration_status
        self.num_courses = num_courses
        self.num_semesters = num_semesters

    def to_tuple(self):
        return (self.id, self.firstname, self.lastname, self.title, self.age, self.nationality, self.registration_status, self.num_courses, self.num_semesters)

    @staticmethod
    def from_tuple(student_tuple: tuple):

        id = student_tuple[0]
        firstname = student_tuple[1]
        lastname = student_tuple[2]
        title = student_tuple[3]
        age = student_tuple[4]
        nationality = student_tuple[5]
        registration_status = student_tuple[6]
        num_courses = student_tuple[7]
        num_semesters = student_tuple[8]

        return Student(
            id=id,
            firstname=firstname,
            lastname=lastname,
            title=title,
            age=age,
            nationality=nationality,
            registration_status=registration_status,
            num_courses=num_courses,
            num_semesters=num_semesters,
        )
