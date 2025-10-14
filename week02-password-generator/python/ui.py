#interfaz del generador de contraseñas
import tkinter as tk
from tkinter import messagebox
from logic import set_length, generate_password, get_password, get_history

#crear la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.geometry("400x300")

#Escoger la longitud de la contraseña
length_label = tk.Label(root, text="Longitud de la Contraseña:")
length_label.pack(pady=10)
length_var = tk.IntVar(value=12)
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()
def update_length():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "La longitud debe ser al menos 4")
        else:
            set_length(length)
            messagebox.showinfo("Éxito", f"Longitud establecida a {length}")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido")

set_length_button = tk.Button(root, text="Establecer Longitud", command=update_length)
set_length_button.pack(pady=10)
#Generar la contraseña
def generate():
    password = generate_password()
    password_var.set(password)
    messagebox.showinfo("Contraseña Generada", f"Tu nueva contraseña es:\n{password}")
generate_button = tk.Button(root, text="Generar Contraseña", command=generate)
generate_button.pack(pady=10)
#Mostrar la contraseña generada
password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Helvetica", 12))
password_label.pack(pady=10)

# Permitir copiar la contraseña al portapapeles (usa primero lo mostrado en pantalla)
def copy_to_clipboard():
    # Obtener la contraseña mostrada en la UI; si está vacía, intentar obtenerla desde la lógica
    password = password_var.get() or get_password()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")
    else:
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar")

# Botón fijo para copiar la contraseña generada (visible en la pantalla principal)
copy_button_main = tk.Button(root, text="Copiar Contraseña", command=copy_to_clipboard)
copy_button_main.pack(pady=5)

#Mostrar el historial de contraseñas
def show_history():
    history = get_history()
    if history:
        history_str = "\n".join(history)
        messagebox.showinfo("Historial de Contraseñas", history_str)
        # Ya no se crea un botón adicional aquí para copiar; se usa el botón principal
    else:
        messagebox.showinfo("Historial de Contraseñas", "No hay historial disponible.")
history_button = tk.Button(root, text="Ver Historial de Contraseñas", command=show_history)
history_button.pack(pady=10)
#Iniciar la interfaz
root.mainloop()

