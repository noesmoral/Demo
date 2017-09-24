from time import sleep

import moduloCamara
import moduloEnvioCorreo

C=moduloCamara.CAMARA()
CR=moduloEnvioCorreo.CORREO()

sleep(2)
C.captura()
sleep(2)
CR.enviar(C)
sleep(2)
CR.enviar(C,opcion='Imagen')
sleep(2)
CR.enviar(C,contenido='Hola encantado')
sleep(2)
CR.enviar(C,opcion='Imagen',contenido='Hola pedrito',direccion='pedrito_noesmoral@hotmail.com')
sleep(2)
C.captura(nombre='pedro')
C.close()
