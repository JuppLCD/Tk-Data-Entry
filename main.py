from tkinter import Tk, messagebox, Frame, LabelFrame, Button

from models.model_abstract import ModelAbstract
from models.excel.user import UserModel

from ui.my_widgets import MyInputText, MyInputNumber, MyInputSelect, MyInputCheckBox
from utils.entities import User


class MainFrame(Frame):
    def __init__(self, userModel: ModelAbstract, **kwargs):
        super().__init__(**kwargs)

        self.pack()

        self.userModel = userModel

        self.user_info_frame = UserInfoFrame(master=self)
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

        # User info
        user_info = self.user_info_frame.get_user_info()
        firstname = user_info["firstname"]
        lastname = user_info["lastname"]

        if firstname.strip() == "" or lastname.strip() == "":
            messagebox.showwarning(
                title="Error", message="First name and last name are required.")

            return

        # Course info
        course_info = self.courses_frame.get_course_info()

        user = User(
            firstname,
            lastname,
            title=user_info["title"],
            age=user_info["age"],
            nationality=user_info["nationality"],
            numcourses=course_info["numcourses"],
            numsemesters=course_info["numsemesters"],
            registration_status=course_info["registration_status"]
        )

        print("First name: ", user.firstname, "Last name: ", user.lastname)
        print("Title: ", user.title, "Age: ", user.age,
              "Nationality: ", user.nationality)
        print("# Courses: ", user.numcourses,
              "# Semesters: ", user.numsemesters)
        print("Registration status", user.registration_status)
        print("------------------------------------------")

        self.userModel.store(user)


# Saving User Info
class UserInfoFrame(LabelFrame):
    def __init__(self, **kwargs):
        super().__init__(text="User Information", **kwargs)

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

    def get_user_info(self) -> dict[str, str | int]:
        user_info = {
            "firstname": self.first_name_input.get_input_value(),
            "lastname": self.last_name_input.get_input_value(),
            "title": self.title_select.get_input_value(),
            "age": self.age_input.get_input_value(),
            "nationality": self.nationality_select.get_input_value(),
        }

        return user_info


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


class App:
    def __init__(self, userModel: ModelAbstract):
        self.window = Tk()
        self.window.title("Data Entry Form")

        MainFrame(master=self.window, userModel=userModel)


if __name__ == "__main__":
    # Excel DB
    userModel = UserModel()

    App(userModel=userModel).window.mainloop()
