#!/usr/bin/env python
# -*- encoding: UTF-8 -*-

# Battleship Game Server
# Abel Castilla Rodríguez, Alejandro Muñoz Del Álamo, Damián Nimo Járquez
# Copyright © 2016



# ---------------------------------------1. Bibliotecas---------------------------------------
# Librerías para la comunicación TCP/IP
import socket 
import sys
import tweepy

# ---------------------------------------2. Funciones---------------------------------------

# 2.1 - Establecer comunicación cliente - servidor

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
	server_address = ('localhost', 10000)		# Creamos una variable server_address con la dirección IP y el puerto que vamos a asignar al servidor
	print >> sys.stdout, 'Montando el servidor %s con puerto %s' % server_address	# Mostramos por pantalla dicha información
	sock.bind(server_address)														# Enlazamos el socket con la información anterior
	print >> sys.stdout, 'Servidor en funcionamiento'								# Mostramos en la consola que el servidor está en funcionamiento
	sock.listen(1)

	while True:																# Disponemos el servidor en modo escucha
		try:
    			print >> sys.stdout, 'Esperando al oponente'	
    			connection, client_address = sock.accept()
       			print >> sys.stderr, 'Conectamos con el cliente', client_address 	# Indicamos con qué cliente comienza la partida
       			partida = True														# Creamos una bandera para conocer el estado de la partida															# Creamos una variable para controlar el turno
    #   			while partida == True:						# Mientras la bandera indique que la partida sigue activa
    #   				option = connection.recv(16)			# Recibimos la respuesta del cliente
    #   				if option == "La Partida ha finalizado.":
    #   					partida = False 
    #   					api.update_status(status = 'Partida Finalizada')
    #   				elif option == "actualiza imagen":
    #   					mostrar()
    #   				elif turno == 1:
    #   					disparar(option)						# Realizamos el disparo
    #   				elif turno == 2:
    #   					disparar(option)

    #   				turno = (turno+1)%2
   	#	finally:
    #   			connection.close()	# Cerramos la conexión

    			while partida == True:      # Mientras la bandera indique que la partida sigue activa
           			option = connection.recv(16)   # Recibimos la respuesta del cliente
           			if option == "La Partida ha finalizado.":
            				partida = False 
                     		api.update_status(status='Partida Finalizada')
           			if option == "actualiza imagen":
            				mostrar()
           			else:
            				disparar(option)

        	finally:
   				connection.close()	# Cerramos la conexión

	# 2.2 -  Ubicar disparo
def disparar(option):

	if turno == 1:
		cadena = "Jugador dispara a la posicion " + option
	else:
		cadena =  cadena + "CPU dispara a la posicion " + option

def mostrar():
	mapa = os.path.abspath('path2.png') # Obtenemos la imagen que queremos postear
	api.update_with_media(mapa, status = cadena) # Posteamos el disparo en twitter

begin_comm()


