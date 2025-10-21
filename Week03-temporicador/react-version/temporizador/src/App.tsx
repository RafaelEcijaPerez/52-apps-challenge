import { useState } from 'react';
import Timer from './components/Timer';
import Controls from './components/Controls';

function App() {
  const [workTime, setWorkTime] = useState(1 * 60);
  const [breakTime, setBreakTime] = useState(5 * 60);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '2rem', padding: '2rem' }}>
      <h1>Temporizador Pomodoro</h1>
      <Timer workTime={workTime} breakTime={breakTime} />
    </div>
  );
}

export default App;
