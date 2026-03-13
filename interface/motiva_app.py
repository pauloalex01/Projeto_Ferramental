import customtkinter
from codigo_barras.decoder_cam import LeitorCodigo
from services.service import MatriculaService, FerramentaService, MovimentacaoService


class MotivaApp(customtkinter.CTk, LeitorCodigo, MovimentacaoService, MatriculaService, FerramentaService):

    matricula = MatriculaService()
    movimentacao = MovimentacaoService()
    ferramenta = FerramentaService()
    leitor = LeitorCodigo()

    def __init__(self):
        super().__init__()
        self.title("Motiva")
        self.geometry("1000x700")

        # Configuração do tema e cores
        customtkinter.set_appearance_mode("System")  # Pode ser "System", "Dark", "Light"
        
        # Definir o tema padrão para 'blue' e depois ajustar as cores dos widgets individualmente
        # para Branco/Anil (Light) e Preto/Branco (Dark)
        customtkinter.set_default_color_theme("blue")

        # Configurar layout da grade principal
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Frame de navegação (sidebar)
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0,
                                                         fg_color=("#5e22f3", "#1A1A1A")) # Branco para light, quase preto para dark
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="motiva",
                                                             compound="left", font=customtkinter.CTkFont(size=45,family="Sora", weight="bold"),
                                                             text_color=("#FFFFFF", "#FFFFFF")) # Preto para light, branco para dark
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões de navegação
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                   text="Início",
                                                   fg_color="transparent", text_color=("#FFFFFF", "#FFFFFF"),
                                                   hover_color=("#5e22f3", "#333333"), # Anil para light, cinza escuro para dark
                                                   anchor="w", command=self.home_button_event,
                                                   font=customtkinter.CTkFont(size=16,family="Sora", weight="bold"))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.matricula_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                        text="Matrícula",
                                                        fg_color="transparent", text_color=("#FFFFFF", "#FFFFFF"),
                                                        hover_color=("#5e22f3", "#333333"),
                                                        # Anil para light, cinza escuro para dark
                                                        anchor="w", command=self.matricula_button_event,
                                                        font=customtkinter.CTkFont(size=16, family="Sora", weight="bold"))
        self.matricula_button.grid(row=2, column=0, sticky="ew")

        self.ferramenta_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                         text="Ferramenta",
                                                         fg_color="transparent", text_color=("#FFFFFF", "#FFFFFF"),
                                                         hover_color=("#5e22f3", "#333333"),
                                                         # Anil para light, cinza escuro para dark
                                                         anchor="w", command=self.ferramenta_button_event,
                                                         font=customtkinter.CTkFont(size=16, family="Sora",weight="bold"))
        self.ferramenta_button.grid(row=3, column=0, sticky="ew")

        self.movimentacao_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                           text="Movimentação",
                                                           fg_color="transparent", text_color=("#FFFFFF", "#FFFFFF"),
                                                           hover_color=("#5e22f3", "#333333"),
                                                           # Anil para light, cinza escuro para dark
                                                           anchor="w", command=self.movimentacao_button_event,
                                                           font=customtkinter.CTkFont(size=16, family="Sora",weight="bold"))
        self.movimentacao_button.grid(row=4, column=0, sticky="ew")

        self.leitor_codigo_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                                            text="Leitor de Código",
                                                            fg_color="transparent", text_color=("#FFFFFF", "#FFFFFF"),
                                                            hover_color=("#5e22f3", "#333333"),
                                                            # Anil para light, cinza escuro para dark
                                                            anchor="w", command=self.leitor_codigo_button_event,
                                                            font=customtkinter.CTkFont(size=16, family="Sora",weight="bold"))
        self.leitor_codigo_button.grid(row=5, column=0, sticky="ew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Modo de Aparência:", anchor="w",
                                                            text_color=("#1A1A1A", "#FFFFFF"))
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event,
                                                                       fg_color=("#F8F8F8", "#1A1A1A"), # Fundo do menu
                                                                       button_color=("#5e22f3", "#FFFFFF"), # Anil para light, branco para dark
                                                                       button_hover_color=("#3c12a8", "#CCCCCC"), # Anil escuro para light, cinza claro para dark
                                                                       text_color=("#1A1A1A", "#FFFFFF"))
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20), sticky="ew")

        # Frames de conteúdo
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(self.home_frame, text="Ferramental Automático", font=customtkinter.CTkFont(size=24, family="Sora" ,weight="bold"),
                                                       text_color=("#1A1A1A", "#FFFFFF"))
        self.home_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.matricula_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.matricula_frame.grid_columnconfigure(0, weight=1)
        self.matricula_frame_label = customtkinter.CTkLabel(self.matricula_frame, text="Seção de Matrícula", font=customtkinter.CTkFont(size=24, weight="bold"),
                                                           text_color=("#1A1A1A", "#FFFFFF"))
        self.matricula_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.matricula_button_cadastrar = customtkinter.CTkButton(self.matricula_frame, text="Cadastrar Matrícula", command=self.cadastrar_matricula,
                                                                  fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.matricula_button_cadastrar.grid(row=1, column=0, padx=20, pady=10)
        self.matricula_button_atualizar = customtkinter.CTkButton(self.matricula_frame, text="Atualizar Matrícula", command=self.atualizar_matricula,
                                                                  fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.matricula_button_atualizar.grid(row=2, column=0, padx=20, pady=10)
        self.matricula_button_remover = customtkinter.CTkButton(self.matricula_frame, text="Remover Matrícula", command=self.remover_matricula,
                                                                fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.matricula_button_remover.grid(row=3, column=0, padx=20, pady=10)
        self.matricula_button_ler = customtkinter.CTkButton(self.matricula_frame, text="Ler Matrícula", command=self.ler_matricula,
                                                            fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.matricula_button_ler.grid(row=4, column=0, padx=20, pady=10)

        self.ferramenta_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ferramenta_frame.grid_columnconfigure(0, weight=1)
        self.ferramenta_frame_label = customtkinter.CTkLabel(self.ferramenta_frame, text="Seção de Ferramenta", font=customtkinter.CTkFont(size=24, weight="bold"),
                                                           text_color=("#1A1A1A", "#FFFFFF"))
        self.ferramenta_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.ferramenta_button_cadastrar = customtkinter.CTkButton(self.ferramenta_frame, text="Cadastrar Ferramenta", command=self.cadastrar_ferramenta,
                                                                   fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.ferramenta_button_cadastrar.grid(row=1, column=0, padx=20, pady=10)
        self.ferramenta_button_atualizar = customtkinter.CTkButton(self.ferramenta_frame, text="Atualizar Ferramenta", command=self.atualizar_ferramenta,
                                                                   fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.ferramenta_button_atualizar.grid(row=2, column=0, padx=20, pady=10)
        self.ferramenta_button_remover = customtkinter.CTkButton(self.ferramenta_frame, text="Remover Ferramenta", command=self.remover_ferramenta,
                                                                 fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.ferramenta_button_remover.grid(row=3, column=0, padx=20, pady=10)
        self.ferramenta_button_ler = customtkinter.CTkButton(self.ferramenta_frame, text="Ler Ferramenta", command=self.ler_ferramenta,
                                                             fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.ferramenta_button_ler.grid(row=4, column=0, padx=20, pady=10)

        self.movimentacao_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.movimentacao_frame.grid_columnconfigure(0, weight=1)
        self.movimentacao_frame_label = customtkinter.CTkLabel(self.movimentacao_frame, text="Seção de Movimentação", font=customtkinter.CTkFont(size=24, weight="bold"),
                                                           text_color=("#1A1A1A", "#FFFFFF"))
        self.movimentacao_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.movimentacao_button_emprestar = customtkinter.CTkButton(self.movimentacao_frame, text="Emprestar Ferramenta", command=self.emprestar_ferramenta,
                                                                     fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.movimentacao_button_emprestar.grid(row=1, column=0, padx=20, pady=10)
        self.movimentacao_button_devolver = customtkinter.CTkButton(self.movimentacao_frame, text="Devolver Ferramenta", command=self.devolver_ferramenta,
                                                                    fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.movimentacao_button_devolver.grid(row=2, column=0, padx=20, pady=10)

        self.leitor_codigo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.leitor_codigo_frame.grid_columnconfigure(0, weight=1)
        self.leitor_codigo_frame_label = customtkinter.CTkLabel(self.leitor_codigo_frame, text="Seção de Leitor de Código", font=customtkinter.CTkFont(size=24, weight="bold"),
                                                           text_color=("#1A1A1A", "#FFFFFF"))
        self.leitor_codigo_frame_label.grid(row=0, column=0, padx=20, pady=20)
        self.leitor_codigo_button_iniciar = customtkinter.CTkButton(self.leitor_codigo_frame, text="Iniciar Leitor de Código", command=self.iniciar_leitor_codigo,
                                                                    fg_color=("#4169E1", "#FFFFFF"), text_color=("#FFFFFF", "#1A1A1A"), hover_color=("#365BC9", "#CCCCCC"))
        self.leitor_codigo_button_iniciar.grid(row=1, column=0, padx=20, pady=10)

        # Selecionar frame inicial
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # Definir cor de fundo do botão para o frame selecionado
        # Usando fg_color com tupla para suportar modos claro/escuro


        self.home_button.configure(fg_color=("#000000", "#333333") if name == "home" else "transparent")
        self.matricula_button.configure(fg_color=("#000000", "#333333") if name == "matricula" else "transparent")
        self.ferramenta_button.configure(fg_color=("#000000", "#333333") if name == "ferramenta" else "transparent")
        self.movimentacao_button.configure(fg_color=("#000000", "#333333") if name == "movimentacao" else "transparent")
        self.leitor_codigo_button.configure(fg_color=("#000000", "#333333") if name == "leitor_codigo" else "transparent")

        # Mostrar o frame selecionado e esconder os outros
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "matricula":
            self.matricula_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.matricula_frame.grid_forget()
        if name == "ferramenta":
            self.ferramenta_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ferramenta_frame.grid_forget()
        if name == "movimentacao":
            self.movimentacao_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.movimentacao_frame.grid_forget()
        if name == "leitor_codigo":
            self.leitor_codigo_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.leitor_codigo_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def matricula_button_event(self):
        self.select_frame_by_name("matricula")

    def ferramenta_button_event(self):
        self.select_frame_by_name("ferramenta")

    def movimentacao_button_event(self):
        self.select_frame_by_name("movimentacao")

    def leitor_codigo_button_event(self):
        self.select_frame_by_name("leitor_codigo")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Métodos placeholder para as funcionalidades
    def cadastrar_matricula(self):
        matricula_input = customtkinter.CTkInputDialog(text="Digite sua matrícula:", title="Cadastro de Matrícula")
        matricula_cadastro = matricula_input.get_input()

        nome_input = customtkinter.CTkInputDialog(text="Digite seu nome:", title="Cadastro de Matrícula")
        nome_cadastro = nome_input.get_input()
        self.matricula.cadastrar(matricula_cadastro, nome_cadastro)
        print("Cadastrar Matrícula clicado")
        # Anexar método da classe Matrícula aqui

    def atualizar_matricula(self):
        print("Atualizar Matrícula clicado")
        # Anexar método da classe Matrícula aqui

    def remover_matricula(self):
        print("Remover Matrícula clicado")
        # Anexar método da classe Matrícula aqui

    def ler_matricula(self):
        print("Ler Matrícula clicado")
        # Anexar método da classe Matrícula aqui

    def cadastrar_ferramenta(self):
        print("Cadastrar Ferramenta clicado")
        # Anexar método da classe Ferramenta aqui

    def atualizar_ferramenta(self):
        print("Atualizar Ferramenta clicado")
        # Anexar método da classe Ferramenta aqui

    def remover_ferramenta(self):
        print("Remover Ferramenta clicado")
        # Anexar método da classe Ferramenta aqui

    def ler_ferramenta(self):
        print("Ler Ferramenta clicado")
        # Anexar método da classe Ferramenta aqui

    def emprestar_ferramenta(self):
        print("Emprestar Ferramenta clicado")
        # Anexar método da classe Movimentação aqui

    def devolver_ferramenta(self):
        print("Devolver Ferramenta clicado")
        # Anexar método da classe Movimentação aqui

    def iniciar_leitor_codigo(self):
        print("Iniciando Leitor de Código...")
        self.leitor.executar()
        self.messagebox = customtkinter.CTk()

        # Anexar método da classe Leitor_codigo aqui


if __name__ == "__main__":
    app = MotivaApp()
    app.mainloop()
