import { useState } from "react"; // Hook para estado local en componentes funcionales
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";

// Definición del tipo Note que representa una nota con id y texto
interface Note {
  id: number;
  text: string;
}

// Componente principal de la aplicación de notas
function App() {
  // Estado que almacena el array de notas
  const [notes, setNotes] = useState<Note[]>([]);
  // Estado que almacena el texto actual del input
  const [text, setText] = useState("");

  // Función para añadir una nueva nota
  const addNote = () => {
    if (text.trim() === "") return; // No añadir si el texto está vacío o solo espacios
    const newNote: Note = { id: Date.now(), text }; // Crear nota con id único aproximado
    setNotes([...notes, newNote]); // Añadir la nueva nota al array (inmutable)
    setText(""); // Limpiar el input
  };

  // Función para eliminar una nota por su id
  const deleteNote = (id: number) => {
    setNotes(notes.filter((note) => note.id !== id)); // Filtrar la nota a eliminar
  };

  // Render del componente
  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Notas</h1>

      {/* Zona de entrada para crear notas */}
      <div style={{ marginBottom: "1rem" }}>
        <input
          type="text"
          value={text} // Input controlado: su valor viene del estado 'text'
          onChange={(e) => setText(e.target.value)} // Actualiza el estado al escribir
          placeholder="Escribe una nota"
        />
        <button onClick={addNote}>Agregar</button> {/* Botón que añade la nota */}
      </div>

      {/* Lista de notas */}
      <ul>
        {notes.map((note) => (
          // Cada nota se muestra en un <li> y usa note.id como key
          <li key={note.id}>
            {note.text}
            {/* Botón para eliminar la nota actual */}
            <button onClick={() => deleteNote(note.id)}>❌</button>
          </li>
        ))}
      </ul>
    </>
  );
}

export default App; // Export por defecto del componente
