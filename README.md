Project of a battleship game operated with a model client server using Python socketing and MATLAB© GUI

Cliente.py:

  - Gestiona el paso de las funciones indicadas por la GUI de MATLAB para realizar la interacción con el servidor del sistema

Battship-server.py

  - Genera un socket de escucha para realizar la conexión con el cliente
  - Realiza la identificación del usuario en Twitter para la transmisión de datos por la red social
  - Identifica las acciones realizadas por los jugadores, y realiza la actualización del sistema según las mismas
  - Cierra la conexión cuando se finaliza la partida
  
Posibles mejoras:

  - Realizar un servidor activo de manera que el servidor quede en escucha tras finalizar la partida
  - Realizar un servidor multithread de forma que se puedan alojar múltiples partidas de manera simultánea
