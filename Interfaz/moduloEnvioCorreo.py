#!/usr/bin/env python
# -*- coding: utf-8 -*-
#otros import
import RPi.GPIO as GPIO
import time
import sys
#importamos la opcion de lanzar otros programas para realizar las capturas
import commands
# importamos la libreria smtplib (no es necesario instalarlo)
import smtplib 
# importamos librerias  para construir el mensaje
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
#importamos librerias para adjuntar
from email.MIMEImage import MIMEImage 
from email import encoders 

#defaul msg
addr_to='pedro.barquin@gmail.com'
mensaje="Cuerpo del mensaje de pruebas de raspberry, para el envio de correos"
##el mail sale desde el correo
addr_from = 'pruebasraspberry@gmail.com'
# Define SMTP email server details
smtp_server = 'smtp.gmail.com:587'
smtp_user   = 'pruebasraspberry@gmail.com'
smtp_pass   = 'Pruebas16'
#Mensaje defualt
cabecera='Correo notificacion Pruebas Raspberry'

class CORREO():
	
	def __init__(self):
		pass

	#funciones envio de mensajes
	def mensajeConImagen(self,C):
		# definimos los correo de remitente y receptor
		##se envia un mail a
		global addr_to, mensaje, smtp_server, smtp_user, smtp_pass, addr_from

		# Construimos el mail
		msg = MIMEMultipart()
		msg['To'] = addr_to
		msg['From'] = addr_from
		msg['Subject'] = cabecera
		#cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
		msg.attach(MIMEText(mensaje))

		#hacemos la captura antes de enviar el mensaje nuevo
		C.captura(ruta='/home/pi/Desktop/Capturas/',resolucionAncho=400,resolucionAlto=200)	
		
		#adjuntamos fichero de texto pero puede ser cualquer tipo de archivo
		##cargamos el archivo a adjuntar de la ruta definida por el programa
		fp = open('/home/pi/Desktop/Capturas/imagen.jpg','rb')
		#adjunto = MIMEBase('multipart', 'encrypted')
		adjunto = MIMEImage(fp.read())
		#lo insertamos en una variable
		#adjunto.set_payload(fp.read()) 
		#fp.close()  
		#lo encriptamos en base64 para enviarlo
		#encoders.encode_base64(adjunto) 
		#agregamos una cabecera y le damos un nombre al archivo que adjuntamos puede ser el mismo u otro
		adjunto.add_header('Content-Disposition', 'attachment', filename='captura.jpg')
		#adjuntamos al mensaje
		msg.attach(adjunto) 

		# inicializamos el stmp para hacer el envio
		server = smtplib.SMTP(smtp_server)
		server.starttls() 
		#logeamos con los datos ya seteamos en la parte superior
		server.login(smtp_user,smtp_pass)
		#el envio
		server.sendmail(addr_from, addr_to, msg.as_string())
		#apagamos conexion stmp
		server.quit()

	def mensajeSimple(self):
		# definimos los correo de remitente y receptor
		##se envia un mail a
		global addr_to, mensaje, smtp_server, smtp_user, smtp_pass, addr_from
	 
		# Construimos el mail
		msg = MIMEMultipart() 
		msg['To'] = addr_to
		msg['From'] = addr_from
		msg['Subject'] = cabecera
		#cuerpo del mensaje en HTML y si fuera solo text puede colocar en el 2da parametro 'plain'
		msg.attach(MIMEText(mensaje))

		# inicializamos el stmp para hacer el envio
		server = smtplib.SMTP(smtp_server)
		server.starttls()
		#logeamos con los datos ya seteamos en la parte superior
		server.login(smtp_user,smtp_pass)
		#el envio
		server.sendmail(addr_from, addr_to, msg.as_string())
		#apagamos conexion stmp
		server.quit()

	def enviar(self, C, opcion='Default', contenido='Default', direccion='Default'):
		global mensaje, addr_to
		#print opcion, contenido, direccion
		try:
               		if opcion=='Default' and contenido=='Default' and direccion=='Default':
				#print "correo simple"
      	        		self.mensajeSimple()
               		else:
				if contenido!='Default':
					mensaje=contenido
				if direccion!='Default':
					addr_to= direccion
	                                if addr_to.endswith(('@gmail.com','@hotmail.com')):
	                                        pass
	               		        else:
        	       		        	print "el correo (tercer parametro) no es valido se enviara al correo default"
						addr_to='pedro.barquin@gmail.com'
				if opcion=='Imagen':
                        	       	#print "mensaje con imagen"
					self.mensajeConImagen(C)
                        	elif opcion=='Default':
					#print "mensaje sin imagen"
                        	       	self.mensajeSimple()
                        	else:
                        	       	print "El primer parametro no es valido"

		except:
	                print "Se ha olvidado añadir algun elemento o poner Default"
	                print "El orden es:"
	                print "Mensaje con imagen: Imagen o Default"
	                print "Cuerpo del mensaje: xxx o Default"
	                print "Correo: xxx@gmail.com o Default"
