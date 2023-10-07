from app import App

# from models.excel.user import UserModel
from models.sqlite.user import UserModel

if __name__ == "__main__":
    userModel = UserModel()

    App(userModel=userModel).window.mainloop()
