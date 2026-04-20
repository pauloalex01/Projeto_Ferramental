import customtkinter


class BuscaFrame(customtkinter.CTkFrame):
    def __init__(self, master, matricula_service, ferramenta_service):
        super().__init__(master)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.matricula_service = matricula_service
        self.ferramenta_service = ferramenta_service

        self.tipo_busca = "ferramenta"

        self.grid_columnconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(
            self, text="Seção de Busca",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.label.grid(row=0, column=0, padx=40, pady=20, )

        # botão toggle
        self.toggle_btn = customtkinter.CTkButton(
            self,
            text="Buscar: Ferramenta",
            command=self.alternar_tipo,
            **btn_args
        )
        self.toggle_btn.grid(row=0, column=3, pady=(30, 10), padx=20)

        # form
        self.form_frame = customtkinter.CTkFrame(self)
        self.form_frame.grid(row=2, column=0, pady=10)

        # botão buscar
        self.btn_buscar = customtkinter.CTkButton(
            self,
            text="Buscar",
            command=self.buscar,
            **btn_args
        )
        self.btn_buscar.grid(row=3, column=0, pady=(10, 30))

        # resultado
        self.resultado = customtkinter.CTkTextbox(self, width=600, height=150, font=customtkinter.CTkFont(size=22, weight="bold"))
        self.resultado.grid(row=4, column=0, pady=(10, 30))

        self.render_form()

    def alternar_tipo(self):
        if self.tipo_busca == "ferramenta":
            self.tipo_busca = "matricula"
            self.toggle_btn.configure(text="Buscar: Matrícula")
        else:
            self.tipo_busca = "ferramenta"
            self.toggle_btn.configure(text="Buscar: Ferramenta")

        self.render_form()

    def render_form(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        entry_width = 600
        entry_height = 40

        if self.tipo_busca == "ferramenta":
            self.input_busca = customtkinter.CTkEntry(
                self.form_frame,
                placeholder_text="Código ou Descrição",
                width=entry_width,
                height=entry_height
            )
            self.input_busca.grid(row=0, column=0, pady=10)

        else:
            self.input_busca = customtkinter.CTkEntry(
                self.form_frame,
                placeholder_text="Matrícula ou Nome",
                width=entry_width,
                height=entry_height
            )
            self.input_busca.grid(row=0, column=0, pady=10)

    def buscar(self):
        valor = self.input_busca.get().strip()

        self.resultado.delete("1.0", "end")

        if not valor:
            self.resultado.insert("end", "Digite um valor para busca.")
            return

        if self.tipo_busca == "ferramenta":
            resultado = self.ferramenta_service.buscar(valor)

            if resultado == 1 or not resultado:
                self.resultado.insert("end", "Ferramenta não encontrada.")
            else:
                _, codigo, descricao, status, quantidade, ativo = resultado

                status_txt = "Ativo" if ativo == 1 else "Desativado"

                texto = (
                    f"Código: {codigo}\n"
                    f"Descrição: {descricao}\n"
                    f"Quantidade: {quantidade}\n"
                    f"Status: {status_txt}"
                )
                self.resultado.insert("end", texto)

        else:
            resultado = self.matricula_service.buscar(valor)

            if resultado == 1 or not resultado:
                self.resultado.insert("end", "Matrícula não encontrada.")
            else:
                _, matricula, nome, status, setor = resultado

                status_txt = "Ativo" if status == 1 else "Desativado"

                texto = (
                    f"Matrícula: {matricula}\n"
                    f"Nome: {nome}\n"
                    f"Setor: {setor}\n"
                    f"Status: {status_txt}"
                )
                self.resultado.insert("end", texto)