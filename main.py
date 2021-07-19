# Ingresamos las librerias insertadas previamente de python
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Indicamos los pines y el grosor de la pantalla, mas un nombre a este
i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = SSD1306_I2C(128, 64, i2c)

# Asignamos el pulsador a la entrada 18 como INPUT
pul = Pin(18, Pin.IN, Pin.PULL_DOWN)

# Iniciamos con la pantalla limpia
oled.fill(0)

global estacion
estacion = 0

global estado_anterior
estado_anterior = 0


# Se observa como actua el contador con el antirrebote
"""
while True:

    if pul.value() and estado_anterior == 0:
        estacion += 1
        estado_anterior = pul.value()
    elif not pul.value() and estado_anterior == 1:
        estado_anterior = 0

    oled.fill(0)
    oled.text(str(pul.value()), 0, 0)
    oled.text(str(estado_anterior), 20, 0)
    oled.text(str(estacion), 30, 0)
    oled.show()
"""

# Se abre un bucle while
while True:
    # Se comprueba el numero de estacion
    if estacion == 0:
        if pul.value() and estado_anterior == 0:
            estacion += 1
            estado_anterior = pul.value()
        elif not pul.value() and estado_anterior == 1:
            estado_anterior = 0
        oled.fill(0)
        oled.text("Hola mundo", 0, 0)
        oled.show()

    elif estacion == 1:
        if pul.value() and estado_anterior == 0:
            estacion += 1
            estado_anterior = pul.value()
        elif not pul.value() and estado_anterior == 1:
            estado_anterior = 0
        oled.fill(0)
        oled.text("Que tal", 0, 0)
        oled.show()

    elif estacion == 2:
        if pul.value() and estado_anterior == 0:
            estacion = 0
            estado_anterior = pul.value()
        elif not pul.value() and estado_anterior == 1:
            estado_anterior = 0
        oled.fill(0)
        oled.text("Yo muy bien", 0, 0)
        oled.show()
