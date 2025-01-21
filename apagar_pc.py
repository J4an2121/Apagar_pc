import os #Se usa para interactuar con el sistema operativo y ejecutar comandos del sistema, como apagar el PC.

shutdown = input( "Quies apargar el pc ? (si /no)")  #Solicita una entrada del usuario, en este caso para preguntar si quiere apagar el PC.

if shutdown.lower() == "si": #Es un comando del sistema operativo Windows que apaga el PC en 1 segundo. /s indica que se apagará y /t 1 es el tiempo de espera (1 segundo).

 os.system("shutdow /s /t 1")

else:

 exit() #Termina la ejecución del programa si el usuario responde "no".