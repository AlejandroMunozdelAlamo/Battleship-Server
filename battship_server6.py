#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# Battleship Game Server
# Abel Castilla RodrÃ­guez, Alejandro MuÃ±oz Del Ã?lamo, DamiÃ¡n Nimo JÃ¡rquez
# Copyright Â© 2016



# ---------------------------------------1. Bibliotecas---------------------------------------
# LibrerÃ­as para la comunicaciÃ³n TCP/IP
import socket 
import sys
import tweepy
import os
import time
# ---------------------------------------2. Funciones---------------------------------------

# 2.1 - Establecer comunicaciÃ³n cliente - servidor

def begin_comm():	

	# Paso 0 - Identificar nuestro usuario en Twitter
	consumer_key='Introducir consumer_key'
	consumer_secret='Introducir consumer_secret'
	access_token='Introducir access_token'
	access_token_secret='Introducir access_token_secret'

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# Paso 1 - Creamos un socket TCP/IP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	

	# Paso 2 - Enlazamos el socket a un puerto
	server_address = ('localhost', 10000)		# Creamos una variable server_address con la direcciÃ³n IP y el puerto que vamos a asignar al servidor
	print >> sys.stdout, 'Montando el servidor %s con puerto %s' % server_address	# Mostramos por pantalla dicha informaciÃ³n
	sock.bind(server_address)														# Enlazamos el socket con la informaciÃ³n anterior
	print >> sys.stdout, 'Servidor en funcionamiento'								# Mostramos en la consola que el servidor estÃ¡ en funcionamiento
	sock.listen(1)
	api.update_status(status='Partida inicializada a las '+(time.strftime("%H:%M:%S")))
	global cadena 
	cadena = ""
	while True:		# Disponemos el servidor en modo escucha
		try:
			print >> sys.stdout, 'Esperando al oponente'	
			connection, client_address = sock.accept()
			print >> sys.stderr, 'Conectamos con el cliente', client_address 	# Indicamos con quÃ© cliente comienza la partida
			partida = True	# Creamos una bandera para conocer el estado de la partida					
			while partida == True:						# Mientras la bandera indique que la partida sigue activa
				option = connection.recv(32)			# Recibimos la respuesta del cliente
				print option
				if option == 'fin':
					partida = False 
					print 'Fin de partida'
					api.update_status(status='Partida Finalizada a las '+(time.strftime("%H:%M:%S")))
				elif option == "actualiza":
					mostrar()
					print 'Entro en actualiza'
				else:
					disparar(option)
					print 'entro en disparo'
				option = ""
   		finally:
			connection.close()	# Cerramos la conexiÃ³n


	# 2.2 -  Ubicar disparo
def disparar(option):
	global cadena 
	cadena =  cadena  + option + " " 

def mostrar():
	global cadena
	mapa = os.path.abspath('path2.png') # Obtenemos la imagen que queremos postear
	api.update_with_media(mapa, status = cadena) # Posteamos el disparo en twitter
	
	cadena = ""

begin_comm()



