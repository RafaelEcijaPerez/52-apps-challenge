//Logica de temporizador Pomodoro
using System;
using System.Timers;
namespace temporizador
{
    public class Pomodoro
    {
        //Constantes
        public const int WORK_TIME = 25; //minutos
        public const int SHORT_BREAK_TIME = 5; //minutos

        //Varables
        private System.Timers.Timer timer;
        private int timeLeft; //segundos
        private bool isRunning;// indica si el temporizador esta en marcha

        public Pomodoro()
        {
            timer = new System.Timers.Timer();
        }

        //Entrada

        //Procedimiento
        //Funcion para iniciar el temporizador
        public void StartTimer(int minutes)
        {
            if (isRunning)
                return; // Si el temporizador ya esta en marcha, no hacer nada

            timeLeft = minutes * 60; // Convertir minutos a segundos
            timer = new System.Timers.Timer(1000); // Configurar el temporizador para que dispare cada segundo
            timer.Elapsed += OnTimedEvent; // Asociar el evento
            timer.Enabled = true; // Habilitar el temporizador
            isRunning = true; // Marcar como en marcha
        }
        //Funcion para cambiar de tiempo de trabajo a descanso
        private void OnTimedEvent(Object source, ElapsedEventArgs e)
        {
            if (timeLeft > 0)
            {
                timeLeft--; // Disminuir el tiempo restante
                Console.WriteLine($"Tiempo restante: {timeLeft / 60}:{timeLeft % 60:D2}"); // Mostrar tiempo restante
            }
            else
            {
                timer.Stop(); // Detener el temporizador
                isRunning = false; // Marcar como no en marcha
                Console.WriteLine("¡Tiempo terminado!"); // Notificar que el tiempo ha terminado
            }
        }

        //Salida
        public void StopTimer()
        {
            if (!isRunning)
            return; // Si el temporizador no está en marcha, no hacer nada

            timer.Stop(); // Detener el temporizador
            isRunning = false; // Marcar como no en marcha
            Console.WriteLine("Temporizador detenido."); // Notificar que el temporizador ha sido detenido
        }
    }
}