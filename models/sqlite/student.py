from utils.entities import Student
from models.sqlite.connection import Connection
from models.model_abstract import ModelAbstract


class StudentModel(ModelAbstract, Connection):
    def __init__(self):
        super().__init__()
        self.create_table()

    def create_table(self):
        sql = '''CREATE TABLE IF NOT EXISTS student (
            firstname varchar(100) NOT NULL,
            lastname varchar(100) NOT NULL,
            title varchar(5) NOT NULL,
            age INTEGER,
            nationality varchar(13),
            registration_status varchar(14),
            num_courses INTEGER,
            num_semesters INTEGER
            )
        '''

        self._run_query(sql)

    def store(self, data: Student):
        new_student = (
            data.firstname,
            data.lastname,
            data.title,
            data.age,
            data.nationality,
            data.registration_status,
            data.numcourses,
            data.numsemesters,
        )
        self._run_query(
            "INSERT INTO student (firstname, lastname, title, age, nationality, registration_status, num_courses, num_semesters) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            new_student
        )
