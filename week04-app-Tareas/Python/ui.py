import tkinter as tk
from tkinter import messagebox
import logic

class TareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("450x400")
        self.root.resizable(False, False)

        self.create_widgets()
        self.refresh_task_list()

    def create_widgets(self):
        # === MARCO DE ENTRADA DE DATOS ===
        entry_frame = tk.LabelFrame(self.root, text="Nueva / Editar Tarea", padx=10, pady=10)
        entry_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(entry_frame, text="Título:").grid(row=0, column=0, sticky="w")
        self.task_name_entry = tk.Entry(entry_frame, width=40)
        self.task_name_entry.grid(row=0, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Descripción:").grid(row=1, column=0, sticky="w")
        self.task_description_entry = tk.Entry(entry_frame, width=40)
        self.task_description_entry.grid(row=1, column=1, padx=5, pady=3)

        tk.Label(entry_frame, text="Estado:").grid(row=2, column=0, sticky="w")
        self.status_var = tk.StringVar(value="pendiente")
        estados = ["pendiente", "en progreso", "completa"]
        self.task_status_menu = tk.OptionMenu(entry_frame, self.status_var, *estados)
        self.task_status_menu.grid(row=2, column=1, sticky="w", pady=3)

        # === BOTONES DE ACCIÓN ===
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="➕ Añadir", width=12, bg="#4CAF50", fg="white",
                  command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="✏️ Actualizar", width=12, bg="#2196F3", fg="white",
                  command=self.update_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="❌ Eliminar", width=12, bg="#F44336", fg="white",
                  command=self.delete_task).grid(row=0, column=2, padx=5)

        # === LISTA DE TAREAS ===
        list_frame = tk.LabelFrame(self.root, text="Lista de tareas", padx=10, pady=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.task_listbox = tk.Listbox(list_frame, width=60, height=10)
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

    # === FUNCIONES ===
    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        tasks = logic.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, f"{task[0]} - {task[1]} ({task[3]})")

    def add_task(self):
        name = self.task_name_entry.get().strip()
        description = self.task_description_entry.get().strip()
        status = self.status_var.get()

        if not name:
            messagebox.showwarning("Advertencia", "El nombre de la tarea no puede estar vacío.")
            return

        result = logic.add_task(name, description, status)
        print(result)
        self.clear_entries()
        self.refresh_task_list()

    def update_task(self):
        try:
            selection = self.task_listbox.get(tk.ACTIVE)
            task_id = int(selection.split(" - ")[0])

            name = self.task_name_entry.get().strip()
            description = self.task_description_entry.get().strip()
            status = self.status_var.get()

            result = logic.update_task(task_id, name, description, status)
            print(result)
            self.clear_entries()
            self.refresh_task_list()
        except:
            messagebox.showerror("Error", "Selecciona una tarea válida para actualizar.")

    def delete_task(self):
        try:
            selection = self.task_listbox.get(tk.ACTIVE)
            task_id = int(selection.split(" - ")[0])
            logic.delete_task(task_id)
            self.refresh_task_list()
        except:
            messagebox.showerror("Error", "Selecciona una tarea válida para eliminar.")

    def clear_entries(self):
        """Limpia los campos de entrada."""
        self.task_name_entry.delete(0, tk.END)
        self.task_description_entry.delete(0, tk.END)
        self.status_var.set("pendiente")
