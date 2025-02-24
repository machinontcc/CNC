import tkinter as tk
from tkinter import ttk, messagebox
import serial
import time
import subprocess

# Variável global para a conexão GRBL
GRBL = None

def enviar_comando_grbl(comando):
    """
    Envia um comando para a máquina CNC via GRBL.
    """
    global GRBL  # Referencia a variável global GRBL
    if GRBL is None or not GRBL.is_open:
        messagebox.showerror("Erro", "CNC não está conectado.")
        return

    print(f"Enviando: {comando}")
    GRBL.write(f'{comando}\n'.encode())
    GRBL.flush()
    
    while True:
        resposta = GRBL.readline().decode().strip()
        if resposta:
            print(f"Resposta: {resposta}")
        if resposta == "ok":
            break

def conectar_cnc(porta):
    """
    Conecta à máquina CNC na porta especificada.
    """
    global GRBL  # Referencia a variável global GRBL
    GRBL_BAUD_RATE = 115200

    try:
        GRBL = serial.Serial(porta, GRBL_BAUD_RATE)
        print(f"Conectado à porta {porta}")
        messagebox.showinfo("Sucesso", "CNC conectado com sucesso!")
        time.sleep(2)  # Aguarda a inicialização do GRBL
    except Exception as e:
        print(f"Erro ao conectar à porta {porta}: {e}")
        messagebox.showerror("Erro", f"Falha ao conectar: {e}")

def desconectar_cnc():
    """
    Desconecta da máquina CNC.
    """
    global GRBL  # Referencia a variável global GRBL
    if GRBL is not None and GRBL.is_open:
        GRBL.close()
        print("Desconectado da máquina CNC")
        messagebox.showinfo("Desconectado", "Desconectado da máquina CNC.")
    else:
        print("Nenhuma conexão ativa para desconectar.")
        messagebox.showwarning("Aviso", "Nenhuma conexão ativa para desconectar.")

def mover_eixo(eixo, direcao, passo, feed):
    """
    Move um eixo específico na direção desejada com o passo e feed rate fornecidos.
    """
    if direcao == 'baixo':
        passo = -passo

    comando = f'G91 G1 {eixo}{passo} F{feed}'
    enviar_comando_grbl(comando)

def iniciar_painel(arduino_port):
    """
    Inicia o painel de controle.
    """
    if GRBL is None or not GRBL.is_open:
        messagebox.showerror("Erro", "CNC não está conectado.")
        return

    print('Painel iniciado.')
    enviar_comando_grbl('G90')
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 X0 Y0 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5) 
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-8 F1000')
    enviar_comando_grbl('G1 Y43.3 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-8 F350')
    enviar_comando_grbl('G1 Y86.6 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-8 F350')
    enviar_comando_grbl('G1 Y129.9 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-8 F350')
    enviar_comando_grbl('G1 X42.367 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-8 F350')
    enviar_comando_grbl('G1 Y86.6 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y43.3 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y0 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 X84.734 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y43.3 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y86.6 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y129.9 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 X127.101 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y86.6 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y43.3 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y0 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 X169.428 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y43.3 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y86.6 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-5 F350')
    enviar_comando_grbl('G1 Y129.9 F1500')
    enviar_comando_grbl('G1 Z-1.5 F1000')
    enviar_comando_grbl('G1 Z0 F100')
    time.sleep(1.5)
    flash_arduino(arduino_port)
    enviar_comando_grbl('G1 Z-10 F1000')
    enviar_comando_grbl('G1 X0 Y0 F1500')

def definir_ponto_zero_xy():
    """
    Define o ponto zero para os eixos X e Y.
    """
    if GRBL is None or not GRBL.is_open:
        messagebox.showerror("Erro", "CNC não está conectado.")
        return

    enviar_comando_grbl('G92 X0 Y0')

def definir_ponto_zero_z():
    """
    Define o ponto zero para o eixo Z.
    """
    if GRBL is None or not GRBL.is_open:
        messagebox.showerror("Erro", "CNC não está conectado.")
        return

    enviar_comando_grbl('G92 Z0')

def flash_arduino(porta):
    # Defina os parâmetros do comando avrdude
    hex_file_path = r"C:\Users\Luciano\Documents\Arduino\fullAutoStopV2\build\MiniCore.avr.328\fullAutoStopV2.ino.hex"
    port = porta
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

    max_tentativas = 3
    tentativa = 1

    while tentativa <= max_tentativas:
        print(f"Tentativa {tentativa} de {max_tentativas}")
        
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode == 0:
            print("Gravação realizada com sucesso.")
            return True
        else:
            print(f"Erro na tentiva {tentativa}:")
            print(result.stderr.decode())
            tentativa += 1
            time.sleep(1)

    print("Erro: falha na gravação após 3 tentativas. Enviando alerta...")
    messagebox.showerror("Erro", "Gravação não realizada... Prosseguindo para próxima peça")
    return False