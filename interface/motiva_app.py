import customtkinter
from codigo_barras.decoder_cam import LeitorCodigo
from interface.frames import BuscaFrame
from interface.frames import CadastroFrame
from repositories.repositories import MatriculaRepository, FerramentaRepository
from services.service import MatriculaService, FerramentaService, MovimentacaoService
from CTkMessagebox import CTkMessagebox
from database.banco_de_dados import Database
from tkinter import ttk


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
            text_color=("#FFFFFF", "#FFFFFF")
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

        self.cadastro_button = customtkinter.CTkButton(text="Cadastro", command=self.cadastro_button_event, **common_args)
        self.cadastro_button.grid(row=2, column=0, sticky="ew")

        self.busca_button = customtkinter.CTkButton(text="Busca", command=self.busca_button_event,
                                                       **common_args)
        self.busca_button.grid(row=3, column=0, sticky="ew")

        self.movimentacao_button = customtkinter.CTkButton(text="Movimentação", command=self.movimentacao_button_event,
                                                           **common_args)
        self.movimentacao_button.grid(row=4, column=0, sticky="ew")

        self.leitor_codigo_button = customtkinter.CTkButton(text="Leitor de Código",
                                                            command=self.leitor_codigo_button_event, **common_args)
        self.leitor_codigo_button.grid(row=5, column=0, sticky="ew")

    def create_content_frames(self):
        """Inicializa todos os frames de conteúdo."""
        self.setup_home_frame()
        self.setup_cadastro_frame()
        self.setup_busca_frame()
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
        # Frame do histórico
        self.historico_frame = customtkinter.CTkFrame(self.home_frame)
        self.historico_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

        self.home_frame.grid_rowconfigure(1, weight=1)

        historico_label = customtkinter.CTkLabel(
            self.home_frame,
            text="Últimas Movimentações",
            font=customtkinter.CTkFont(size=18, weight="bold")
        )

        historico_label.grid(row=1, column=0, pady=(10, 0))

        self.criar_tabela_historico()



    def criar_tabela_historico(self):

        colunas = ("Ferramenta", "Matrícula", "Quantidade", "Retirada", "Devolução")

        self.historico_tabela = ttk.Treeview(
            self.historico_frame,
            columns=colunas,
            show="headings",
            height=10
        )

        for col in colunas:
            self.historico_tabela.heading(col, text=col)
            self.historico_tabela.column(col, anchor="center")

        self.historico_tabela.grid(row=0, column=0, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.historico_frame, orient="vertical", command=self.historico_tabela.yview)
        self.historico_tabela.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky="ns")

        dados = self.movimentacao.carregar_historico()

        for row in dados:
            self.historico_tabela.insert("", "end", values=row)

    def setup_cadastro_frame(self):

        self.cadastro_frame = CadastroFrame(self, self.matricula, self.ferramenta)

        self.cadastro_frame.grid(row=0, column=1, sticky="nsew")

    def setup_busca_frame(self):

        self.busca_frame = BuscaFrame(self, self.matricula, self.ferramenta)
        self.busca_frame.grid(row=1, column=1, sticky="nsew")

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
        self.cadastro_button.configure(fg_color=("#000000", "#333333") if name == "cadastro" else "transparent")
        self.movimentacao_button.configure(fg_color=("#000000", "#333333") if name == "movimentacao" else "transparent")
        self.leitor_codigo_button.configure(
            fg_color=("#000000", "#333333") if name == "leitor_codigo" else "transparent")

        # Gerencia visibilidade dos frames
        frames = {
            "home": self.home_frame,
            "cadastro": self.cadastro_frame,
            "busca": self.busca_frame,
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

    def cadastro_button_event(self):
        self.select_frame_by_name("cadastro")

    def busca_button_event(self):
        self.select_frame_by_name("busca")

    def movimentacao_button_event(self):
        self.select_frame_by_name("movimentacao")

    def leitor_codigo_button_event(self):
        self.select_frame_by_name("leitor_codigo")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Métodos de serviço (Lógica de Negócio)
    def atualizar_home(self):

        opcao_input = CTkMessagebox(message="Deseja atualizar a matrícula ou a ferramenta",
                                                   title="Atualização",
                                                   icon="question",
                                                   option_1="Matrícula",
                                                   option_2="Ferramenta")
        opcao_cadastro = opcao_input.get()

        if not opcao_cadastro: return None

        elif opcao_cadastro == "Matrícula": return self.atualizar_matricula()
        elif opcao_cadastro == "Ferramenta": return self.atualizar_ferramenta()

        return None

    def remover_home(self):

        opcao_input = CTkMessagebox(message="Deseja remover a matrícula ou a ferramenta",
                                                   title="Remoção",
                                                   icon="question",
                                                   option_1="Matrícula",
                                                   option_2="Ferramenta")
        opcao_cadastro = opcao_input.get()

        if not opcao_cadastro: return None

        elif opcao_cadastro == "Matrícula": return self.remover_matricula()
        elif opcao_cadastro == "Ferramenta": return self.remover_ferramenta()

        return None

    def ativar_home(self):

        opcao_input = CTkMessagebox(message="Deseja ativar a matrícula ou a ferramenta",
                                    title="Ativação",
                                    icon="question",
                                    option_1="Matrícula",
                                    option_2="Ferramenta")
        opcao_cadastro = opcao_input.get()

        if not opcao_cadastro:
            return None

        elif opcao_cadastro == "Matrícula":
            return self.ativar_matricula()
        elif opcao_cadastro == "Ferramenta":
            return self.ativar_ferramenta()

        return None

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
                return None
            else:
                CTkMessagebox(title="Erro", message="Matricula está desativada")
                return None
        else:
            CTkMessagebox(title="Cancelado", message="Atualização foi cancelada")
            return None


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
                return None

            elif remocao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está desativada")
                return None
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {matricula_busca} removida com sucesso")
                return None
        else:
            CTkMessagebox(title="Cancelado", message="Desativação foi cancelada")
            return None

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
                return None

            elif ativacao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está ativada")
                return None

            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {ferramenta_ativacao} ativada com sucesso")
                return None
        else:
            CTkMessagebox(title="Cancelado", message="Ativação foi cancelada")
            return None

    def atualizar_ferramenta(self):

        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta a ser atualizada:",
                                                        title="Mudança de Descrição")
        ferramenta_atualizacao = ferramenta_input.get_input()

        if not ferramenta_atualizacao: return None

        codigo_descricao = self.ferramenta.buscar(ferramenta_atualizacao)

        if codigo_descricao:
            codigo_descricao = codigo_descricao[2]
        else:
            codigo_descricao = None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja mudar a descrição da ferramenta: {codigo_descricao}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")

        if mensagem.get() == "Sim":
            descricao_input = customtkinter.CTkInputDialog(text="Digite a nova descricao:", title="Mudança de Descricao")
            descricao_atualizacao = descricao_input.get_input()



            if self.ferramenta.atualizar(ferramenta_codigo=ferramenta_atualizacao, descricao=descricao_atualizacao) == 2:
                CTkMessagebox(title="Erro", message="Ferramenta não encontrada")
                return None
            elif self.ferramenta.atualizar(ferramenta_codigo=ferramenta_atualizacao, descricao=descricao_atualizacao) == 0:
                CTkMessagebox(title="Sucesso", message=f"Ferramenta atualizada com sucesso")
                return None
            else:
                CTkMessagebox(title="Erro", message="Ferramenta está desativada")
                return None

        else:
            CTkMessagebox(title="Cancelado", message="Atualização foi cancelada")
            return None


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
                return None

            elif remocao == 2:
                CTkMessagebox(title="Erro", message="Ferramenta já está desativada")
                return None

            else:
                CTkMessagebox(title="Sucesso", message=f"Ferramenta: {ferramenta_remocao} removida com sucesso")
                return None
        else:
            CTkMessagebox(title="Cancelado", message="Desativação foi cancelada")
            return None

    def ativar_ferramenta(self):

        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta a ser ativada:",
                                                       title="Ativação de Ferramenta")
        ferramenta_ativacao = ferramenta_input.get_input()


        if not ferramenta_ativacao: return None

        mensagem = CTkMessagebox(title="Confirmação",
                                 message=f"Deseja ativar esta ferramenta: {ferramenta_ativacao}?",
                                 icon="question",
                                 option_1="Sim",
                                 option_2="Não")
        if mensagem.get() == "Sim":
            ativacao = self.ferramenta.ativar(ferramenta_ativacao)

            if ativacao == 1:
                CTkMessagebox(title="Erro", message="Matricula não encontrada")
                return None
            elif ativacao == 2:
                CTkMessagebox(title="Erro", message="Matricula já está ativada")
                return None
            else:
                CTkMessagebox(title="Sucesso", message=f"Matricula: {ferramenta_ativacao} ativada com sucesso")
                return None
        else:
            CTkMessagebox(title="Cancelado", message="Ativação foi cancelada")
            return None


    def emprestar_ferramenta(self):

        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta a ser emprestada:",
                                                        title="Empréstimo")
        ferramenta_emprestada = ferramenta_input.get_input()

        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula a ser atribuido o empréstimo:",
                                                       title="Empréstimo")
        matricula_emprestimo = matricula_input.get_input()

        quantidade_input = customtkinter.CTkInputDialog(text="Digite a quantidade da ferramenta a ser emprestada:",
                                                       title="Empréstimo")
        quantidade_emprestimo = quantidade_input.get_input()

        emprestimo = self.movimentacao.emprestar(ferramenta_codigo=ferramenta_emprestada,
                                                 matricula_codigo=matricula_emprestimo,
                                                 quantidade=quantidade_emprestimo)

        if emprestimo:

            if emprestimo == 1:
                CTkMessagebox(title="Erro", message="Matrícula não encontrada")
                return None
            elif emprestimo == 2:
                CTkMessagebox(title="Erro", message=f"Ferramenta não encontrada")
                return None
            elif emprestimo == 3:
                CTkMessagebox(title="Erro", message=f"Ferramenta já foi emprestada")
                return None
            else:
                CTkMessagebox(title="Sucesso", message=f"A movimentacao foi registrada")
                return None
        return None

    def devolver_ferramenta(self):
        ferramenta_input = customtkinter.CTkInputDialog(text="Digite o código da ferramenta a ser devolvida:",
                                                        title="Devolução")
        ferramenta_devolucao = ferramenta_input.get_input()

        matricula_input = customtkinter.CTkInputDialog(text="Digite a matrícula a qual foi atribuída o empréstimo:",
                                                       title="Devolução")
        matricula_devolucao = matricula_input.get_input()

        quantidade_input = customtkinter.CTkInputDialog(text="Digite a quantidade a ser devolvida:",
                                                       title="Devolução")
        quantidade_devolucao = quantidade_input.get_input()

        devolucao = self.movimentacao.emprestar(ferramenta_codigo=ferramenta_devolucao,
                                                 matricula_codigo=matricula_devolucao,
                                                 quantidade=quantidade_devolucao)

        if devolucao == 1:

            if devolucao == 1:
                CTkMessagebox(title="Erro", message="Matrícula não encontrada")
                return None
            elif devolucao == 2:
                CTkMessagebox(title="Erro", message=f"Ferramenta não encontrada")
                return None
            elif devolucao == 3:
                CTkMessagebox(title="Erro", message=f"Ferramenta já foi emprestada")
                return None
            else:
                CTkMessagebox(title="Sucesso", message=f"A movimentacao foi registrada")
                return None
        return None


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
                        self.movimentacao.emprestar(matricula_codigo=matricula_emprestimo, ferramenta_codigo=codigo, quantidade="1")

                else:
                    for codigo in codigos:
                        self.movimentacao.devolver(matricula=matricula_emprestimo, ferramenta=codigo, quantidade=1)

        return None


if __name__ == "__main__":
    database = Database()
    database.criar_banco()
    app = MotivaApp()
    app.mainloop()
