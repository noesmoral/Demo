#!/usr/bin/python
import moduloCamara
import moduloQRN
import moduloEnvioCorreo
import moduloConversorTexto

import os,signal
import subprocess, time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

C=moduloCamara.CAMARA()
CR=moduloEnvioCorreo.CORREO()
QR=moduloQRN.QR()
CONV=moduloConversorTexto.CONVERSOR()

def contador():
	try:
	        numfilasAnterior=0
	        i=0
	        while i == 0 :
	                archivo = open('/home/pi/Desktop/registro.txt', 'r')
	                contenido = archivo.read()
	                palabra = contenido.splitlines()
	                longitud=len(palabra)
	                print numfilasAnterior, palabra, longitud
	                if (longitud <= numfilasAnterior):
	                        archivo.close()
	                        time.sleep(1)
	                else:
	                        numfilasAnterior = longitud
	                        frase=palabra[numfilasAnterior-1]
	                        if frase=="ENCENDER LED":
	                                print ("detectado encender led")
	                                GPIO.output(17, True)
	                        if frase=="ENCENDER":
	                                print ("detectado encender led")
	                                GPIO.output(17, True)
	                        if frase=="APAGAR LED":
	                                print ("detectado apagar led")
	                                GPIO.output(17, False)
	                        if frase=="APAGAR":
	                                print ("detectado apagar led")
	                                GPIO.output(17, False)
	                        if frase=="ADIOS":
	                                GPIO.output(17, True)
	                                time.sleep(0.5)
	                                GPIO.output(17, False)
	                                time.sleep(0.5)
	                                GPIO.output(17, True)
	                                time.sleep(0.5)
	                                GPIO.output(17, False)
	                                print ("detectada salida")
	                                i=1
	                        archivo.close()
	                        time.sleep(1)
	except Exception as e:
	        print(e)

try:
	os.system("rm /home/pi/Desktop/registro.txt")

	proc = subprocess.Popen('sudo pocketsphinx_continuous -lm /home/pi/Diccionario/9586.lm -dict /home/pi/Diccionario/9586.dic > /home/pi/Desktop/registro.txt -adcdev sysdefault -inmic yes',shell=True)
	print proc.pid
	
	time.sleep(1)

	contador()
	
	os.killpg(os.getpgid(proc.pid), signal.SIGKILL)

except Exception as e:
	print(e)

