from abc import ABC, abstractmethod

from tkinter import LabelFrame, Label, Entry, Spinbox, StringVar, Checkbutton
from tkinter.ttk import Combobox


class MyInput(ABC):
    # Entry || Spinbox || Combobox
    input = None

    # StringVar
    value = None
    default_value = ""

    @classmethod
    @abstractmethod
    def __init__(self):
        pass

    def get_input_value(self):
        return self.value.get()

    def set_input_value(self, new_text: str):
        self.value.set(new_text)

    def clear_input_value(self):
        self.set_input_value(self.default_value)

    def disabled_input(self):
        self.clear_input_value()
        self.input.config(state='disabled')

    def enable_input(self):
        self.clear_input_value()
        self.input.config(state='normal')


class MyInputText(MyInput):
    def __init__(self, master: LabelFrame, text: str, position=(0, 0)):
        label_text = f'{text.strip().capitalize()}'

        row = position[0]
        column = position[1]

        # Label
        self.label = Label(master, text=label_text)
        self.label.config(font=('Arial', 12, 'bold'))
        self.label.grid(row=row, column=column, padx=10, pady=5)

        # Input
        self.default_value = ""
        self.value = StringVar(value=self.default_value)

        row = row + 1
        self.input = Entry(master, textvariable=self.value)
        self.input.config(font=('Arial', 12))
        self.input.grid(row=row, column=column, padx=10, pady=5)


class MyInputNumber(MyInput):
    def __init__(self, master: LabelFrame, text: str, position=(0, 0), rangeInput=(0, 'infinity')):
        label_text = f'{text.strip().capitalize()}'

        row = position[0]
        column = position[1]

        # Label
        self.label = Label(master, text=label_text)
        self.label.config(font=('Arial', 12, 'bold'))
        self.label.grid(row=row, column=column, padx=10, pady=5)

        # Input
        self.default_value = rangeInput[0]
        self.value = StringVar(value=self.default_value)

        row = row + 1
        self.input = Spinbox(
            master,
            textvariable=self.value,
            from_=rangeInput[0],
            to=rangeInput[1]
        )
        self.input.config(font=('Arial', 12))
        self.input.grid(row=row, column=column, padx=10, pady=5)


class MyInputSelect(MyInput):
    def __init__(self, master: LabelFrame, text: str, position=(0, 0), options=tuple()):
        label_text = f'{text.strip().capitalize()}'

        row = position[0]
        column = position[1]

        # Label
        self.label = Label(master, text=label_text)
        self.label.config(font=('Arial', 12, 'bold'))
        self.label.grid(row=row, column=column, padx=10, pady=5)

        # style = Style()
        # style.configure('TCombobox', fieldbackground=[('readonly', 'white')])
        # style.configure('TCombobox', selectbackground=[('readonly', 'white')])
        # style.configure('TCombobox', selectforeground=[('readonly', 'black')])

        # Input
        self.default_value = options[0]
        self.value = StringVar(value=self.default_value)

        row = row + 1
        self.input = Combobox(
            master,
            textvariable=self.value,
            state="readonly",
            values=options
        )

        self.input.config(font=('Arial', 12))
        self.input.grid(row=row, column=column, padx=10, pady=5)


class MyInputCheckBox(MyInput):
    def __init__(self, master: LabelFrame, text_check_box: str, label_text="", position=(0, 0), onvalue: bool | str = True, offvalue: bool | str = False):
        row = position[0]
        column = position[1]

        if label_text.strip() != "":
            label_text = f'{label_text.strip().capitalize()}'

            # Label
            self.label = Label(master, text=label_text)
            self.label.config(font=('Arial', 12, 'bold'))
            self.label.grid(row=row, column=column, padx=10, pady=5)

            row = row + 1

        # Input
        self.default_value = offvalue
        self.value = StringVar(value=self.default_value)

        self.input = Checkbutton(
            master,
            variable=self.value,
            onvalue=onvalue,
            offvalue=offvalue,
            text=text_check_box
        )
        self.input.config(font=('Arial', 12))
        self.input.grid(row=row, column=column, padx=10, pady=5)
