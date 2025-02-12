# pip install pyserial
import serial
import time

# configurando porta serial (ajustar)
PORTA = "COM7" # ajuste 
BAUDRATE = 115200

def conectar_grbl():
       # Estabelece conexão com a máquina
       try:
              ser = serial.Serial(PORTA, BAUDRATE, timeout = 1)
              time.sleep(2) # aguarda inicialização
              ser.flushInput()
              print("Conectado ao GRBL!")
              return ser
       except Exception as e:
              print(f"Erro ao conectar: {e}")
              return None

def enviar_comando(ser, comando):
       # envia comando g-code para a cnc
       if ser:
              ser.write((comando + "\n").encode())
              resposta = ser.readline().decode().strip()
              print(f"GRBL: {resposta}")

def desligar_grbl(ser):
       # fecha conexao
       if ser:
              ser.close()
              print("Conexão fechada")


# exemplo de uso
if __name__ == "__main__":
       ser = conectar_grbl()

       if ser:
              enviar_comando(ser, "$$")
              desligar_grbl(ser)