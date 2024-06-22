import os
import time
import requests
import webbrowser

version="v1.0.3"

os.system('cls')
print(f"Iniciando PythonAutoShutdown {version} ")
time.sleep(2)

i=0
while (i<1):
    os.system('cls')
    print("Cargando.")
    time.sleep(1)
    os.system('cls')
    print("Cargando..")
    time.sleep(1)
    os.system('cls')
    print("Cargando...")
    time.sleep(1)
    os.system('cls')
    i+=1


#Checkeo de version

def check_latest_version(repo_owner, repo_name, current_version):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    response = requests.get(url)
    if response.status_code == 200:
        latest_version = response.json()["tag_name"]
        if latest_version != current_version:
            print(f"¡Hay una nueva versión disponible! Versión actual: {current_version}, Última versión: {latest_version}")

            print("Desea descargar la versión mas reciente del programa?")
            rta = input("S o N ")
            if (rta == "S"):
                webbrowser.open("https://github.com/MaximilianoEgidi/PythonAutoShutdown/releases")
                exit
        else:
            print("Estás utilizando la versión más reciente.")
    else:
        print("No se pudo obtener la información de la última versión.")

repo_owner = "MaximilianoEgidi"
repo_name = "PythonAutoShutdown"
current_version = version  
check_latest_version(repo_owner, repo_name, current_version)

time.sleep(3)
os.system('cls')


# Programa principal

unidad = ""
while unidad != "H" and unidad != "M":
    unidad = input("Horas o Minutos (H o M): ").upper()
    os.system("cls")
    if unidad != "H" and unidad != "M":
        print("Entrada inválida. Por favor, ingresa 'H' para Horas o 'M' para Minutos.")
        time.sleep(4)
        os.system("cls")

if (unidad=="H"):
    unidad="Horas"
else:
    if(unidad=="M"):
        unidad="Minutos"

if (unidad=="Horas"):    
    horas = float(input(f"En cuantas horas apagar la computadora?"))
else:
    if(unidad=="Minutos"):
        horas = float(input(f"En cuantos minutos apagar la computadora?"))


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
        

