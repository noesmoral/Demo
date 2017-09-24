from time import sleep
import moduloCamara
import moduloConversorTexto
import moduloEnvioCorreo
import moduloQRN
import time


C=moduloCamara.CAMARA()
CR=moduloEnvioCorreo.CORREO()
QR=moduloQRN.QR()
CONV=moduloConversorTexto.CONVERSOR()

QR.localizar(C,CR,CONV)

C.close()
CONV.close()
