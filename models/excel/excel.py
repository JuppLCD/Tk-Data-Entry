import os

from openpyxl import Workbook, load_workbook


class ExcelModel():
    def __init__(self, filepath: str, heading: tuple):
        self.heading = heading
        self.filepath = filepath

        self.openWB()

    def apend_data(self, all_data: list[tuple]):
        self.openWB()
        for data in all_data:
            self.sheet.append(data)
        self.save_excel()

    def openWB(self):
        if not os.path.exists(self.filepath):
            self.workbook = Workbook()
            self.sheet = self.workbook.active

            self.sheet.append(self.heading)
        else:
            self.workbook = load_workbook(self.filepath)
            self.sheet = self.workbook.active

        self.save_excel()

    def save_excel(self):
        self.workbook.save(self.filepath)
