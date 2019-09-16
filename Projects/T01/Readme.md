# Tarea 01: InitialP:


## Consideraciones generales :octocat:

*Todo comando que sea ingresado debe ser un numero almenos que se indique lo contrarío, es decir, se le este asignando un nombre a un vehículo o jugador

### Cosas implementadas y no implementadas :white_check_mark: :x:

* **Menús**: <Implementado en módulo "menus.py">
   * Menú sesión: < implementado >
   * Menú principal: < implementado >
   * Menú configurar carrera: < implementado >
   * Menú carrera: < implementado >
   * Menú pits: < implementado >
   * Menú comprar auto: < implementado >
* **Flujo de carrera**: <Implementado en módulo "carrera.py">
    * La velocidad real aparentemente siempre me da valores negativos, por lo tanto,  siempre se utiliza la velocidad mínima.
* **Entidades**: <Implementado en módulo "carrera.py">
   * Vehículo: < implementado >
   * Pista: < implementado >
   * Piloto: < implementado >
* **Archivos**: <Implementado en módulo "carrera.py">
   * Nueva partida: < implementado >
   * Cargar partida: < implementado >
   * Guardar partida: < implementado >
* **Fórmulas**: <Implementado en módulo "funciones.py">
   * Cálculo de velocidad: < implementado >
   * Sucesos durante la carrera: < implementado >
   * Ganador de la carrera: < implementado >
* **Bonus**: <Implementado en módulo "menus.py y funciones.py">
   * Cálculo de velocidad: < implementado >

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```InitialP.py```:

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random```: ```randint(), uniform(), random()```
2. ```math```: ```ceil()``` 
3. ```abc```: ```ABC```
4. ```os```: ```path``` 

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus```: Contiene a ```Menu```, ```Menu_sesion```, ```Menu_principal```, ```Menu_buy```, ```Menu_pits```, ```Menu_race_configuration```, ```Menu_race```
2. ```carrera```: Contiene a ```Car```, ```Racer```, ```Track```, ```Race```, ```Game```
3. ```funciones```
4. ```parametros```

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:**  No alcance a colocar la explicación de las funciones en el programa, así que las colocaré aquí por si son de utilidad
* ** Módulo <menus.py>**:
   * print(): Lo posee cada clase se encarga de utilizar la funcion print_options() sobre cada elemento de self.options y despues imprime f"[0] {self.exit}".
 Si se encuentra dentro de la clase Menu_race se ha utilizado un funcionamiento similar, pero solo para una opcion.
 En Menu_pits y Menu_buy se ha modificado para imprimir el index, la opciones a comprar y su precio.
   * selection(): Utiliza self.print() y luego se asegura que el comando ingresado sea un número solo compuesto por unidades, entonces devuelve el comando.
 Si no se cumple esta condición devuelve False.
 En Menu_pits y Menu_buy también se asegura que el dinero del jugador también sea mayor o igual a al precio de la opción seleccionada.
 En Menu_race_configuration le pide al usuario ingresar dos comandos numericos que solo se compongan de unidades y despúes genera una instancia de la clase Race y la retorna
   * print_options(): Se ecarga de recibir una lista, posteriormente imprime el index de la lista junto a el elemento de la lista

* ** Módulo <menus.py>**:

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
