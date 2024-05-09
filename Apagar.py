import os
import time
import requests
import webbrowser

version="v0.0.0"

os.system('cls')
print(f"Iniciando PythonAutoShutdown {version} ")
time.sleep(2)

i=0
while (i<2):
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
            webbrowser.open("https://github.com/MaximilianoEgidi/PythonAutoShutdown/releases")
            exit
        else:
            print("Estás utilizando la versión más reciente.")
    else:
        print("No se pudo obtener la información de la última versión.")

repo_owner = "MaximilianoEgidi"
repo_name = "PythonAutoShutdown"
current_version = version  # Tu versión actual aquí
check_latest_version(repo_owner, repo_name, current_version)

time.sleep(3)
os.system('cls')


# Programa principal
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
        

