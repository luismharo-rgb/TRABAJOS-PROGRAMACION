import random
import time

saludos=["una gran ciudad", 
         "un precioso lugar", 
         "que lindo que se pasa ahí!", 
         "me gustaría ir un día"
         "el invierno ahi es precioso"
         "el verano ahí es precioso"
         "la primavera ahí es preciosa"
         "el otoño ahí es precioso"
         "la gente ahi es muy amable"
         "me gusta la comida de ahí"
         ]
nombre=input("Ingrese su nombre: ")
ciudad=input("Ingrese el nombre de tu ciudad de origen: ")
ram_saludo=random.choice(saludos)
time.sleep(2)
print("Hola", nombre, ", eres de", ciudad, "?", ram_saludo)
