from os import path
from xlrd import open_workbook
from .models.categories import Category
from .models.sub_categories import SubCategory
from .models.items import Item

from app import db

xl_path = '/import/data.xlsx'
cwd_xl = path.dirname(path.abspath(__file__)) + xl_path
dir_strings = cwd_xl.split("/")
# dir_strings = [i for i in dir_strings if i!="db"]
dir_strings = [i for i in dir_strings]
import_xl_path = "/".join(dir_strings)


class Excel():
    def load_wb(self, path):
        self.wb = open_workbook(path)
        return self.wb

    def load_keys(self,sheet):
        return [sheet.cell_value(0, i) for i in range(sheet.ncols)]

    def add_rows(self, sheet, model):
        for row in range(sheet.nrows-1):
            data = {}
            keys = self.load_keys(sheet)
            for col, key in enumerate(keys):
                data[key] = sheet.cell_value(row+1, col)
                if type(data[key]) is float:
                    data[key] = int(data[key])
            m = model(**data)
            db.session.add(m)
        db.session.commit()

    def create_all_data(self):
        self.load_categories(excel_session.load_wb(import_xl_path))
        self.load_sub_categories(excel_session.load_wb(import_xl_path))
        self.load_items(excel_session.load_wb(import_xl_path))

        return

    def load_categories(self, wb):
        # if Category.query.count():
        #     return
        target_sheet = wb.sheet_by_name("category")
        self.add_rows(target_sheet, Category)
        return

    def load_sub_categories(self, wb):
        # if SubCategory.query.count():
        #     return
        target_sheet = wb.sheet_by_name("subcategory")
        self.add_rows(target_sheet, SubCategory)
        return

    def load_items(self, wb):
        # if Item.query.count():
        #     return
        target_sheet = wb.sheet_by_name("item")
        Item.query.filter().delete(synchronize_session='fetch')
        db.session.commit()
        self.add_rows(target_sheet, Item)
        return


db.create_all()
excel_session = Excel()
excel_session.create_all_data()
