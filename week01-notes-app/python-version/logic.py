import uuid

def add_note(title, content, notes_list):
    """Agrega una nueva nota."""
    note = {
        "id": str(uuid.uuid4()),
        "title": title,
        "content": content
    }
    notes_list.append(note)
    return notes_list

def get_notes(notes_list):
    """Devuelve todas las notas."""
    return notes_list

def update_note(index, new_title, new_content, notes_list):
    """Actualiza una nota existente."""
    if 0 <= index < len(notes_list):
        notes_list[index]["title"] = new_title
        notes_list[index]["content"] = new_content
    return notes_list
def delete_note_by_id(note_id, notes_list):
    """Elimina una nota por su ID."""
    notes_list = [note for note in notes_list if note["id"] != note_id]
    return notes_list
