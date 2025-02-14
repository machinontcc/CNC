import serial
import time
import keyboard  # Biblioteca para capturar eventos do teclado

# Configuração da porta serial (ajuste conforme necessário)
PORTA = "COM5"  # Ajuste para a porta correta
BAUDRATE = 115200
PASSO = 10  # Distância de deslocamento por comando nos eixos X e Y
PASSO_Z = 1  # Distância de deslocamento por comando no eixo Z


def conectar_grbl():
    """Estabelece conexão com o GRBL"""
    try:
        ser = serial.Serial(PORTA, BAUDRATE, timeout=1)
        time.sleep(2)  # Aguarda inicialização
        ser.flushInput()
        print("Conectado ao GRBL!")
        return ser
    except Exception as e:
        print(f"Erro ao conectar: {e}")
        return None


def enviar_comando(ser, comando):
    """Envia comando G-code para a CNC"""
    if ser:
        ser.write((comando + "\n").encode())
        while True:
            resposta = ser.readline().decode().strip()
            if resposta:
                print(f"GRBL: {resposta}")
            if resposta == "ok":
                break  # Sai do loop quando o GRBL confirma que o comando foi processado


def controlar_cnc(ser):
    """Controla os eixos X, Y e Z com o teclado"""
    print("Use as setas para mover os eixos X e Y, '+' para subir Z e '-' para descer Z. Pressione 'ESC' para sair.")
    while True:
        if keyboard.is_pressed("up"):
            enviar_comando(ser, f"G91 G0 Y{PASSO}")  # Move Y para frente
            time.sleep(0.2)
        elif keyboard.is_pressed("down"):
            enviar_comando(ser, f"G91 G0 Y-{PASSO}")  # Move Y para trás
            time.sleep(0.2)
        elif keyboard.is_pressed("left"):
            enviar_comando(ser, f"G91 G1 X-{PASSO} F200")  # Move X para a esquerda
            time.sleep(0.2)
        elif keyboard.is_pressed("right"):
            enviar_comando(ser, f"G91 G1 X{PASSO} F200")  # Move X para a direita
            time.sleep(0.2)
        elif keyboard.is_pressed("+"):
            enviar_comando(ser, f"G91 G0 Z{PASSO_Z}")  # Move Z para cima
            time.sleep(0.2)
        elif keyboard.is_pressed("-"):
            enviar_comando(ser, f"G91 G0 Z-{PASSO_Z}")  # Move Z para baixo
            time.sleep(0.2)
        elif keyboard.is_pressed("esc"):
            print("Saindo do controle de teclado.")
            break


def desligar_grbl(ser):
    """Fecha a conexão com o GRBL"""
    if ser:
        ser.close()
        print("Conexão fechada")


if __name__ == "__main__":
    ser = conectar_grbl()
    if ser:
        try:
            controlar_cnc(ser)
        except KeyboardInterrupt:
            print("\nEncerrando...")
        finally:
            desligar_grbl(ser)
