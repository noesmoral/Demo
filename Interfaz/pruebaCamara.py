import moduloCamara

C=moduloCamara.CAMARA()

contenido='resolucionAncho=300,resolucionAlto=100'
C.captura()
C.captura(ruta='/home/pi/Desktop/')
C.captura(nombre='Foto')
C.captura(nombre='Foto2',resolucionAncho=600,resolucionAlto=400)
C.captura(contenido)
C.close()
