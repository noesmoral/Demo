import cv2
import numpy
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import zbar
import Image

class QR():
    def __init__(self):
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config('enable')

    def localizar(self,Camara,Correo,Conversor):
        Camara.captura(nombre='2')
        img=cv2.imread('/home/pi/Desktop/Imagenes/2.jpg')
        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        try:
		pil = Image.fromarray(gray)
                width, height = pil.size
                raw = pil.tostring()
                image = zbar.Image(width, height, 'Y800', raw)
                self.scanner.scan(image)
                try:
                        for symbol in image:
                                contenidoQR=symbol.data
                                cabecera=contenidoQR[0:7]
                                cabecera=cabecera.lower()
                                cuerpo=contenidoQR[7:]
                                lineas=contenidoQR.splitlines()
                                longitud=len(lineas)
                                print cabecera
                                print cuerpo
                                print lineas
                                print longitud
                                if cabecera=='comando':
                                        print "COMANDO"
                                        os.system(cuerpo+' &')
                                elif cabecera=='mensaje':
                                        print "MENSAJE"
                                        if longitud>1:
                                        	idioma="es"
                                        	velocidad=150
                                        	texto=' '
                                        	fichero=' '
                                        	ruta='/home/pi/Desktop/Grabaciones/'
                                        	nombre='last'
                                        	reproducir=0
                                        	grabar=0
                                        	for i in xrange(1,longitud):
                                        		if lineas[i].startswith("idioma="):
                                				idioma=lineas[i][7:]
                                			if lineas[i].startswith("velocidad="):
                                				velocidad=int(lineas[i][10:])
                                			if lineas[i].startswith("texto="):
                                				texto=lineas[i][6:]
                                			if lineas[i].startswith("fichero="):
                                				fichero=lineas[i][8:]
                                			if lineas[i].startswith("ruta="):
                                				ruta=lineas[i][5:]
                                			if lineas[i].startswith("nombre="):
                                				nombre=lineas[i][7:]
                                			if lineas[i].startswith("reproducir="):
                                				reproducir=int(lineas[i][11:])
                                			if lineas[i].startswith("grabar="):
                                				grabar=int(lineas[i][7:])
                                        	Conversor.convertir(idioma=idioma, velocidad=velocidad, texto=texto, fichero=fichero, ruta=ruta, nombre=nombre, reproducir=reproducir, grabar=grabar)
                                        else:
                                        	print "Falta informacion en el QR para realizar la accion"
                                elif cabecera=='correos':
                                		print "CORREO"
                                		if longitud>1:
                                			opcion="Default"
                                			contenido="Default"
                                			direccion="Default"
                                			for i in xrange(1,longitud):
                                				if lineas[i].startswith("opcion="):
                                					opcion=lineas[i][7:]
                                				if lineas[i].startswith("contenido="):
                                					contenido=lineas[i][10:]
                                				if lineas[i].startswith("direccion="):
                                					direccion=lineas[i][10:]
                                			Correo.enviar(Camara,opcion=opcion,contenido=contenido,direccion=direccion)
                                		else:
                                			Correo.enviar(Camara)
                                elif cabecera=="captura":
                                		print 'CAPTURA'
                                		if longitud>1:
                                			ruta='/home/pi/Desktop/Imagenes/'
                                			nombre='imagen'
                                			resolucionAncho=1920
                                			resolucionAlto=1088
                                			for i in xrange(1,longitud):
                                				if lineas[i].startswith("ruta="):
                                					ruta=lineas[i][5:]
                                				if lineas[i].startswith("nombre="):
                                					nombre=lineas[i][7:]
                                				if lineas[i].startswith("resolucionAncho="):
                                					resolucionAncho=int(lineas[i][16:])
                                				if lineas[i].startswith("resolucionAlto="):
                                					resolucionAlto=int(ineas[i][15:])
                                			Camara.captura(ruta=ruta, nombre=nombre, resolucionAncho=resolucionAncho, resolucionAlto=resolucionAlto)
                                		else:
                                			Camara.captura()
                                #elif cabecera=="serialp"
                                #		print 'SERIAL'
                                else:
                                        print "QR no definido"
                except:
                        print "NO SE PUEDE DECODIFICAR\n"
        except Exception as e:
                print "Error en la captura o interpretacion del codigo QR"
