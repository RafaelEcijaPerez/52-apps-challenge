# interfaz.py
import tkinter
import logic

class TareasApp:
    def __init__(self, root):
        self.root = root
        root.title("Tareas App")
        root.geometry("400x350")
        self.create_widgets()
        self.refresh_task_list()

    def create_widgets(self):
        # Entradas de texto
        tkinter.Label(self.root, text="Nombre de tarea:").pack()
        self.task_name_entry = tkinter.Entry(self.root, width=30)
        self.task_name_entry.pack()

        tkinter.Label(self.root, text="Descripción:").pack()
        self.task_description_entry = tkinter.Entry(self.root, width=30)
        self.task_description_entry.pack()

        tkinter.Label(self.root, text="Estado (pendiente / completa):").pack()
        self.task_status_entry = tkinter.Entry(self.root, width=30)
        self.task_status_entry.pack()

        # Botones
        button_frame = tkinter.Frame(self.root)
        button_frame.pack(pady=5)

        tkinter.Button(button_frame, text="➕ Añadir", command=self.add_task).grid(row=0, column=0, padx=5)
        tkinter.Button(button_frame, text="✏️ Actualizar", command=self.update_task).grid(row=0, column=1, padx=5)
        tkinter.Button(button_frame, text="❌ Eliminar", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tkinter.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

    def refresh_task_list(self):
        self.task_listbox.delete(0, tkinter.END)
        tasks = logic.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tkinter.END, f"{task[0]} - {task[1]} ({task[3]})")

    def add_task(self):
        name = self.task_name_entry.get()
        description = self.task_description_entry.get()
        status = self.task_status_entry.get() or "pendiente"

        if name:
            logic.add_task(name, description, status)
            self.refresh_task_list()
            self.task_name_entry.delete(0, tkinter.END)
            self.task_description_entry.delete(0, tkinter.END)
            self.task_status_entry.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning("Advertencia", "El nombre de la tarea no puede estar vacío.")

    def update_task(self):
        try:
            selection = self.task_listbox.get(tkinter.ACTIVE)
            task_id = int(selection.split(" - ")[0])
            name = self.task_name_entry.get()
            description = self.task_description_entry.get()
            status = self.task_status_entry.get()

            logic.update_task(task_id, name, description, status)
            self.refresh_task_list()
        except:
            tkinter.messagebox.showerror("Error", "Selecciona una tarea válida para actualizar.")

    def delete_task(self):
        try:
            selection = self.task_listbox.get(tkinter.ACTIVE)
            task_id = int(selection.split(" - ")[0])
            logic.delete_task(task_id)
            self.refresh_task_list()
        except:
            tkinter.messagebox.showerror("Error", "Selecciona una tarea válida para eliminar.")
