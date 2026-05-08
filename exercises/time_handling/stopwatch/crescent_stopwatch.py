import time
import sys

def cronometro():
    print("Cronômetro iniciado! Pressione Ctrl+C para parar.")
    start_time = time.time()
    try:
        while True:
            elapsed_time = time.time() - start_time
            # Formata o tempo: horas, minutos, segundos e centésimos
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            hundredths = int((elapsed_time * 100) % 100)
            
            # \r volta o cursor para o início da linha
            sys.stdout.write(f"\rTempo decorrido: {hours:02d}:{minutes:02d}:{seconds:02d}.{hundredths:02d}")
            sys.stdout.flush()
            time.sleep(0.01) # Atualiza a cada 10ms
    except KeyboardInterrupt:
        print("\n\nCronômetro parado.")
        total_time = time.time() - start_time
        print(f"Tempo total: {total_time:.2f} segundos.")

if __name__ == "__main__":
    cronometro()
