# PYTHON 🐍

Python es lenguaje de programación multiparadigma, ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional. Es un lenguaje interpretado, dinámico y multiplataforma.

Python es muy elogiado por su elegante sintaxis y su código legible, si estás comenzando tu carrera de programación, Python se adapta a tus necesidades.

* Facil
* Elegante
* Buenas practicas

Python tienen una amplia gama de usos. Desde procesamiento de datos, al aprendizaje de máquina. Por ello, Python es elegido como el lenguaje de programación de muchas empresas y organizaciones.

Campos de uso de Python:
* **Frontend:** Se encarga de llevar el diseño de una aplicación o sitio web a código

* **IoT:** Se encarga de darle la capacidad de conectarse a internet a elementos que pueden estar a nuestro alrededor.

* **IA:** Se encarga de enseñarle a la computadora a resolver un determinado problema sin la necesidad de estar involucrados constantemente.

* **Backend:** Se encarga de crear la lógica con la cual va a funcionar una determinada aplicación y que va a ser almacenada en un servidor.

* **DevOps:** Se encarga de manejar la información almacenada en la nube de una determinada aplicación.

* **Data Science:** Se encarga de tomar la información relevante de un determinado ambiente y poder sacar conclusiones al respecto.

* **Videojuegos:** Se encarga de combinar la programación, el diseño y la música para generar grandes experiencias a los usuarios.

* **Desarrollo móvil:** Se encarga de crear aplicaciones que serán almacenadas en la PlayStore o AppStore, y que podremos hacer uso de ellas desde nuestros smartphones.

### De todos estos Pytho funciona muy bien en los siguientes campos:

* **IoT**

* **Inteligencia Artificial**

* **Backend**

* **Data Science**

## ALGORITMOS

Dentro de todo lenguaje de programación existe un núcleo llamado algoritmo. Un algoritmo es una serie de pasos ordenados para resolver un problema.
Este es:

* finito
* ordenado
* no ambiguo.


### Definiciones de algoritmo:

**Algoritmo:** Conjunto ordenado de operaciones sistemáticas que permite hacer un cálculo y hallar la solución de un tipo de problema.
**Algoritmo:** Se denomina algoritmo a un grupo finito de operaciones organizadas de manera lógica y ordenada que permite solucionar un determinado problema.
**Algoritmo:** una serie de instrucciones o reglas establecidas que, por medio de una sucesión de pasos, permiten arribar a un resultado o solución.
**Algoritmo:** una secuencia de instrucciones que representan un modelo de solución para determinado tipo de problemas. O bien como un conjunto de instrucciones que realizadas en orden conducen a obtener la solución de un problema.

### ¿Cómo se Diseña un Algoritmo?:

En programación, un algoritmo establece, de manera genérica e informal, la secuencia de pasos o acciones que resuelve un determinado problema y, para representarlo, se utiliza, fundamentalmente, dos tipos de notación:

* pseudocódigo
* diagramas de flujo.

### Partes de un Algoritmo:

Todo algoritmo debe obedecer a la estructura básica de un sistema, es decir: entrada, proceso y salida.

### Características de los Algoritmos:

Las características fundamentales que debe cumplir todo algoritmo son:

* Un algoritmo debe ser preciso e indicar el orden de realización de cada paso.

* Un algoritmo debe estar definido. Si se sigue un algoritmo dos veces, se debe obtener el mismo resultado cada vez.

* Un algoritmo debe ser finito. el algoritmo se debe terminar en algún momento; o sea, debe tener un número finito de pasos.

* Un algoritmo debe ser legible: El texto que lo describe debe ser claro, tal que permita entenderlo y leerlo fácilmente.


## OPERACIONES CON PYTHON

SUMA
```
# En consola
5 + 5

# En editor de código
print(5 + 5)
```

RESTA
```
# En consola
5 - 5

# En editor de código
print(5 - 5)
```

MULTIPLICACIÓN
```
# En consola
5 * 5

# En editor de código
print(5 * 5)
```

DIVISIÓN
```
# En consola
5 / 25

# En editor de código
print(5 / 25)

# En caso de división entera
21 // 5
# Para ver lo que resta
21 % 5
```

POTENCIA
```
# En consola
5 ** 5

# En editor de código
print(5 ** 5)
```

RAÍZ
```
# Hay dos métodos para ésta operación:
9 ** (1/2)
9 ** .5

# En editor de código
print(9 ** (1/2))
```

**Python sigue el orden de presedencia en operaciones**
1 * Parentesis
2 * Potencias y raices
3 * multiplicaciones y divisiones
4 * sumas y restas


### VARIABLES

Una variable = a una caja

Las variables pueden recibir un nobre = identificador

ASIGNAR VALORES

```
nx = 230
ny = 400
print(nx + ny)
```

```
nx = 230
ny = 400
nR = nx + ny
print(nR)
```

**Reglas en el uso de identificadores de variable**
* No pueden empezar con un número.
* Deben estar en minúsculas
* Para separar las palabras usamos el guion bajo: _
* Estas reglas son aplicadas al lenguaje Python, en otros lenguajes puede haber otras reglas.


### TIPOS DE DATOS

Strings
```
# Los textos pueden llevar "" o ''
nx = 'Francisco '
ny = 'Zúñiga'
nR = nx + ny
print(nR)
```

Decimales
```
nx = 2.5
# La ' , ' no funciona porque Python esta basado en el idioma "Inglés"
```

Booleanos
```
nx = True
ny = False
```

### Operadores lógicos
* and ( y ): compara dos valores, y si ambos son verdaderos, devuelve True.
* or ( ó ): si al comparar dos valores y uno de los dos se cumple, devuelve True. Solo * devuelve falso cuando los dos valores no se cumplen.
* not ( no): invierte el valor de una variable, dando el valor contrario al de la variable evaluada.

### Operadores de comparación
* == ( igual qué ): determina si dos valores son iguales o no.
* != (diferente de): determina si dos valores son distintos o no. Si los valores son diferentes devuelve True, si son iguales devuelve False.
* > (mayor que): compara dos valores, y determina si es mayor que el otro.
* < (menor que): compara dos valores y determina si es menor que el otro.
* >= (mayor o igual): compara dos valores y determinas si es mayor o igual que el otro.
* <= (menor o igual): compara dos valores y determinas si es menor o igual que el otro.

```
nx = True
ny = False

n2 and n1
# Esto imprime False

n1 or n2
# Esto imprime True

not n1
# False

not n2
# True

nx = 10
ny = 10

nx == ny
# True

```