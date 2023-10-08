from tkinter import messagebox, Frame, LabelFrame, Button


from models.model_abstract import ModelAbstract

from ui.my_widgets import MyInputText, MyInputNumber, MyInputSelect, MyInputCheckBox
from utils.entities import Student


class StudentFormView(Frame):
    def __init__(self, studentModel: ModelAbstract, **kwargs):
        super().__init__(**kwargs)

        self.pack()

        self.studentModel = studentModel

        self.student_info_frame = StudentInfoFrame(master=self)
        self.courses_frame = CoursesFrame(master=self)
        self.accept_terms_frame = TermsAndConditions(master=self)

        # Button
        button = Button(self, text="Enter data", command=self.enter_data)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    def enter_data(self):
        is_accepted = self.accept_terms_frame.is_accepted()

        if not is_accepted:
            messagebox.showwarning(
                title="Error",
                message="You have not accepted the terms"
            )

            return

        # Student info
        student_info = self.student_info_frame.get_student_info()
        firstname = student_info["firstname"]
        lastname = student_info["lastname"]

        if firstname.strip() == "" or lastname.strip() == "":
            messagebox.showwarning(
                title="Error", message="First name and last name are required.")

            return

        # Course info
        course_info = self.courses_frame.get_course_info()

        new_student = Student(
            firstname=firstname,
            lastname=lastname,
            title=student_info["title"],
            age=student_info["age"],
            nationality=student_info["nationality"],
            num_courses=course_info["numcourses"],
            num_semesters=course_info["numsemesters"],
            registration_status=course_info["registration_status"]
        )

        print("The data has been added correctly")

        self.studentModel.store(new_student)


# Saving Student Info
class StudentInfoFrame(LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(text="Student Information", **kwargs)

        self.grid(row=0, column=0, padx=20, pady=10)

        self.first_name_input = MyInputText(
            self, text="First Name", position=(0, 0))
        self.last_name_input = MyInputText(
            self, text="Last Name", position=(0, 1))

        self.title_select = MyInputSelect(
            master=self,
            text="Title",
            position=(0, 2),
            options=("", "Mr.", "Ms.", "Dr.")
        )

        self.age_input = MyInputNumber(
            master=self,
            text="Age",
            position=(2, 0),
            rangeInput=(18, 110)
        )

        self.nationality_select = MyInputSelect(
            master=self,
            text="Nationality",
            position=(2, 1),
            options=(
                "", "Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"
            )
        )

    def get_student_info(self) -> dict[str, str | int]:
        student_info = {
            "firstname": self.first_name_input.get_input_value(),
            "lastname": self.last_name_input.get_input_value(),
            "title": self.title_select.get_input_value(),
            "age": self.age_input.get_input_value(),
            "nationality": self.nationality_select.get_input_value(),
        }

        return student_info


# Saving Course Info
class CoursesFrame(LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.reg_status_input = MyInputCheckBox(
            self,
            label_text="Registration Status",
            text_check_box="Currently Registered",
            onvalue="Registered",
            offvalue="Not registered",
            position=(0, 0)
        )

        self.numcourses_input = MyInputNumber(
            master=self,
            text="# Completed Courses",
            position=(0, 1),
        )

        self.numsemesters_input = MyInputNumber(
            master=self,
            text="# Semesters",
            position=(0, 2),
        )

    def get_course_info(self) -> dict[str, str | int]:
        course_info = {
            "registration_status": self.reg_status_input.get_input_value(),
            "numcourses": self.numcourses_input.get_input_value(),
            "numsemesters": self.numsemesters_input.get_input_value()
        }

        return course_info


# Accept terms
class TermsAndConditions(LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(text="Terms & Conditions", **kwargs)

        self.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.accept_terms_input = MyInputCheckBox(
            self,
            text_check_box="I accept the terms and conditions.",
            onvalue="Accepted",
            offvalue="Not Accepted",
            position=(0, 0)
        )

    def is_accepted(self) -> bool:
        accepted = self.accept_terms_input.get_input_value()
        return accepted == "Accepted"
