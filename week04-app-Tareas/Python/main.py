# Archivo main.py — Aplicación de Tareas
import tkinter as tk
import database
import logic
import ui

def main():
    # Crear tabla en la base de datos si no existe
    database.create_table()

    # Iniciar la interfaz principal
    root = tk.Tk()
    app = ui.TareasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
