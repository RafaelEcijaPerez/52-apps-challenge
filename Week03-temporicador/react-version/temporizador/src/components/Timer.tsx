import { useState, useEffect } from 'react';
import Controls from './Controls';

interface TimerProps {
  workTime: number;
  breakTime: number;
}

const Timer: React.FC<TimerProps> = ({ workTime, breakTime }) => {
  const [timeLeft, setTimeLeft] = useState(workTime);
  const [isWorking, setIsWorking] = useState(true);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    let timer: ReturnType<typeof setInterval> | undefined;

    if (isActive && timeLeft > 0) {
      timer = setInterval(() => setTimeLeft(prev => prev - 1), 1000);
    } else if (timeLeft === 0) {
      setIsWorking(prev => !prev);
      setTimeLeft(isWorking ? breakTime : workTime);
    }

    return () => {
      if (timer) {
        clearInterval(timer);
      }
    };
  }, [isActive, timeLeft, isWorking, workTime, breakTime]);

  const formatTime = (time: number) => {
    const minutes = Math.floor(time / 60);
    const seconds = time % 60;
    return `${minutes.toString().padStart(2,'0')}:${seconds.toString().padStart(2,'0')}`;
  };

  const handleStartPause = () => setIsActive(prev => !prev);
  const handleReset = () => {
    setIsActive(false);
    setTimeLeft(isWorking ? workTime : breakTime);
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <h2>{isWorking ? 'Trabajo' : 'Descanso'}</h2>
      <p style={{ fontSize: '3rem' }}>{formatTime(timeLeft)}</p>
      <Controls isActive={isActive} onStartPause={handleStartPause} onReset={handleReset} />
    </div>
  );
};

export default Timer;
