#!/usr/bin/python
import moduloVoz
import os,signal
import subprocess, time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT) ## GPIO 17 como salida

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

        V=moduloVoz.VOZ()

        time.sleep(1)

        contador()
	
        V.close()
        
except Exception as e:
	print(e)
        V.close()
