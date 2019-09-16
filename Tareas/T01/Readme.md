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
    * <Nombre subitem pauta<sub>2.1</sub>>: Hecha completa 
    * <Nombre subitem pauta<sub>2.2</sub>>: Me faltó hacer <insertar qué cosa faltó>
    * ...
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
El módulo principal de la tarea a ejecutar es  ```archivo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


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



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/master/Tareas/Descuentos.md).
