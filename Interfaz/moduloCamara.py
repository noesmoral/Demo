from picamera import PiCamera
from time import sleep

class CAMARA():

    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution=(1920, 1088)
        self.camera.hflip=True
        self.camera.vflip=True

    def captura(self, ruta='/home/pi/Desktop/Imagenes/', nombre='imagen', resolucionAncho=1920, resolucionAlto=1088):
        try:
                if resolucionAncho!=1920 or resolucionAlto!=1088:
                        self.camera.capture(ruta+nombre+".jpg",resize=(resolucionAncho,resolucionAlto))
                else:
                        self.camera.capture(ruta+nombre+".jpg")
        except Exception as e:
                print(e)
                print "Error en alguno de los parametros"

    def close(self):
        self.camera.close()
