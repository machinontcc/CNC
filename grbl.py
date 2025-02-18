import serial
import time
import keyboard
import subprocess

GRBL_PORT = 'COM4' # porta serial do grbl (maquina cnc)
GRBL_BAUD_RATE = 115200 # baud rate da maquina

# Realizar conexão com a máquina
GRBL = serial.Serial(GRBL_PORT, GRBL_BAUD_RATE)
time.sleep(2) # aguarda a conexão ser estabelecida

# função para enviar comandos ao GRBL (G-CODE)
def enviar_comando_grbl(comando):
    print(f'Enviando: {comando}')
    GRBL.write(f'{comando}\n'.encode())
    GRBL.flush()
    time.sleep(1)

# definir ponto 0 (origem) dos eixos X e Y
def definir_ponto_zero_xy():
    enviar_comando_grbl('G92 X0 Y0')

# definir ponto 0 (origem) dos eixos Z
def definir_ponto_zero_z():
    enviar_comando_grbl('G92 Z0')


def flash_arduino():
    # Defina os parâmetros do comando avrdude
    hex_file_path = r"C:\Users\Luciano\Documents\Arduino\fullAutoStopV2\build\MiniCore.avr.328\fullAutoStopV2.ino.hex"
    port = "COM7"
    programmer = "arduino_as_isp"
    mcu = "m328pb"

    # Comando avrdude
    command = [
        "avrdude",
        "-c", programmer,
        "-p", mcu,
        "-P", port,
        "-v",
        "-e",
        "-U", f"flash:w:{hex_file_path}:a",
        "-U", "lfuse:w:0xE2:m",
        "-U", "hfuse:w:0xDF:m",
        "-U", "efuse:w:0xF4:m",
        "-U", "lock:w:0xC0:m"
    ]   

    # Executa o comando
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print("Comando executado")
    # Verifica se a gravação foi bem-sucedida
    if result.returncode == 0:
        print("Gravação realizada com sucesso!")
    else:
        print("Erro na gravação:")
        print(result.stderr.decode())


def controle_teclado():
    while True:
        if keyboard.is_pressed('up'):
            enviar_comando_grbl('G91 G1 Y0.25 F1500')
        elif keyboard.is_pressed('down'):
            enviar_comando_grbl('G91 G1 Y-0.25 F1500')
        elif keyboard.is_pressed('left'):
            enviar_comando_grbl('G91 G1 X0.5 F1500')
        elif keyboard.is_pressed('right'):
            enviar_comando_grbl('G91 G1 X-0.5 F1500')
        elif keyboard.is_pressed('+'):
            enviar_comando_grbl('G91 G1 Z0.5 F100')
        elif keyboard.is_pressed('-'):
            enviar_comando_grbl('G91 G1 Z-1 F100')
        elif keyboard.is_pressed('p'):
            enviar_comando_grbl('G91 G1 Y43.3 F1500')
        elif keyboard.is_pressed('g'):
            flash_arduino()
        elif keyboard.is_pressed('z'):
            definir_ponto_zero_xy()
            definir_ponto_zero_z()
        elif keyboard.is_pressed('s'):
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 X0 Y0 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F1000')
            enviar_comando_grbl('G1 Y43.3 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y86.6 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y129.9 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 X42.367 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y86.6 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y43.3 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y0 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 X84.734 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y43.3 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y86.6 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y129.9 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 X127.101 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y86.6 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y43.3 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y0 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 X169.428 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y43.3 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y86.6 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-5 F350')
            enviar_comando_grbl('G1 Y129.9 F1500')
            enviar_comando_grbl('G1 Z-1.5 F1000')
            enviar_comando_grbl('G1 Z0 F100')
            enviar_comando_grbl('G1 Z-10 F1000')
            enviar_comando_grbl('G1 X0 Y0 F1500')
        elif keyboard.is_pressed('esc'):
            print("Saindo...")
            break
        time.sleep(0.1)

if __name__ == '__main__':
    controle_teclado()
    GRBL.close()