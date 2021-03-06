#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import time
import threading
import os
import RPi.GPIO as GPIO
from subprocess import check_output

import moduloCamara
import moduloQRN
import moduloEnvioCorreo
import moduloConversorTexto
import moduloVoz

C=moduloCamara.CAMARA()
CR=moduloEnvioCorreo.CORREO()
QR=moduloQRN.QR()
CONV=moduloConversorTexto.CONVERSOR()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

pygame.init()
pygame.mixer.quit()
screen=pygame.display.set_mode((800,480),pygame.FULLSCREEN)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
myfont = pygame.font.SysFont("monospace", 85)

mainloop = True

salir=0
mostrar=False
menu=1
frase=" "
aux2=0

def mostrarTextoMenu1():
	pygame.display.flip()
	screen.fill(WHITE)

	textSurface=myfont.render('FOTO/QR', 1, (0,0,0))
	textRect= textSurface.get_rect()
	textRect.center=(400,40)
	screen.blit(textSurface,textRect)

	textSurface=myfont.render('CORREO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,140)
        screen.blit(textSurface,textRect)

	textSurface=myfont.render('CONVERSOR TEXTO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,240)
        screen.blit(textSurface,textRect)

	textSurface=myfont.render('COMANDOS VOZ', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

	textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

	pygame.display.update()

def mostrarTextoMenu2():
        pygame.display.flip()
        screen.fill(WHITE)

        textSurface=myfont.render('FOTO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,40)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('FOTO REDUCIDA', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,140)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('QR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,240)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('VOLVER', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

        pygame.display.update()

def mostrarTextoMenu3():
        pygame.display.flip()
        screen.fill(WHITE)

        textSurface=myfont.render('CORREO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,40)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('CORREO+FOTO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,140)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('CORREO+FOTO+TXT', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,240)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('VOLVER', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

        pygame.display.update()

def mostrarTextoMenu4():
        pygame.display.flip()
        screen.fill(WHITE)

        textSurface=myfont.render('CONV MENSAJE', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,40)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('CONV TEXTO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,140)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('REPRODUCIR AUDIO', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,240)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('VOLVER', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

        pygame.display.update()

def mostrarTextoMenu5(mensaje):
        pygame.display.flip()
        screen.fill(WHITE)

        textSurface=myfont.render(mensaje, 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,140)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('VOLVER', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

        pygame.display.update()

def mostrarTextoMenuLock():
        pygame.display.flip()
        screen.fill(RED)

        textSurface=myfont.render('VOLVER', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,340)
        screen.blit(textSurface,textRect)

        textSurface=myfont.render('SALIR', 1, (0,0,0))
        textRect= textSurface.get_rect()
        textRect.center=(400,440)
        screen.blit(textSurface,textRect)

        pygame.display.update()
        
def contador():
        global frase,salir,mostrar
        numfilasAnterior=0
        while salir == 0:
                if mostrar==True:
                        archivo = open('/home/pi/Desktop/registro.txt', 'r')
                        contenido = archivo.read()
                        palabra = contenido.splitlines()
                        longitud=len(palabra)
			print (longitud, palabra[numfilasAnterior-1])
                        if (longitud <= numfilasAnterior):
                                archivo.close()
                                time.sleep(1)
                        else:
                                numfilasAnterior = longitud
                                frase=palabra[numfilasAnterior-1]
                                mostrarTextoMenu5(frase)
                                if frase=="HOLA" or frase=="LED":
                                        GPIO.output(17, True)
                                elif frase=="ADIOS":
                                        GPIO.output(17, False)
                                time.sleep(1)
                else:
                        time.sleep(1)

mostrarTextoMenu1()

os.system("rm /home/pi/Desktop/registro.txt")

V=moduloVoz.VOZ()

time.sleep(2)

hilo=threading.Thread(target=contador)
hilo.start()

try:
        while mainloop:
            time.sleep(0.3) 
            
            for event in pygame.event.get():

                if menu==1:
                        if pygame.mouse.get_pos()[0] >= 230 and pygame.mouse.get_pos()[1] >= 10:
                                if pygame.mouse.get_pos()[0] <= 575 and pygame.mouse.get_pos()[1] <= 70:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                menu=2
                                                mostrarTextoMenu2()
                                                first=1
                        if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 115:
                                if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 170:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                menu=3
                                                mostrarTextoMenu3()
                                                first=1
                        if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 215:
                                if pygame.mouse.get_pos()[0] <= 780 and pygame.mouse.get_pos()[1] <= 270:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                menu=4
                                                mostrarTextoMenu4()
                                                first=1
                        if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[1] >= 315:
                                if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 370:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                menu=5
                                                mostrarTextoMenu5(" ")
                                                mostrar=True
                                                first=1

                if menu==2:
                        if first==1:
                                first=0
                        else:
                                if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos()[1] >= 10:
                                        if pygame.mouse.get_pos()[0] <= 500 and pygame.mouse.get_pos()[1] <= 70:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        C.captura()
                                                        img=pygame.image.load("/home/pi/Desktop/Imagenes/imagen.jpg")
                                                        img = pygame.transform.scale(img, (800, 480))
                                                        screen.blit(img,(0,0))
                                                        pygame.display.update()
                                                        time.sleep(7)
                                                        mostrarTextoMenu2()
                                if pygame.mouse.get_pos()[0] >= 75 and pygame.mouse.get_pos()[1] >= 115:
                                        if pygame.mouse.get_pos()[0] <= 730 and pygame.mouse.get_pos()[1] <= 170:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        C.captura(resolucionAncho=600,resolucionAlto=400)
                                                        img=pygame.image.load("/home/pi/Desktop/Imagenes/imagen.jpg")
                                                        img = pygame.transform.scale(img, (800, 480))
                                                        screen.blit(img,(0,0))
                                                        pygame.display.update()
                                                        time.sleep(7)
                                                        mostrarTextoMenu2()
                                if pygame.mouse.get_pos()[0] >= 340 and pygame.mouse.get_pos()[1] >= 215:
                                        if pygame.mouse.get_pos()[0] <= 460 and pygame.mouse.get_pos()[1] <= 270:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        QR.localizar(C,CR,CONV)
                                                        mostrarTextoMenu2()
                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        menu=1
                                                        mostrarTextoMenu1()

                if menu==3:
                        if first==1:
                                first=0
                        else:
                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 10:
                                        if pygame.mouse.get_pos()[0] <= 550 and pygame.mouse.get_pos()[1] <= 70:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CR.enviar(C)
                                                        mostrarTextoMenu3()
                                if pygame.mouse.get_pos()[0] >= 125 and pygame.mouse.get_pos()[1] >= 115:
                                        if pygame.mouse.get_pos()[0] <= 680 and pygame.mouse.get_pos()[1] <= 170:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CR.enviar(C,opcion='Imagen')
                                                        mostrarTextoMenu3()
                                if pygame.mouse.get_pos()[0] >= 20 and pygame.mouse.get_pos()[1] >= 215:
                                        if pygame.mouse.get_pos()[0] <= 780 and pygame.mouse.get_pos()[1] <= 270:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CR.enviar(C,opcion='Imagen',contenido='Hola, esto es un correo de prueba, de la demo del TFG')
                                                        mostrarTextoMenu3()
                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        menu=1
                                                        mostrarTextoMenu1()

                if menu==4:
                        if first==1:
                                first=0
                        else:
                                if pygame.mouse.get_pos()[0] >= 95 and pygame.mouse.get_pos()[1] >= 10:
                                        if pygame.mouse.get_pos()[0] <= 700 and pygame.mouse.get_pos()[1] <= 70:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CONV.convertir(texto='Mensaje de conversión, texto voz, offline')
                                                        aux=1
                                                        aux2=1
                                                        while aux==1:
                                                                try:
                                                                        check_output(["pidof","espeak"])
                                                                        for event in pygame.event.get():
                                                                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                                                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                        try:
                                                                                                                os.system("sudo pkill mplayer")
                                                                                                                os.system("sudo pkill espeak")
                                                                                                        except:
                                                                                                                pass
                                                                                                        aux=0
                                                                except:
                                                                        aux=0
                                                        first=1
                                                        mostrarTextoMenu4()
                                if pygame.mouse.get_pos()[0] >= 150 and pygame.mouse.get_pos()[1] >= 115:
                                        if pygame.mouse.get_pos()[0] <= 650 and pygame.mouse.get_pos()[1] <= 170:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CONV.convertir(fichero='/home/pi/Desktop/mensaje.txt')
                                                        aux=1
                                                        aux2=1
                                                        while aux==1:
                                                                try:
                                                                        check_output(["pidof","espeak"])
                                                                        for event in pygame.event.get():
                                                                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                                                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                        try:
                                                                                                                os.system("sudo pkill mplayer")
                                                                                                                os.system("sudo pkill espeak")
                                                                                                        except:
                                                                                                                pass
                                                                                                        aux=0
                                                                except:
                                                                        aux=0
                                                        first=1
                                                        mostrarTextoMenu4()
                                if pygame.mouse.get_pos()[0] >= 5 and pygame.mouse.get_pos()[1] >= 215:
                                        if pygame.mouse.get_pos()[0] <= 795 and pygame.mouse.get_pos()[1] <= 270:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        mostrarTextoMenuLock()
                                                        CONV.convertir(ruta='/home/pi/Desktop/',nombre='cancion',reproducir=1)
                                                        aux=1
                                                        aux2=1
                                                        while aux==1:
                                                                try:
                                                                        check_output(["pidof","mplayer"])
                                                                        for event in pygame.event.get():
                                                                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                                                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                                                                        try:
                                                                                                                os.system("sudo pkill mplayer")
                                                                                                                os.system("sudo pkill espeak")
                                                                                                        except:
                                                                                                                pass
                                                                                                        aux=0
                                                                except:
                                                                        aux=0
                                                        first=1
                                                        mostrarTextoMenu4()
                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                if event.type == pygame.MOUSEBUTTONDOWN and aux2==0:
                                                        menu=1
                                                        mostrarTextoMenu1()		
                                                else:
                                                        aux2=0		

                if menu==5:
                        if first==1:
                                first=0
                        else:
                                if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 315:
                                        if pygame.mouse.get_pos()[0] <= 555 and pygame.mouse.get_pos()[1] <= 370:
                                                if event.type == pygame.MOUSEBUTTONDOWN:
                                                        menu=1
                                                        mostrar=False
                                                        time.sleep(1.1)
                                                        mostrarTextoMenu1()

                if event.type == pygame.QUIT:
                        mainloop = False
                        V.close()
                        C.close()
                        CONV.close()
                        salir=1
                        time.sleep(1.1)
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                mainloop = False
                                V.close()
                                C.close()
                                CONV.close()
                                salir=1
                                time.sleep(1.1)
                if pygame.mouse.get_pos()[0] >= 270 and pygame.mouse.get_pos()[1] >= 415:
                                if pygame.mouse.get_pos()[0] <= 520 and pygame.mouse.get_pos()[1] <= 470:
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                mainloop = False
                                                V.close()
                                                C.close()
                                                CONV.close()
                                                salir=1
                                                time.sleep(1.1)


            pygame.display.flip()
         
        pygame.quit()
        GPIO.output(17, False)
except:
        V.close()
        C.close()
        CONV.close()
