import customtkinter
from codigo_barras.decoder_cam import LeitorCodigo
from repositories.repositories import MatriculaRepository, FerramentaRepository
from services.service import MatriculaService, FerramentaService, MovimentacaoService
from CTkMessagebox import CTkMessagebox


class MotivaApp(customtkinter.CTk, LeitorCodigo, MovimentacaoService, MatriculaService, FerramentaService):

    matricula_repo = MatriculaRepository()
    ferramenta_repo = FerramentaRepository()
    matricula = MatriculaService()
    movimentacao = MovimentacaoService()
    ferramenta = FerramentaService()
    leitor = LeitorCodigo()

    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_layout_grid()
        self.create_navigation_sidebar()
        self.create_content_frames()

        # Selecionar frame inicial
        self.select_frame_by_name("home")

    def setup_window(self):
        """Configurações básicas da janela principal."""
        self.title("Motiva")
        self.geometry("1000x700")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

    def setup_layout_grid(self):
        """Configura a grade principal da aplicação."""
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def create_navigation_sidebar(self):
        """Cria e configura a barra lateral de navegação."""
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0,
                                                       fg_color=("#5e22f3", "#1A1A1A"))
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text="motiva",
            compound="left", font=customtkinter.CTkFont(size=45, family="Sora", weight="bold"),
            text_color=("#FFFFFF", "#FFFFFF")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Botões de navegação
        self.setup_navigation_buttons()

        # Controle de aparência
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.navigation_frame, text="Modo de Aparência:", anchor="w",
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.navigation_frame, values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event,
            fg_color=("#F8F8F8", "#1A1A1A"),
            button_color=("#5e22f3", "#FFFFFF"),
            button_hover_color=("#3c12a8", "#CCCCCC"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 20), sticky="ew")

    def setup_navigation_buttons(self):
        """Configura os botões da barra lateral."""
        button_font = customtkinter.CTkFont(size=16, family="Sora", weight="bold")
        common_args = {
            "master": self.navigation_frame,
            "corner_radius": 0,
            "height": 40,
            "border_spacing": 10,
            "fg_color": "transparent",
            "text_color": ("#FFFFFF", "#FFFFFF"),
            "hover_color": ("#5e22f3", "#333333"),
            "anchor": "w",
            "font": button_font
        }

        self.home_button = customtkinter.CTkButton(text="Início", command=self.home_button_event, **common_args)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.matricula_button = customtkinter.CTkButton(text="Matrícula", command=self.matricula_button_event,
                                                        **common_args)
        self.matricula_button.grid(row=2, column=0, sticky="ew")

        self.ferramenta_button = customtkinter.CTkButton(text="Ferramenta", command=self.ferramenta_button_event,
                                                         **common_args)
        self.ferramenta_button.grid(row=3, column=0, sticky="ew")

        self.movimentacao_button = customtkinter.CTkButton(text="Movimentação", command=self.movimentacao_button_event,
                                                           **common_args)
        self.movimentacao_button.grid(row=4, column=0, sticky="ew")

        self.leitor_codigo_button = customtkinter.CTkButton(text="Leitor de Código",
                                                            command=self.leitor_codigo_button_event, **common_args)
        self.leitor_codigo_button.grid(row=5, column=0, sticky="ew")

    def create_content_frames(self):
        """Inicializa todos os frames de conteúdo."""
        self.setup_home_frame()
        self.setup_matricula_frame()
        self.setup_ferramenta_frame()
        self.setup_movimentacao_frame()
        self.setup_leitor_codigo_frame()

    def setup_home_frame(self):
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_label = customtkinter.CTkLabel(
            self.home_frame, text="Ferramental Automático",
            font=customtkinter.CTkFont(size=24, family="Sora", weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.home_frame_label.grid(row=0, column=0, padx=20, pady=20)

    def setup_matricula_frame(self):
        self.matricula_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.matricula_frame.grid_columnconfigure(0, weight=1)
        self.matricula_frame_label = customtkinter.CTkLabel(
            self.matricula_frame, text="Seção de Matrícula",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.matricula_frame_label.grid(row=0, column=0, padx=20, pady=20)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.matricula_button_cadastrar = customtkinter.CTkButton(self.matricula_frame, text="Cadastrar Matrícula",
                                                                  command=self.cadastrar_matricula, **btn_args)
        self.matricula_button_cadastrar.grid(row=1, column=0, padx=20, pady=10)

        self.matricula_button_atualizar = customtkinter.CTkButton(self.matricula_frame, text="Atualizar Matrícula",
                                                                  command=self.atualizar_matricula, **btn_args)
        self.matricula_button_atualizar.grid(row=2, column=0, padx=20, pady=10)

        self.matricula_button_remover = customtkinter.CTkButton(self.matricula_frame, text="Remover Matrícula",
                                                                command=self.remover_matricula, **btn_args)
        self.matricula_button_remover.grid(row=3, column=0, padx=20, pady=10)

        self.matricula_button_ler = customtkinter.CTkButton(self.matricula_frame, text="Ler Matrícula",
                                                            command=self.ler_matricula, **btn_args)
        self.matricula_button_ler.grid(row=4, column=0, padx=20, pady=10)

        self.matricula_button_ativar= customtkinter.CTkButton(self.matricula_frame, text="Ativar Matrícula",
                                                              command=self.ativar_matricula, **btn_args)

        self.matricula_button_ativar.grid(row=5, column=0, padx=20, pady=10)

    def setup_ferramenta_frame(self):
        self.ferramenta_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ferramenta_frame.grid_columnconfigure(0, weight=1)
        self.ferramenta_frame_label = customtkinter.CTkLabel(
            self.ferramenta_frame, text="Seção de Ferramenta",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.ferramenta_frame_label.grid(row=0, column=0, padx=20, pady=20)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.ferramenta_button_cadastrar = customtkinter.CTkButton(self.ferramenta_frame, text="Cadastrar Ferramenta",
                                                                   command=self.cadastrar_ferramenta, **btn_args)
        self.ferramenta_button_cadastrar.grid(row=1, column=0, padx=20, pady=10)

        self.ferramenta_button_atualizar = customtkinter.CTkButton(self.ferramenta_frame, text="Atualizar Ferramenta",
                                                                   command=self.atualizar_ferramenta, **btn_args)
        self.ferramenta_button_atualizar.grid(row=2, column=0, padx=20, pady=10)

        self.ferramenta_button_remover = customtkinter.CTkButton(self.ferramenta_frame, text="Remover Ferramenta",
                                                                 command=self.remover_ferramenta, **btn_args)
        self.ferramenta_button_remover.grid(row=3, column=0, padx=20, pady=10)

        self.ferramenta_button_ler = customtkinter.CTkButton(self.ferramenta_frame, text="Ler Ferramenta",
                                                             command=self.ler_ferramenta, **btn_args)
        self.ferramenta_button_ler.grid(row=4, column=0, padx=20, pady=10)

        self.ferramenta_button_ativar = customtkinter.CTkButton(self.ferramenta_frame, text="Ativar Ferramenta",
                                                                command=self.ativar_ferramenta, **btn_args)

        self.ferramenta_button_ativar.grid(row=5, column=0, padx=20, pady=10)

    def setup_movimentacao_frame(self):
        self.movimentacao_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.movimentacao_frame.grid_columnconfigure(0, weight=1)
        self.movimentacao_frame_label = customtkinter.CTkLabel(
            self.movimentacao_frame, text="Seção de Movimentação",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.movimentacao_frame_label.grid(row=0, column=0, padx=20, pady=20)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.movimentacao_button_emprestar = customtkinter.CTkButton(self.movimentacao_frame,
                                                                     text="Emprestar Ferramenta",
                                                                     command=self.emprestar_ferramenta, **btn_args)

        self.movimentacao_button_emprestar.grid(row=1, column=0, padx=20, pady=10)

        self.movimentacao_button_devolver = customtkinter.CTkButton(self.movimentacao_frame, text="Devolver Ferramenta",
                                                                    command=self.devolver_ferramenta, **btn_args)
        self.movimentacao_button_devolver.grid(row=2, column=0, padx=20, pady=10)

    def setup_leitor_codigo_frame(self):
        self.leitor_codigo_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.leitor_codigo_frame.grid_columnconfigure(0, weight=1)
        self.leitor_codigo_frame_label = customtkinter.CTkLabel(
            self.leitor_codigo_frame, text="Seção de Leitor de Código",
            font=customtkinter.CTkFont(size=24, weight="bold"),
            text_color=("#1A1A1A", "#FFFFFF")
        )
        self.leitor_codigo_frame_label.grid(row=0, column=0, padx=20, pady=20)

        btn_args = {"fg_color": ("#4169E1", "#FFFFFF"), "text_color": ("#FFFFFF", "#1A1A1A"),
                    "hover_color": ("#365BC9", "#CCCCCC")}

        self.leitor_codigo_button_iniciar = customtkinter.CTkButton(self.leitor_codigo_frame,
                                                                    text="Iniciar Leitor de Código",
                                                                    command=self.iniciar_leitor_codigo, **btn_args)
        self.leitor_codigo_button_iniciar.grid(row=1, column=0, padx=20, pady=10)

    def select_frame_by_name(self, name):
        # Atualiza cores dos botões de navegação
        self.home_button.configure(fg_color=("#000000", "#333333") if name == "home" else "transparent")
        self.matricula_button.configure(fg_color=("#000000", "#333333") if name == "matricula" else "transparent")
        self.ferramenta_button.configure(fg_color=("#000000", "#333333") if name == "ferramenta" else "transparent")
        self.movimentacao_button.configure(fg_color=("#000000", "#333333") if name == "movimentacao" else "transparent")
        self.leitor_codigo_button.configure(
            fg_color=("#000000", "#333333") if name == "leitor_codigo" else "transparent")

        # Gerencia visibilidade dos frames
        frames = {
            "home": self.home_frame,
            "matricula": self.matricula_frame,
            "ferramenta": self.ferramenta_frame,
            "movimentacao": self.movimentacao_frame,
            "leitor_codigo": self.leitor_codigo_frame
        }

        for frame_name, frame_obj in frames.items():
            if frame_name == name:
                frame_obj.grid(row=0, column=1, sticky="nsew")
            else:
                frame_obj.grid_forget()

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

    # Métodos de serviço (Lógica de Negócio)
    def cadastrar_matricula(self):

        matricula_input = customtkinter.CTkInputDialog(text="Digite sua matrícula:", title="Cadastro de Matrícula")
        matricula_cadastro = matricula_input.get_input()

        if not matricula_cadastro: return None

        nome_input = customtkinter.CTkInputDialog(text="Digite seu nome:", title="Cadastro de Matrícula")
        nome_cadastro = nome_input.get_input()

        if not nome_cadastro: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Matricula: {matricula_cadastro}, Nome: {nome_cadastro}",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            busca = self.matricula.cadastrar(matricula_cadastro, nome_cadastro)
            if busca == 1:
                CTkMessagebox(title="Cancelado",
                              message=f"Matricula: {matricula_cadastro} já existente e ativa no sistema")
            elif busca == 2:
                CTkMessagebox(title="Cancelado",
                              message=f"Matricula: {matricula_cadastro} já existente, porém desativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {matricula_cadastro} cadastrada com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Cadastro Cancelado")

    def atualizar_matricula(self):
        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula cujo nome será atualizado:",
                                                       title="Mudança de nome")
        matricula = matricula_input.get_input()

        if not matricula: return None

        nome_data = self.matricula_repo.buscar_por_matricula(matricula)

        if nome_data:
            nome_atual = nome_data[2]
        else:
            nome_atual = None


        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja substituir o nome {nome_atual} ?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            nome_input = customtkinter.CTkInputDialog(text="Digite o novo nome:", title="Mudança de nome")
            nome_novo = nome_input.get_input()

            if self.matricula.atualizar(matricula, nome_novo) == 1:
                CTkMessagebox(title="Sucesso!", message="Atualização realizada com sucesso")
            else:
                CTkMessagebox(title="Erro", message="Matricula está desativada")
        else:
            CTkMessagebox(title="Cancelado", message="Atualização foi cancelada")

    def remover_matricula(self):
        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula a ser desativada:",
                                                       title="Desativação de Matrícula")
        matricula_busca = matricula_input.get_input()

        if not matricula_busca: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja desativar a Matricula: {matricula_busca}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            remocao = self.matricula.remover(matricula_busca)

            if remocao == 1:
                CTkMessagebox(title="Erro", message="Matricula não encontrada")
            elif remocao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está desativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {matricula_busca} removida com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Desativação foi cancelada")

    def ler_matricula(self):

        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula a ser procurada:",
                                                       title="Busca de Matrícula")
        matricula_busca = matricula_input.get_input()

        if not matricula_busca: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja buscar a Matricula: {matricula_busca}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            busca = self.matricula.buscar(matricula_busca)

            if busca == 1:
                CTkMessagebox(title="Erro", message="Matricula não encontrada")
            else:

                CTkMessagebox(title="Sucesso", message=f"Matricula: {matricula_busca} removida com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Desativação foi cancelada")

    def ativar_matricula(self):

        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula a ser ativada:",
                                                       title="Ativação de Matrícula")
        ferramenta_ativacao = matricula_input.get_input()

        if not ferramenta_ativacao: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja ativar a Matricula: {ferramenta_ativacao}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            ativacao = self.matricula.ativar(ferramenta_ativacao)

            if ativacao == 1:
                CTkMessagebox(title="Erro", message="Matricula não encontrada")
            elif ativacao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está ativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {ferramenta_ativacao} ativada com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Ativação foi cancelada")

    def cadastrar_ferramenta(self):

        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta:", title="Cadastro de Ferramenta")
        ferramenta_cadastro = ferramenta_input.get_input()

        if not ferramenta_cadastro: return None

        descricao_input = customtkinter.CTkInputDialog(text="Digite a descrição da ferramenta:", title="Cadastro de Ferramenta")
        descricao_cadastro = descricao_input.get_input()

        if not descricao_cadastro: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Ferramenta: {ferramenta_cadastro}, Descrição: {descricao_cadastro}",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            busca = self.ferramenta.cadastrar(ferramenta_cadastro, descricao_cadastro)
            if busca == 1:
                CTkMessagebox(title="Cancelado",
                              message=f"{descricao_cadastro} já existente e ativa no sistema")
            elif busca == 2:
                CTkMessagebox(title="Cancelado",
                              message=f"{descricao_cadastro} já existente, porém desativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"{descricao_cadastro} cadastrado(a) com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Cadastro Cancelado")

    def atualizar_ferramenta(self):
        print("Atualizar Ferramenta clicado")

    def remover_ferramenta(self):
        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta a ser desativada:",
                                                       title="Desativação de Ferramenta")
        ferramenta_remocao = ferramenta_input.get_input()

        if not ferramenta_remocao: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja desativar a ferramenta: {ferramenta_remocao}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            remocao = self.ferramenta.remover(ferramenta_remocao)

            if remocao == 1:
                CTkMessagebox(title="Erro", message="Ferramenta não encontrada")
            elif remocao == 2:
                CTkMessagebox(title="Erro", message="Ferramenta já está desativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"Ferramenta: {ferramenta_remocao} removida com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Desativação foi cancelada")


    def ler_ferramenta(self):
        print("Ler Ferramenta clicado")

    def ativar_ferramenta(self):

        ferramenta_input = customtkinter.CTkInputDialog(text="Digite a matrícula a ser ativada:",
                                                       title="Ativação de Matrícula")
        ferramenta_ativacao = ferramenta_input.get_input()

        if not ferramenta_ativacao: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja ativar a Matricula: {ferramenta_ativacao}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            ativacao = self.ferramenta.ativar(ferramenta_ativacao)

            if ativacao == 1:
                CTkMessagebox(title="Erro", message="Matricula não encontrada")
            elif ativacao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está ativada")
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {ferramenta_ativacao} ativada com sucesso")
        else:
            CTkMessagebox(title="Cancelado", message="Ativação foi cancelada")

    def emprestar_ferramenta(self):
        print("Emprestar Ferramenta clicado")

    def devolver_ferramenta(self):
        print("Devolver Ferramenta clicado")

    def iniciar_leitor_codigo(self):

        aviso = CTkMessagebox(icon="info", message="Pressione ESC para fechar a câmera", title="Aviso", option_1="Entendido")

        if aviso.get() == "Entendido":
            codigos = self.leitor.executar()

        else: return None

        if codigos:
            codigos_texto = "\n".join(codigos[:10])
            mensagem = CTkMessagebox(icon="question",
                                     message=f"Códigos lidos estão corretos?\n{codigos_texto}",
                                     option_1="Sim",
                                     option_2="Não",
                                     title="Aviso")

            if mensagem.get() == "Sim":

                matricula = customtkinter.CTkInputDialog(text="Digite sua matrícula para realizar o empréstimo:",
                                                         title="Matrícula para empréstimo")
                matricula_emprestimo = matricula.get_input()

                validacao = CTkMessagebox(icon="question",
                                          message=f"Deseja devolver ou emprestar?",
                                          option_1="Devolver",
                                          option_2="Emprestar",
                                          title="Empréstimo ou Devolução")

                escolha = validacao.get()


                if escolha == "Emprestar":
                    for codigo in codigos:
                        self.movimentacao.emprestar(ferramenta_codigo=codigo, matricula_codigo=matricula_emprestimo)

                else:
                    for codigo in codigos:
                        self.movimentacao.devolver(matricula=matricula_emprestimo,ferramenta=codigo)


            """
                if not self.ferramenta_repo.buscar_por_codigo(codigos):

                    busca = self.matricula_repo.buscar_por_matricula_ativo(matricula_emprestimo)

                    return print(busca) if busca else print(2)

                else:
                    CTkMessagebox(icon="error",message="Código não registrado")
            """



if __name__ == "__main__":
    app = MotivaApp()
    app.mainloop()