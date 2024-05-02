import os
import time

unidad = str(input("Horas o Minutos"))
horas = float(input(f"En cuantas {unidad} apagar la computadora?"))
if (unidad == "Horas"):
    segundos = horas * 3600
else:
    segundos = horas * 60  

print(f"La PC se apagará en {horas} {unidad}")
while (segundos>0):
    segundos-=1
    print(segundos)
    time.sleep(1)
    if (segundos<=0):
         os.system(f"shutdown /s /t 1")
         break  
        

