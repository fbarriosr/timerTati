## TIMER TATI

Es un TIMER que ayuda a las presentaciones en los audidorios
## Requerimientos

Requiere python 3, pygame


## Installation

Instala Python3 en tu sistema de operativo. Puedes descargalo del sitio web o desde Store de Win 11.

Luego usando powershell en win u otra terminal, instala pygame
```
$pip install pygame
```

Descarga el proyecto desde Github usando la opción zip o git clone. Mueve el proyecto timerTati a una carpeta en tu computador. 

Descomprime el archivo zip mediante consola o usando las herramientas del sistema operativo (click derecho descomprimir)
```
$unzip timerTati.zip
```

## Ejecución

Ejecutar el programa mediante el comando python en tu direcctorio con las siguientes opciones:
```
-m: minutos TIMER
-s: segundos TIMER
-a: alarma en segundos TIMER
```
Un ejemplo para un timer de 10 minutos 10 segundos con alarma de 5 segundos es de:
```
$ python screen.py -m 10 -s 10 -a 5
```

Un ejemplo para un timer de 10 segundos con alarma de 6 segundos es de:
```
$ python screen.py -s 10 -a 6
```
Un ejemplo para un timer de 50 segundos con alarma de 20 segundos (default) es de:
```
$ python screen.py -s 50
```




