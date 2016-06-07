#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# Battleship Game Server
# Abel Castilla Rodríguez, Alejandro Muñoz Del �?lamo, Damián Nimo Járquez
# Copyright © 2016



# ---------------------------------------1. Bibliotecas---------------------------------------
# Librerías para la comunicación TCP/IP
import socket 
import sys
import tweepy
import os
import time

# ---------------------------------------2. Funciones---------------------------------------

# 2.1 - Establecer comunicación cliente - servidor

def begin_comm():	

	# Paso 0 - Identificar nuestro usuario en Twitter
	consumer_key='4zfod1mtVenCNLCSgzhT0xwDo'
	consumer_secret='MBiddLBS3XWzbX3M34AkcbFi9hvjznp0Lsl5xCDd5eNsH8vXug'
	access_token='709277264123469824-90KqXm5uXE01YnHC32A9snX6ULf1tDC'
	access_token_secret='e8tjKhQimZaQNtFknsEdPZHPJQLSLsIK4bU6CoxEdsF2i'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)

	api = tweepy.API(auth)

	# Paso 1 - Creamos un socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	

	# Paso 2 - Enlazamos el socket a un puerto
	server_address = ('localhost', 10000)		# Creamos una variable server_address con la dirección IP y el puerto que vamos a asignar al servidor
	print >> sys.stdout, 'Montando el servidor %s con puerto %s' % server_address	# Mostramos por pantalla dicha información
	sock.bind(server_address)														# Enlazamos el socket con la información anterior
	print >> sys.stdout, 'Servidor en funcionamiento'								# Mostramos en la consola que el servidor está en funcionamiento
	sock.listen(1)
	api.update_status(status='Partida inicializada a las '+(time.strftime("%H:%M:%S")))
	global cadena 
	cadena = ""
	while True:		# Disponemos el servidor en modo escucha
		try:
			print >> sys.stdout, 'Esperando al oponente'	
			connection, client_address = sock.accept()
			print >> sys.stderr, 'Conectamos con el cliente', client_address 	# Indicamos con qué cliente comienza la partida
			partida = True	# Creamos una bandera para conocer el estado de la partida 						
									# Creamos una variable para controlar el turno
			# while (partida == True):						# Mientras la bandera indique que la partida sigue activa
			option = connection.recv(16)			# Recibimos la respuesta del cliente
			print option
			if (option == 'fin'):
				partida = False 
				print 'ENTRO POR DONDE NO ES'
				api.update_status(status='Partida Finalizada a las' + (time.strftime("%H:%M:%S")))
			elif (option == "actualiza"):
				mostrar(api)
				print 'Entro en actualiza'
			else:
				disparar(option)
				print 'entro en disparo'
   		finally:
   			if (partida == False):
				connection.close()	# Cerramos la conexión
				break


	# 2.2 -  Ubicar disparo
def disparar(option):
	global cadena 
	cadena =  cadena  + option + " " 

def mostrar(api):
	global cadena
	mapa = os.path.abspath('path2.png') # Obtenemos la imagen que queremos postear
	api.update_with_media(mapa, status = cadena) # Posteamos el disparo en twitter
	
	cadena = ""

begin_comm()



