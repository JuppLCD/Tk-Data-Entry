from tkinter import Frame


from models.model_abstract import ModelAbstract

from ui.my_widgets import MyTable


class StudentTableView(Frame):
    def __init__(self, studentModel: ModelAbstract, **kwargs):
        super().__init__(**kwargs)

        self.pack()

        self.studentModel = studentModel

        table_cols = ("id", "firstname", "lastname", "title", "age", "nationality",
                      "registration_status", "num_courses", "num_semesters")

        cols_width = (30, 100, 100, 70, 50, 120, 200, 140, 160)

        self.student_table = MyTable(
            self,
            cols=table_cols,
            cols_text=tuple(
                map(lambda col_text: col_text.upper(), table_cols)),
            cols_width=cols_width
        )
