from utils.entities import User
from models.model_abstract import ModelAbstract
from models.excel.excel import ExcelModel


class UserModel(ModelAbstract, ExcelModel):
    heading = ("First Name", "Last Name", "Title", "Age",
               "Nationality", "# Courses", "# Semesters", "Registration status")

    def __init__(self):
        super().__init__(UserModel.heading, None)

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
