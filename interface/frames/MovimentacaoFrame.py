import customtkinter


class MovimentacaoFrame(customtkinter.CTkFrame):
    def __init__(self, master, movimentacao_service):
        super().__init__(master)

        self.movimentacao_service = movimentacao_service

        self.grid_columnconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(
            self,
            text="Seção de Movimentação",
            font=customtkinter.CTkFont(size=24, weight="bold")
        )
        self.label.grid(row=0, column=0, pady=20)

        self.btn_emprestar = customtkinter.CTkButton(
            self,
            text="Emprestar Ferramenta",
            command=self.emprestar
        )
        self.btn_emprestar.grid(row=1, column=0, pady=10)

        self.btn_devolver = customtkinter.CTkButton(
            self,
            text="Devolver Ferramenta",
            command=self.devolver
        )
        self.btn_devolver.grid(row=2, column=0, pady=10)

    def emprestar(self):
        print("Emprestar (implementar UI depois)")

    def devolver(self):
        print("Devolver (implementar UI depois)")