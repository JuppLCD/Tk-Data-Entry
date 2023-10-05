from tkinter import Tk, messagebox, Frame, LabelFrame, Button, Menu

from models.model_abstract import ModelAbstract
# from models.excel.user import UserModel
from models.sqlite.user import UserModel


from ui.my_widgets import MyInputText, MyInputNumber, MyInputSelect, MyInputCheckBox, MyTable
from utils.entities import User


class StudentTableView(Frame):
    def __init__(self, userModel: ModelAbstract, **kwargs):
        super().__init__(**kwargs)

        self.pack()

        self.userModel = userModel

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


class StudentFormView(Frame):
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

        print("The data has been added correctly")

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

        # Main window size
        window_width = 900
        window_height = 500

        # User screen size
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Obtaining the coordinate in which the left point of the screen is going to be placed (we want to center it)
        x = int((screen_width/2) - (window_width/2))
        y = int((screen_height/2) - (window_height/2) - 30)
        # -30 for the taskbar at the bottom

        # Setting the width, height of the window and the coordinates in which it will be located
        self.window.geometry(
            f"{window_width}x{window_height}+{x}+{y}"
        )

        self.main_frame = Frame(self.window).pack()

        self.userModel = userModel

        self.current_view = None

        self.menu()

        self.default_view()

    def menu(self):
        menu_bar = Menu(self.window)
        self.window.config(menu=menu_bar)

        # --------------- Application menu
        home_menu = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label='Home', menu=home_menu)

        menu_bar.add_command(
            label='Students', command=self.students_table_view)

        # Example menus
        menu_bar.add_command(label='Setting', command=lambda: print("Setting"))
        menu_bar.add_command(label='Help', command=lambda: print("Help"))

        # --------------- Submenus
        home_menu.add_command(label='Student Form', command=self.default_view)
        home_menu.add_command(
            label='Opcion 1', command=lambda: print("Opcion 1"))
        home_menu.add_command(label='Close', command=self.window.destroy)

    def default_view(self):
        self.clear_current_view()

        self.current_view = StudentFormView(
            master=self.main_frame, userModel=self.userModel)

    def students_table_view(self):
        self.clear_current_view()

        self.current_view = StudentTableView(
            master=self.main_frame, userModel=self.userModel)

    def clear_current_view(self):
        if self.current_view != None:
            self.current_view = self.current_view.destroy()


if __name__ == "__main__":
    userModel = UserModel()

    App(userModel=userModel).window.mainloop()
