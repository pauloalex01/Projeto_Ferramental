import customtkinter
from CTkMessagebox import CTkMessagebox

from services.service import MatriculaService, FerramentaService


class CadastroFrame(customtkinter.CTkFrame):
    def __init__(self, master, matricula, ferramenta):
        super().__init__(master)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.matricula_service = MatriculaService()
        self.ferramenta_service = FerramentaService()

        self.tipo_cadastro = "ferramenta"

        self.grid_columnconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(
            self, text="Seção de Cadastro",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.label.grid(row=0, column=0, padx=20, pady=20)

        self.toggle_btn = customtkinter.CTkButton(
            self,
            text="Cadastrar: Ferramenta",
            command=self.alternar_tipo,
            **btn_args
        )
        self.toggle_btn.grid(row=0, column=3, pady=10, padx=20)

        self.form_frame = customtkinter.CTkFrame(self)
        self.form_frame.grid(row=1, column=0, pady=10)

        self.btn_salvar = customtkinter.CTkButton(
            self,
            text="Cadastrar",
            command=self.cadastrar,
            **btn_args
        )
        self.btn_salvar.grid(row=2, column=0, pady=(10, 30))

        self.render_form()

    def alternar_tipo(self):
        if self.tipo_cadastro == "ferramenta":
            self.tipo_cadastro = "matricula"
            self.toggle_btn.configure(text="Cadastrar: Matrícula")
        else:
            self.tipo_cadastro = "ferramenta"
            self.toggle_btn.configure(text="Cadastrar: Ferramenta")

        self.render_form()

    def render_form(self):
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        entry_width = 600
        entry_height = 40

        if self.tipo_cadastro == "ferramenta":
            self.codigo_entry = customtkinter.CTkEntry(self.form_frame,
                                                       placeholder_text="Código da Ferramenta",
                                                       width=entry_width,
                                                       height=entry_height,

            )
            self.codigo_entry.grid(row=0, column=0, pady=10)

            self.descricao_entry = customtkinter.CTkEntry(self.form_frame,
                                                          placeholder_text="Descrição",
                                                          width=entry_width,
                                                          height=entry_height
            )
            self.descricao_entry.grid(row=1, column=0, pady=10)

            self.quantidade_entry = customtkinter.CTkEntry(self.form_frame,
                                                          placeholder_text="Quantidade",
                                                          width=entry_width,
                                                          height=entry_height
                                                          )
            self.quantidade_entry.grid(row=2, column=0, pady=10)

        else:
            self.codigo_entry = customtkinter.CTkEntry(self.form_frame,
                                                       placeholder_text="Código da Matrícula",
                                                       width=entry_width,
                                                       height=entry_height

            )
            self.codigo_entry.grid(row=0, column=0, pady=10)

            self.nome_entry = customtkinter.CTkEntry(self.form_frame,
                                                     placeholder_text="Nome Completo",
                                                     width=entry_width,
                                                     height=entry_height

            )
            self.nome_entry.grid(row=1, column=0, pady=10)

            setores = [
                "Preventiva A", "Preventiva B", "Plantão A", "Plantão B",
                "Plantão C", "Plantão D", "Reparo", "RG", "Auxiliares", "MRO"
            ]

            self.setor_dropdown = customtkinter.CTkOptionMenu(
                self.form_frame,
                values=setores,
                text_color=("#FFFFFF", "#FFFFFF"),
                fg_color="#5E22F3",
                width=entry_width,
                height=entry_height,
            )
            self.setor_dropdown.set("Selecione o Setor")
            self.setor_dropdown.grid(row=2, column=0, pady=10)

    def cadastrar(self):
        if self.tipo_cadastro == "ferramenta":
            codigo = self.codigo_entry.get()
            descricao = self.descricao_entry.get()
            quantidade = self.quantidade_entry.get()

            self.cadastrar_ferramenta(ferramenta=codigo, descricao=descricao, quantidade=quantidade)

        else:
            codigo = self.codigo_entry.get()
            nome = self.nome_entry.get()
            setor = self.setor_dropdown.get()

            self.cadastrar_matricula(matricula_cadastro=codigo, nome_cadastro=nome,setor_cadastro=setor)

    def cadastrar_ferramenta(self, ferramenta, descricao, quantidade):

        cadastro = self.ferramenta_service.cadastrar(codigo=ferramenta,
                                          descricao=descricao,
                                          quantidade=quantidade)
        if cadastro == 1:
            CTkMessagebox(title="Cancelado",
                          message=f"{descricao} já existente e ativa no sistema")
            return None

        elif cadastro == 2:
            CTkMessagebox(title="Cancelado",
                          message=f"{descricao} já existente, porém desativada")
            return None

        else:
            CTkMessagebox(title="Sucesso", message=f"{descricao} cadastrado(a) com sucesso")
            return None

    def cadastrar_matricula(self, matricula_cadastro, nome_cadastro, setor_cadastro):

        cadastro = self.matricula_service.cadastrar(matricula_str=matricula_cadastro, nome=nome_cadastro, setor=setor_cadastro)

        if cadastro == 1:
            CTkMessagebox(title="Cancelado",
                          message=f"Matricula: {matricula_cadastro} já existente e ativa no sistema")
            return None

        elif cadastro == 2:
            CTkMessagebox(title="Cancelado",
                          message=f"Matricula: {matricula_cadastro} já existente, porém desativada")
            return None
        else:
            CTkMessagebox(title="Sucesso", message=f"Matricula: {matricula_cadastro} cadastrada com sucesso")
            return None
