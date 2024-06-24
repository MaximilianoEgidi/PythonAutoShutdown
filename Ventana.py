import tkinter as tk
from tkinter import font
from tkinter import messagebox

# Crear ventana
ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Python Auto Shutdown")

# Establecer fuente
fuente_titulo = font.Font(family="Helvetica", size=16, weight="bold")
fuente_texto = font.Font(family="Helvetica", size=12)

# Presentación
presentacion = tk.Label(ventana, text="Python Auto Shutdown", font=fuente_titulo, fg="blue")
presentacion.pack(pady=10)

# Función saludo
def saludo():
    tiempo = textoTiempo.get()
    print(f"Hola, el tiempo ingresado es: {tiempo}")
    messagebox.showinfo("Alerta", f"Los datos de tiempo son incorrectos")

# Opciones de tiempo
var = tk.IntVar(value=1)
checkBoxHoras = tk.Radiobutton(ventana, text="Horas", variable=var, value=1, font=fuente_texto)
checkBoxMinutos = tk.Radiobutton(ventana, text="Minutos", variable=var, value=2, font=fuente_texto)
checkBoxHoras.pack(pady=2)
checkBoxMinutos.pack(pady=2)

# Entrada de tiempo
textoTiempo = tk.Entry(ventana, font=fuente_texto)
textoTiempo.pack(pady=10)

# Botón Enviar
botonEnviar = tk.Button(ventana, text="Enviar", command=saludo, bg="lightblue", font=fuente_texto)
botonEnviar.pack(pady=5)

# Iniciar bucle de eventos
ventana.mainloop()
