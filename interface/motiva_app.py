import customtkinter
from codigo_barras.decoder_cam import LeitorCodigo
from services.service import *
from CTkMessagebox import CTkMessagebox
from database.banco_de_dados import Database
from frames.CadastroFrame import CadastroFrame
from frames.MovimentacaoFrame import MovimentacaoFrame
from frames.BuscarFrame import BuscaFrame

class MotivaApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.matricula = MatriculaService()
        self.movimentacao = MovimentacaoService()
        self.ferramenta = FerramentaService()
        self.leitor = LeitorCodigo()

        self.setup_window()
        self.setup_layout_grid()
        self.create_navigation_sidebar()
        self.create_content_frames()

        self.select_frame_by_name("home")

    def setup_window(self):
        self.title("Motiva")
        self.geometry("1000x700")
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("blue")

    def setup_layout_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def create_navigation_sidebar(self):
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

        self.home_button = customtkinter.CTkButton(self.navigation_frame, text="Início", command=self.home_button_event)
        self.home_button.grid(row=0, column=0, sticky="ew")

        self.cadastro_button = customtkinter.CTkButton(self.navigation_frame, text="Cadastro", command=self.cadastro_button_event)
        self.cadastro_button.grid(row=1, column=0, sticky="ew")

        self.movimentacao_button = customtkinter.CTkButton(self.navigation_frame, text="Movimentação", command=self.movimentacao_button_event)
        self.movimentacao_button.grid(row=2, column=0, sticky="ew")

        self.busca_button = customtkinter.CTkButton(self.navigation_frame, text="Busca", command=self.busca_button_event)
        self.busca_button.grid(row=3, column=0, sticky="ew")

    def create_content_frames(self):
        self.home_frame = customtkinter.CTkFrame(self)

        self.cadastro_frame = CadastroFrame(
            self,
            self.matricula,
            self.ferramenta
        )

        self.movimentacao_frame = MovimentacaoFrame(
            self,
            self.movimentacao
        )

        self.busca_frame = BuscaFrame(
            self,
            self.matricula,
            self.ferramenta
        )

    def select_frame_by_name(self, name):
        frames = {
            "home": self.home_frame,
            "cadastro": self.cadastro_frame,
            "movimentacao": self.movimentacao_frame,
            "busca": self.busca_frame
        }

        for frame_name, frame in frames.items():
            if frame_name == name:
                frame.grid(row=0, column=1, sticky="nsew")
            else:
                frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def cadastro_button_event(self):
        self.select_frame_by_name("cadastro")

    def movimentacao_button_event(self):
        self.select_frame_by_name("movimentacao")

    def busca_button_event(self):
        self.select_frame_by_name("busca")

if __name__ == "__main__":
    database = Database()
    database.criar_banco()
    app = MotivaApp()
    app.mainloop()
