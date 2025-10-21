import React from 'react';

interface ControlsProps {
  isActive: boolean;
  onStartPause: () => void;
  onReset: () => void;
}

const Controls: React.FC<ControlsProps> = ({ isActive, onStartPause, onReset }) => (
  <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem' }}>
    <button onClick={onStartPause} style={{ padding: '10px 20px', borderRadius: '8px', cursor: 'pointer', backgroundColor: isActive ? '#f87171' : '#4ade80', color: 'white', border: 'none' }}>
      {isActive ? 'Pausar' : 'Iniciar'}
    </button>
    <button onClick={onReset} style={{ padding: '10px 20px', borderRadius: '8px', cursor: 'pointer', backgroundColor: '#60a5fa', color: 'white', border: 'none' }}>
      Reiniciar
    </button>
  </div>
);

export default Controls;
