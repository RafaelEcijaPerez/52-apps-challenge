'''Creación de la interfaz de la aplicación de notas'''

from tkinter import *
from logic import *
from storage import *

# Carga la lista global de notas desde almacenamiento
notes_list = load_notes()

# Función principal para crear la ventana de la aplicación
def create_main_window():
    window = Tk()  # Crea la ventana principal
    window.title("Aplicación de Notas")  # Título de la ventana
    window.geometry("400x400")  # Tamaño de la ventana

    barra_menu = Menu(window)  # Barra de menú principal
    menu_notas = Menu(barra_menu, tearoff=False)  # Menú de opciones de notas
    
    # Frame donde se mostrará el contenido dinámico (formularios, listas, etc.)
    content_frame = Frame(window)
    content_frame.pack(fill=BOTH, expand=True)

    # Función para limpiar el frame antes de mostrar nuevo contenido
    def clear_frame():
        for widget in content_frame.winfo_children():
            widget.destroy()

    # Muestra el formulario para crear una nueva nota en el frame principal
    def show_create_note():
        clear_frame()  # Limpia el frame
        Label(content_frame, text="Título:").pack(pady=5)  # Etiqueta para el título
        title_entry = Entry(content_frame, width=30)  # Campo de entrada para el título
        title_entry.pack(pady=5)
        Label(content_frame, text="Contenido:").pack(pady=5)  # Etiqueta para el contenido
        content_text = Text(content_frame, width=30, height=5)  # Campo de texto para el contenido
        content_text.pack(pady=5)
        # Función para guardar la nota
        def guardar():
            title = title_entry.get()  # Obtiene el título
            content = content_text.get("1.0", END).strip()  # Obtiene el contenido
            if title and content:  # Verifica que ambos campos tengan datos
                global notes_list
                notes_list = add_note(title, content, notes_list)  # Agrega la nota
                save_notes(notes_list)  # Guarda las notas
                show_view_notes()  # Muestra la lista de notas después de guardar
            else:
                print("Título o contenido vacío")  # Mensaje si falta información
        Button(content_frame, text="Guardar Nota", command=guardar).pack(pady=10)  # Botón para guardar

    # Muestra la lista de notas en el frame principal
    def show_view_notes():
        clear_frame()  # Limpia el frame
        notes_listbox = Listbox(content_frame, width=50, height=15)  # Listbox para mostrar notas
        notes_listbox.pack(pady=10)
        global notes_list
        notes_listbox.delete(0, END)  # Limpia el Listbox
        for note in notes_list:  # Agrega cada nota al Listbox
            notes_listbox.insert(END, f"{note['title']}: {note['content']}")

    # Muestra la opción para eliminar una nota en el frame principal
    def show_delete_note():
        clear_frame()  # Limpia el frame
        notes_listbox = Listbox(content_frame, width=50, height=15)  # Listbox para seleccionar nota a eliminar
        notes_listbox.pack(pady=10)
        global notes_list
        for note in notes_list:  # Agrega los títulos de las notas al Listbox
            notes_listbox.insert(END, f"{note['title']}")
        # Función para eliminar la nota seleccionada
        def eliminar():
            global notes_list
            seleccion = notes_listbox.curselection()  # Obtiene la selección
            if seleccion:
                index = seleccion[0]  # Índice de la nota seleccionada
                note_to_delete = notes_list[index]  # Nota a eliminar
                note_id = notes_list[index]["id"]  # ID de la nota
                notes_list = delete_note_by_id(note_id, notes_list)  # Elimina la nota
                save_notes(notes_list)  # Guarda los cambios
                notes_listbox.delete(index)  # Elimina de la interfaz
                print(f"Nota eliminada: {note_to_delete['title']}")  # Mensaje de confirmación
        Button(content_frame, text="Eliminar Nota", command=eliminar).pack(pady=5)  # Botón para eliminar

    # Modificar las opciones del menú para que actualicen el frame principal
    menu_notas.add_command(label="Nueva nota", command=show_create_note)
    menu_notas.add_command(label="Ver notas", command=show_view_notes)
    menu_notas.add_command(label="Eliminar nota", command=show_delete_note)
    
    barra_menu.add_cascade(menu=menu_notas, label="Notas")  # Añade el menú de notas a la barra principal
    window.config(menu=barra_menu)  # Configura la barra de menú en la ventana

    window.mainloop()  # Inicia el bucle principal de la interfaz

# Función para crear una ventana secundaria para crear notas (no se usa en el frame principal)
def create_note_window(window):
    note_window = Toplevel(window)  # Crea una ventana secundaria
    note_window.title("Crear Nota")
    note_window.geometry("300x200")

    # Campos para el título y contenido de la nota
    Label(note_window, text="Título:").pack(pady=5)
    title_entry = Entry(note_window, width=30)
    title_entry.pack(pady=5)

    Label(note_window, text="Contenido:").pack(pady=5)
    content_text = Text(note_window, width=30, height=5)
    content_text.pack(pady=5)

    # Función para guardar la nota
    def guardar():
        title = title_entry.get()
        content = content_text.get("1.0", END).strip()
        if title and content:
            global notes_list
            notes_list = add_note(title, content, notes_list)
            save_notes(notes_list)
            note_window.destroy()  # Cierra la ventana secundaria
        else:
            print("Título o contenido vacío")

    Button(note_window, text="Guardar Nota", command=guardar).pack(pady=10)

# Función para crear una ventana secundaria para ver notas (no se usa en el frame principal)
def view_notes_window(window):
    view_window = Toplevel(window)  # Crea una ventana secundaria
    view_window.title("Ver Notas")
    view_window.geometry("400x300")

    notes_listbox = Listbox(view_window, width=50, height=15)
    notes_listbox.pack(pady=10)

    global notes_list
    notes_listbox.delete(0, END)
    for note in notes_list:
        notes_listbox.insert(END, f"{note['title']}: {note['content']}")

    Button(view_window, text="Cerrar", command=view_window.destroy).pack(pady=5)

# Función para crear una ventana secundaria para eliminar notas (no se usa en el frame principal)
def delete_note_window(window):
    delete_window = Toplevel(window)  # Crea una ventana secundaria
    delete_window.title("Eliminar Nota")
    delete_window.geometry("400x300")

    notes_listbox = Listbox(delete_window, width=50, height=15)
    notes_listbox.pack(pady=10)
    
    global notes_list
    for note in notes_list:
        notes_listbox.insert(END, f"{note['title']}")

    # Función para eliminar la nota seleccionada
    def eliminar():
        global notes_list
        seleccion = notes_listbox.curselection()
        if seleccion:
            index = seleccion[0]
            note_to_delete = notes_list[index]
            note_id = notes_list[index]["id"]
            notes_list = delete_note_by_id(note_id, notes_list)
            save_notes(notes_list)
            notes_listbox.delete(index)
            print(f"Nota eliminada: {note_to_delete['title']}")

    Button(delete_window, text="Eliminar Nota", command=eliminar).pack(pady=5)
    Button(delete_window, text="Cerrar", command=delete_window.destroy).pack(pady=5)
