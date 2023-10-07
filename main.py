from app import App

# from models.excel.student import StudentModel
from models.sqlite.student import StudentModel

if __name__ == "__main__":
    studentModel = StudentModel()

    App(studentModel=studentModel).window.mainloop()
