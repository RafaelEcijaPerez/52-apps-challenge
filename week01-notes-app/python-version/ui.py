'''Creación de la interfaz de la aplicación de notas'''

from tkinter import *
from logic import *
from storage import *

# Lista global de notas
notes_list = load_notes()

def create_main_window():
    window = Tk()
    window.title("Aplicación de Notas")
    window.geometry("400x400")

    barra_menu = Menu(window)
    
    menu_notas = Menu(barra_menu, tearoff=False)
    menu_notas.add_command(label="Nueva nota", command=lambda: create_note_window(window))
    menu_notas.add_command(label="Ver notas", command=lambda: view_notes_window(window))
    menu_notas.add_command(label="Eliminar nota", command=lambda: delete_note_window(window))
    
    barra_menu.add_cascade(menu=menu_notas, label="Notas")
    window.config(menu=barra_menu)

    window.mainloop()

def create_note_window(window):
    note_window = Toplevel(window)
    note_window.title("Crear Nota")
    note_window.geometry("300x200")

    Label(note_window, text="Título:").pack(pady=5)
    title_entry = Entry(note_window, width=30)
    title_entry.pack(pady=5)

    Label(note_window, text="Contenido:").pack(pady=5)
    content_text = Text(note_window, width=30, height=5)
    content_text.pack(pady=5)

    def guardar():
        title = title_entry.get()
        content = content_text.get("1.0", END).strip()
        if title and content:
            global notes_list
            notes_list = add_note(title, content, notes_list)
            save_notes(notes_list)
            note_window.destroy()
        else:
            print("Título o contenido vacío")

    Button(note_window, text="Guardar Nota", command=guardar).pack(pady=10)

def view_notes_window(window):
    view_window = Toplevel(window)
    view_window.title("Ver Notas")
    view_window.geometry("400x300")

    notes_listbox = Listbox(view_window, width=50, height=15)
    notes_listbox.pack(pady=10)

    global notes_list
    notes_listbox.delete(0, END)
    for note in notes_list:
        notes_listbox.insert(END, f"{note['title']}: {note['content']}")

    Button(view_window, text="Cerrar", command=view_window.destroy).pack(pady=5)

def delete_note_window(window):
    delete_window = Toplevel(window)
    delete_window.title("Eliminar Nota")
    delete_window.geometry("400x300")

    notes_listbox = Listbox(delete_window, width=50, height=15)
    notes_listbox.pack(pady=10)

    global notes_list
    for note in notes_list:
        notes_listbox.insert(END, f"{note['title']}")

    def eliminar():
        global notes_list  # <-- importante
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
