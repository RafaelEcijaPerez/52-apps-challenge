#Logica del programa de Tareas
import database

def validate_task_data(title, status):
    """Valida los datos básicos de una tarea"""
    errors = []
    if not title or len(title.strip()) == 0:
        errors.append("Title is required")
    if not status or status not in ['pending', 'in progress', 'completed']:
        errors.append("Valid status is required (pending, in progress, completed)")
    return errors

#Función para agregar una nueva tarea
def add_task(title, description, status):
    errors = validate_task_data(title, status)
    if errors:
        return "Error: " + ", ".join(errors)
    
    database.insert_task(title.strip(), description, status.lower())
    return "Task added successfully."

#Función para obtener todas las tareas
def get_tasks():
    return database.get_all_tasks()


#Función para actualizar una tarea existente
def update_task(task_id, title, description, status):
    if not task_id or task_id <= 0:
        return "Error: Invalid task ID"
        
    errors = validate_task_data(title, status)
    if errors:
        return "Error: " + ", ".join(errors)
    
    database.update_task(task_id, title.strip(), description, status.lower())
    return "Task updated successfully."

#Función para eliminar una tarea
def delete_task(task_id):
    if not task_id or task_id <= 0:
        return "Error: Invalid task ID"
        
    database.delete_task(task_id)
    return "Task deleted successfully."

#Inicializar la base de datos
database.create_table()
