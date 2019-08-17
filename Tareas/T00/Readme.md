# Tarea 00: LegoSweeper

## Consideraciones generales :octocat:

* Los comandos del menú solo funcionan con números, excepto al seleccionar casillas porque también se utilizan letras. 
* El nombre de usuario no puede contener signos gráficos sobre las vocales, por ejemplo, día, pingüino o virtù, ya que generá un error en la función writelines(). 

### Formato de guardar partida:

Se genera un archivo .sav en la carpeta partidas que tiene el siguiente formato:  
3 -> Ancho del tablero  
3 -> Largo del tablero  
1 -> Cantidad de legos del tablero  
esp/esp/esp -> Información de las posiciones de los legos en el tablero,  
esp/esp/ L &nbsp; &nbsp; &nbsp; &nbsp; se trata de una lista donde cada elemento se separa con "/"  
esp/esp/esp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   y cada linea representa una fila  
0/1/esp -> Información de el tablero mostrado al usuario, utiliza el  
0/1/esp &nbsp;&nbsp;&nbsp;&nbsp; mismo formato del caso anterior separando cada elemento de  
0/1/esp&nbsp; &nbsp; &nbsp; la lista con "/" y cada linea representa una fila  
***esp será un espacio en blanco en el archivo guardado**  
****La información del tablero se almacena en una lista de listas**  
### Cosas implementadas y no implementadas :white_check_mark: :x: 

* **Menús**:
   * Menú principal: < implementado >
   * Menú de juego: < implementado >
* **Partida**:
   * Crear: < implementado >
   * Cargar: < implementado >
   * Guardar: < implementado >
* **Reglas**: < implementado >
* **Puntuación**:
   * Puntuación final: < implementado >
   * Ranking: < implementado >
* ***Bonus***:
   * Descubrimiento de celdas: < implementado >

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


## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. < No se puede perder en el primer turno, ya que sería injusto que el jugador pierda de una manera tan azarosa sin acceso a ningún tipo de información > 

-------