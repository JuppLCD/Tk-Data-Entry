from tkinter import Tk, Frame, Menu


from models.model_abstract import ModelAbstract

from ui.views.student_form import StudentFormView
from ui.views.student_table import StudentTableView


class App:
    def __init__(self, studentModel: ModelAbstract):
        self.window = Tk()
        self.window.title("Data Entry Form")

        self.setting_window_size()

        self.main_frame = Frame(self.window).pack()

        self.studentModel = studentModel

        self.current_view = None
        self.menu()
        self.default_view()

    def setting_window_size(self):
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
            master=self.main_frame, studentModel=self.studentModel)

    def students_table_view(self):
        self.clear_current_view()

        self.current_view = StudentTableView(
            master=self.main_frame, studentModel=self.studentModel)

    def clear_current_view(self):
        if self.current_view != None:
            self.current_view = self.current_view.destroy()
