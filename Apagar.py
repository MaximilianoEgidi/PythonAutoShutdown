import os
import time
import requests
import webbrowser
import tkinter as tk
from tkinter import font
from tkinter import messagebox

version="v1.0.5"

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
def apagar():

    tiempo=float(textoTiempo.get())

    if var.get() == 1:
        segundos=tiempo*3600
        unidad = "horas"
    elif var.get() == 2:
        unidad = "minutos"
        segundos=tiempo*60

    messagebox.showinfo("Alerta", f"La PC se apagara en {tiempo} {unidad}")

    time.sleep(2)
    ventana.withdraw()
    
    while (segundos>0):
        segundos-=1
        print(segundos)
        time.sleep(1)

        if (segundos<=0):
             os.system(f"shutdown /s /t 1")
             break

# Ventana

ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Python Auto Shutdown")


fuente_titulo = font.Font(family="Helvetica", size=22, weight="bold")
fuente_subtitulo = font.Font(family="Helvetica", size=12, weight="bold")
fuente_texto = font.Font(family="Helvetica", size=12, weight="bold")


presentacion = tk.Label(ventana, text="Python Auto Shutdown", font=fuente_titulo, fg="blue")
presentacion.pack(pady=10)


var = tk.IntVar(value=1)
checkBoxHoras = tk.Radiobutton(ventana, text="Horas", variable=var, value=1, font=fuente_texto)
checkBoxMinutos = tk.Radiobutton(ventana, text="Minutos", variable=var, value=2, font=fuente_texto)
checkBoxHoras.pack(pady=2)
checkBoxMinutos.pack(pady=2)

presentacion = tk.Label(ventana, text="Ingrese un valor", font=fuente_subtitulo, fg="black")
presentacion.pack(pady=10)
textoTiempo = tk.Entry(ventana, font=fuente_texto)
textoTiempo.pack(pady=10)


botonEnviar = tk.Button(ventana, text="Enviar", command=apagar, bg="lightblue", font=fuente_texto)
botonEnviar.pack(pady=5)


ventana.mainloop()