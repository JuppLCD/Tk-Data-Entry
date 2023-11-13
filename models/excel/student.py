from utils.entities import Student
from models.model_abstract import ModelAbstract
from models.excel.excel import ExcelModel

# ! TODO: Falta implementar metodos del ModelAbstract


class StudentModel(ModelAbstract, ExcelModel):
    heading = ("First Name", "Last Name", "Title", "Age",
               "Nationality", "# Courses", "# Semesters", "Registration status")

    def __init__(self):
        super().__init__(StudentModel.heading, None)

    def store(self, data: Student):
        self.apend_data([
            (
                data.firstname,
                data.lastname,
                data.title,
                data.age,
                data.nationality,
                data.num_courses,
                data.num_semesters,
                data.registration_status
            )
        ])
