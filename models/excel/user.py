import os

from utils.entities import User
from models.model_abstract import ModelAbstract
from models.excel.excel import ExcelModel

ruta_actual = os.path.abspath(os.path.dirname(__file__))


class UserModel(ModelAbstract, ExcelModel):
    heading = ("First Name", "Last Name", "Title", "Age",
               "Nationality", "# Courses", "# Semesters", "Registration status")
    filepath = os.path.join(ruta_actual, '..', '..', 'db', 'data.xlsx')

    def __init__(self):
        super().__init__(UserModel.filepath, UserModel.heading)

    def store(self, data: User):
        self.apend_data([
            (
                data.firstname,
                data.lastname,
                data.title,
                data.age,
                data.nationality,
                data.numcourses,
                data.numsemesters,
                data.registration_status
            )
        ])
