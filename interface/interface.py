import customtkinter as ctk
from barcode.decoder_cam import Leitor_codigo


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('600x500')
        self.title('Controle Ferramental')
        self.leitor = Leitor_codigo()


        self.button = ctk.CTkButton(self, text='BUTAO', text_color='red', command=self.click)
        self.button.grid(row=0, column=0, padx=20, pady=10)

    def click(self):
        print('Iniciando Câmera')
        self.leitor.executar()




app = App()

app.mainloop()