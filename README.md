# Refugio Valenzuela

Programa en Python que simula un día en un refugio de animales. Define la clase `Animal`, crea a Luna, Rocky y Kiwi, los hace presentarse con un mensaje de **cowsay** y les aplica actividades (jugar, comer y dormir) que modifican su energía, la cual siempre se mantiene entre 0 y 100.

## Requisitos

- **Python 3.10 o superior.** Para verificarlo: `python --version` (en Mac: `python3 --version`).
- **pip**, el instalador de paquetes de Python (viene incluido con Python).
- **Git**, para clonar el repositorio. Para verificarlo: `git --version`.
- Las dependencias de Python están en `requirements.txt` y se instalan en el paso de instalación:
  - `cowsay==6.1`: muestra los mensajes de los animales dentro de un recuadro.

## Instalación

1. Clonar el repositorio:

```
git clone https://github.com/gaanvapezz/refugio-valenzuela.git
```

2. Entrar a la carpeta del proyecto:

```
cd refugio-valenzuela
```

3. Instalar las dependencias:

```
pip install -r requirements.txt
```

En Mac, si `pip` no funciona, use `pip3 install -r requirements.txt`.

## Ejecución

Desde la carpeta del proyecto, ejecute:

```
python main.py
```

En Mac, el comando suele ser `python3 main.py`.

### Salida esperada

Cada animal se presenta dentro de un recuadro de cowsay y al final se imprime su energía:

```
Luna: energia 75
Rocky: energia 30
Kiwi: energia 90
```

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `animal.py` | Clase `Animal` con los métodos `presentarse()`, `comer(gramos)`, `jugar()` y `dormir()`. |
| `main.py` | Simula un día en el refugio con Luna, Rocky y Kiwi. |
| `requirements.txt` | Paquetes que necesita el proyecto. |
| `README.md` | Este archivo. |

## Funcionamiento de la clase Animal

- Cada animal tiene `nombre`, `especie`, `edad` y `energia`, que empieza en 50.
- `presentarse()`: muestra "Hola, soy NOMBRE. Especie: ESPECIE. Edad: EDAD años." con cowsay.
- `comer(gramos)`: suma `gramos // 10` a la energía.
- `jugar()`: resta 20 a la energía.
- `dormir()`: suma 30 a la energía.
- La energía nunca baja de 0 ni pasa de 100.