import cv2
from pyzbar.pyzbar import decode, ZBarSymbol



class Leitor_codigo:

    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.cap = None
        self.instrumentos_cadastrados = []


    def iniciar_camera(self):
        self.cap = cv2.VideoCapture(self.camera_index,cv2.CAP_DSHOW)
        print("Pressione ESC para fechar a câmera")

        if not self.cap.isOpened():
            raise Exception("Não foi possível abrir a câmera")

    @staticmethod
    def desenhar_borda(frame, rect, texto):
        x, y, w, h = rect

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            texto,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            2,
        )


    def ler_codigo(self):

        if self.cap is None:
            print("Câmera não iniciada")
            return None

        else:

            try:
                while True:
                    ret, frame = self.cap.read()

                    if not ret:
                        break

                    resultados = decode(frame, symbols=[ZBarSymbol.EAN13])

                    for obj in resultados:
                        codigo = obj.data.decode("utf-8")
                        tipo = obj.type

                        self.desenhar_borda(frame, obj.rect, codigo)

                        if codigo not in self.instrumentos_cadastrados:
                            self.instrumentos_cadastrados.append(codigo)
                            print(f"Código encontrado: {codigo} | Tipo: {tipo}")


                    cv2.imshow("Leitor de Codigo", frame)

                    if cv2.waitKey(1) == 27:
                        break

            except Exception as e:
                print(e)

            finally:
                self.fechar_camera()

    def fechar_camera(self):

        if self.cap is not None:

            self.cap.release()
            cv2.destroyAllWindows()

            return self.instrumentos_cadastrados

        else:
            print("Câmera não iniciada")
            return None

    def executar(self):

        self.iniciar_camera()
        self.ler_codigo()
        self.fechar_camera()

        return self.instrumentos_cadastrados

        #for instrumento in self.instrumentos_cadastrados:
           # print(instrumento)

