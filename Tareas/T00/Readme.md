# Tarea 00: LegoSweeper

## Consideraciones generales :octocat:

> Adentrate en Legosweeper la increible simulación que te permite sentir la emocionante experiencia de evitar 
> legos escondidos en baldosas. Para está misión se te entregara información por cada baldosa descubierta sin
> un lego, en caso contrario, si se llega a encontrar con un mortal lego la simulación acabará para proteger
> al usuario. Al descubrir una casilla se entrega informacion de la cantidad casillas de adyacentes que poseen
> un lego *(si el numero entregado es cero se revelarán las casillas adyacentes de manera automática)*, el
> objetivo es descubrir todas las casillas sin un lego. Al finalizar se proporcionará una puntuación
> correspondiente a la dificultad de la simulación y las casillas descubiertas, si esta es digna podrá ser
> almacenada en el ranking con los 10 mejores puntajes registrados hasta el momento.
> Si el usuario no es capaz de continuar con la actividad, o no desea perder la simulación generada, existe
> la opción de guardar los datos de la partida para continuar más tarde.

###Formato de guardad partida:
Se genera un archivo .sav en la carpeta partidas que tiene el siguiente formato:
Ancho del tablero
Largo del tablero
Cantidad de legos del tablero
Información de las posiciones de los legos en el tablero, se trata de una lista donde cada elemento se separa con "/" y cada linea representa una fila
Información de el tablero mostrado al usuario, utiliza el mismo formato de los legos separando cada elemento de la lista con "/"
** *La información del tablero se almacena en una lista de listas
### Cosas implementadas y no implementadas :white_check_mark: :x:

* Parte <X<sub>1</sub>>: Hecha completa
* Parte <X<sub>2</sub>>: Hecha completa
* Parte <X<sub>3</sub>>: Hecha completa
* Parte <X<sub>4</sub>>: Hecha completa
* Parte <X<sub>5</sub>>: Hecha completa
* Parte <X<sub>6</sub>>: Hecha completa
* Parte <X<sub>7</sub>>: Hecha completa
* Parte <X<sub>8</sub>>: Hecha completa

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```Legosweeper.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```-> ```randint()```
2. ```os```-> ```path```
3. ```os```-> ```makedirs()```
4. ```sys```-> ```exit()```
5. ```parametros```
6. ```tablero```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. Ninguna de momento

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. < No se puede perder en el primer turno, ya que sería injusto que el jugador pierda de una manera tan azarosa sin acceso a ningún tipo de información > 
2. < Se asume que el nombre de usuario no tiene caracteres especiales como cremillas. Se pueden colocar tildes, pero se eliminaran. El método que conosco para realizar esto no está permitido >

-------
## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. No utilicé código de terceros



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).