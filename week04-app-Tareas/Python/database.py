#Generar la conexion con la base de datos
import sqlite3

#task
DB = "tasks.db"
#Función para conectar a la base de datos SQLite
def connect_db():
    #Crear la conexión a la base de datos SQLite
    try:
        conexion = sqlite3.connect(DB)
    except sqlite3.Error as e:
        conexion = "Error: " + str(e)
    
    return conexion

#Funcion para creear la tabla de tareas si no existe
def create_table():
    conexion = connect_db()
    cursor = conexion.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       title TEXT NOT NULL,
                       description TEXT,
                       status TEXT NOT NULL)''')
    conexion.commit()
    conexion.close()

#Funcion para insertar una nueva tarea
def insert_task(title, description, status):
    conexion = connect_db()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)",
                   (title, description, status))
    conexion.commit()
    conexion.close()

#Funcion para obtener todas las tareas
def get_all_tasks():
    conexion = connect_db()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conexion.close()
    return tasks

#Funcion para actualizar una tarea
def update_task(task_id, title, description, status):
    conexion = connect_db()
    cursor = conexion.cursor()
    cursor.execute("UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?",
                   (title, description, status, task_id))
    conexion.commit()
    conexion.close()

#Funcion para eliminar una tarea
def delete_task(task_id):
    conexion = connect_db()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conexion.commit()
    conexion.close()

