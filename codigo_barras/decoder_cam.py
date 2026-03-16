import cv2
from pyzbar.pyzbar import decode, ZBarSymbol
from typing import List, Optional, Tuple

class LeitorCodigo:
    """Classe para ler códigos de barras EAN-13 usando a câmera."""

    def __init__(self, camera_index: int = 0):
        """Inicializa o leitor de código de barras.

        Args:
            camera_index: O índice da câmera a ser usada.
        """
        self.camera_index: int = camera_index
        self.cap: Optional[cv2.VideoCapture] = None
        self.instrumentos_cadastrados: List[str] = []

    def iniciar_camera(self) -> None:
        """Inicializa e abre a captura de vídeo da câmera."""
        self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)
        if not self.cap.isOpened():
            raise IOError("Não foi possível abrir a câmera.")
        print("Câmera iniciada. Pressione 'ESC' para fechar.")

    @staticmethod
    def desenhar_borda(frame, rect: Tuple[int, int, int, int], texto: str) -> None:
        """Desenha uma borda e um texto no frame de vídeo."""
        x, y, w, h = rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, texto, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    def ler_codigo(self) -> Optional[List[str]]:
        """Lê os códigos de barras do feed da câmera até que 'ESC' seja pressionado."""
        if self.cap is None:
            print("Câmera não iniciada.")
            return None

        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Não foi possível ler o frame da câmera.")
                    break

                resultados = decode(frame, symbols=[ZBarSymbol.EAN13])

                for obj in resultados:
                    try:
                        codigo = obj.data.decode("utf-8")
                        if codigo not in self.instrumentos_cadastrados:
                            self.instrumentos_cadastrados.append(codigo)
                            print(f"Código encontrado: {codigo} | Tipo: {obj.type}")
                        self.desenhar_borda(frame, obj.rect, codigo)
                    except UnicodeDecodeError:
                        print(f"Erro ao decodificar dados do código de barras: {obj.data}")

                cv2.imshow("Leitor de Codigo", frame)

                if cv2.waitKey(1) & 0xFF == 27:
                    break
        except Exception as e:
            print(f"Ocorreu um erro durante a leitura: {e}")
        finally:
            return self.fechar_camera()

    def fechar_camera(self) -> List[str]:
        """Libera a câmera e destrói as janelas do OpenCV, retornando os códigos lidos."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
        cv2.destroyAllWindows()
        return self.instrumentos_cadastrados

    def executar(self) -> List[str]:
        """Executa o processo completo de leitura de código de barras."""
        try:
            self.iniciar_camera()
            codigos = self.ler_codigo()
            return codigos if codigos is not None else []
        except IOError as e:
            print(e)
            return []

if __name__ == '__main__':
    leitor = LeitorCodigo()
    codigos_lidos = leitor.executar()
    print("\nCódigos de barras lidos:")
    for codigo in codigos_lidos:
        print(codigo)