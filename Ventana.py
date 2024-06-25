import tkinter as tk
from tkinter import font
from tkinter import messagebox


ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Python Auto Shutdown")


fuente_titulo = font.Font(family="Helvetica", size=22, weight="bold")
fuente_subtitulo = font.Font(family="Helvetica", size=12, weight="bold")
fuente_texto = font.Font(family="Helvetica", size=12, weight="bold")


presentacion = tk.Label(ventana, text="Python Auto Shutdown", font=fuente_titulo, fg="blue")
presentacion.pack(pady=10)


def apagar():
    tiempo = textoTiempo.get()
    print(f"Hola, el tiempo ingresado es: {tiempo}")
    messagebox.showinfo("Alerta", f"Los datos de tiempo son incorrectos")


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
