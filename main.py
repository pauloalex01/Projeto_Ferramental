from interface.motiva_app import MotivaApp
from database.banco_de_dados import Database

def main():

    Database.criar_banco()
    app = MotivaApp()
    app.mainloop()


if __name__ == "__main__":
    main()
