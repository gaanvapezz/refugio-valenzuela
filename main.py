"""
Simulación de una día en el refugio
"""

from animal import Animal

animal1 = Animal("Luna", "Gato", 3)
animal2 = Animal ("Rocky", "Perro", 5)
animal3 = Animal("Kiwi", "Loro", 2)


#Presentaciones

animal1.presentarse()
animal2.presentarse()
animal3.presentarse()

#Actividad luna
animal1.jugar()
animal1.comer(150)
animal1.dormir()

#Activad Rocky
animal2.jugar()
animal2.jugar()
animal2.jugar()
animal2.comer(300)

#Actividad Kiwi
animal3.comer(100)
animal3.dormir()

#VIDA

animal1.observar_vida()
animal2.observar_vida()
animal3.observar_vida()


