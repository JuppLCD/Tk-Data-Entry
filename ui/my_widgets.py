from abc import ABC, abstractmethod

from tkinter import Frame, Label, Entry, Spinbox, StringVar, Checkbutton
from tkinter.ttk import Combobox, Treeview, Scrollbar

# Tkinter constants
from tkinter import END, CENTER, NS, E


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
    def __init__(self, master: Frame, text: str, position=(0, 0)):
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
    def __init__(self, master: Frame, text: str, position=(0, 0), rangeInput=(0, 'infinity')):
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
    def __init__(self, master: Frame, text: str, position=(0, 0), options=tuple()):
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
    def __init__(self, master: Frame, text_check_box: str, label_text="", position=(0, 0), onvalue: bool | str = True, offvalue: bool | str = False):
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


class MyTable():
    def __init__(
            self,
            master: Frame,
            cols=(0, 1, 2),
            cols_text=("#0", "#1", "#2"),
            cols_width=(100, 100, 100),
            position=(0, 0),
            columnspan=1,
            sticky=NS+E,
            ** kwargs
    ):
        """
        cols[0] will be the identifier of the element in the table
        """

        self.table = Treeview(master, **kwargs, columns=cols, show="headings")

        self.table.grid(
            row=position[0],
            column=position[1],
            columnspan=columnspan,
            sticky=sticky
        )

        for i, col in enumerate(cols):
            self.table.heading(
                col,
                text=cols_text[i],
                anchor=CENTER
            )

        for i, col in enumerate(cols):
            self.table.column(
                col,
                width=cols_width[i]
            )

        # Añadiendo y configurando el scroll de la tabla
        self.scroll = Scrollbar(
            master,
            orient='vertical',
            command=self.table.yview
        )

        col_scroll = position[1] + columnspan - 1
        self.scroll.grid(row=position[0], column=col_scroll, sticky='nse')

        self.table.configure(yscrollcommand=self.scroll.set)

    def clear_table(self):
        # get_children() retorna una lista, e * al inicio es el spreed operator
        self.table.delete(*self.table.get_children())

    def insert_item(self, item):
        self.table.insert('', END, text=item[0], values=item)

    def insert_all_items(self, all_items: list):
        for item in all_items:
            self.insert_item(item)

    def select_item(self) -> dict | None:
        try:
            return self.table.item(self.table.selection())
        except IndexError:
            return None

    def get_item(self) -> tuple | None:
        item = self.select_item()

        if item != None:
            item = item['values']

        return item
