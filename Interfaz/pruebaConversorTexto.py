import moduloConversorTexto
import time

C=moduloConversorTexto.CONVERSOR()

C.convertir(velocidad=145, texto='Hola don Pepito. Hola don jose')
'''
time.sleep(5)
C.convertir(velocidad=170, fichero='/home/pi/Desktop/mensaje.txt')
time.sleep(5)
C.convertir(grabar=True, texto='Hola don pepito, hola don jose', nombre='1')
time.sleep(5)
C.convertir(grabar=True, fichero='/home/pi/Desktop/mensaje.txt', nombre='2')
time.sleep(5)
C.convertir(reproducir=True, nombre='1')
time.sleep(5)
'''
C.close()
