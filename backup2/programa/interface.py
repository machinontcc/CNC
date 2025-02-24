import tkinter as tk
from tkinter import ttk
import serial.tools.list_ports

from comandos import enviar_comando_grbl, conectar_cnc, desconectar_cnc, mover_eixo, iniciar_painel, definir_ponto_zero_xy, definir_ponto_zero_z

# Função para listar as portas seriais disponíveis
def listar_portas_seriais():
    portas = serial.tools.list_ports.comports()
    return [porta.device for porta in portas]

# Função para atualizar as portas seriais nos ComboBox
def atualizar_portas():
    portas = listar_portas_seriais()
    combo_cnc['values'] = portas
    combo_arduino['values'] = portas
    if portas:
        combo_cnc.current(0)  # Seleciona a primeira porta por padrão
        combo_arduino.current(0)  # Seleciona a primeira porta por padrão

# Função para enviar comandos G-code diretamente
def enviar_comando_direto():
    comando = entry_comando.get()
    if comando:
        enviar_comando_grbl(comando)
        entry_comando.delete(0, tk.END)  # Limpa o campo de entrada

# Criando a janela principal
root = tk.Tk()
root.title("Controle de Máquina CNC e Arduino")

# Frame para seleção de portas seriais
frame_portas = ttk.LabelFrame(root, text="Portas Seriais")
frame_portas.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# ComboBox para selecionar a porta da Máquina CNC
label_cnc = ttk.Label(frame_portas, text="Máquina CNC:")
label_cnc.grid(row=0, column=0, padx=5, pady=5)
combo_cnc = ttk.Combobox(frame_portas, state="readonly")
combo_cnc.grid(row=0, column=1, padx=5, pady=5)

# Botão para conectar a Máquina CNC
botao_conectar_cnc = ttk.Button(frame_portas, text="Conectar CNC", command=lambda: conectar_cnc(combo_cnc.get()))
botao_conectar_cnc.grid(row=0, column=2, padx=5, pady=5)

# Botão para desconectar a Máquina CNC
botao_desconectar_cnc = ttk.Button(frame_portas, text="Desconectar CNC", command=desconectar_cnc)
botao_desconectar_cnc.grid(row=0, column=3, padx=5, pady=5)

# ComboBox para selecionar a porta do Arduino
label_arduino = ttk.Label(frame_portas, text="Arduino:")
label_arduino.grid(row=1, column=0, padx=5, pady=5)
combo_arduino = ttk.Combobox(frame_portas, state="readonly")
combo_arduino.grid(row=1, column=1, padx=5, pady=5)

# Botão para atualizar as portas seriais
botao_atualizar = ttk.Button(frame_portas, text="Atualizar Portas", command=atualizar_portas)
botao_atualizar.grid(row=2, column=0, columnspan=4, pady=5)

# Frame para controle dos eixos
frame_eixos = ttk.LabelFrame(root, text="Controle de Eixos")
frame_eixos.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Função para criar botões de seta para cada eixo
def criar_controle_eixo(frame, eixo, coluna):
    # Label do eixo
    label_eixo = ttk.Label(frame, text=f"Eixo {eixo}:")
    label_eixo.grid(row=0, column=coluna * 2, padx=5, pady=5)

    # Botão para mover para cima
    botao_cima = ttk.Button(frame, text="↑", command=lambda: mover_eixo(eixo, "cima", float(combo_passo.get()), float(combo_feed_rate.get())))
    botao_cima.grid(row=1, column=coluna * 2, padx=5, pady=5)

    # Botão para mover para baixo
    botao_baixo = ttk.Button(frame, text="↓", command=lambda: mover_eixo(eixo, "baixo", float(combo_passo.get()), float(combo_feed_rate.get())))
    botao_baixo.grid(row=2, column=coluna * 2, padx=5, pady=5)

# Criando controles para os eixos X, Y e Z (lado a lado)
criar_controle_eixo(frame_eixos, "X", 0)
criar_controle_eixo(frame_eixos, "Y", 1)
criar_controle_eixo(frame_eixos, "Z", 2)

# Botões adicionais ao lado dos eixos
botao_iniciar_painel = ttk.Button(frame_eixos, text="Iniciar Painel", command=lambda: iniciar_painel(combo_arduino.get()))
botao_iniciar_painel.grid(row=0, column=6, padx=10, pady=5)

botao_ponto_zero_xy = ttk.Button(frame_eixos, text="Definir Ponto Zero X e Y", command=definir_ponto_zero_xy)
botao_ponto_zero_xy.grid(row=1, column=6, padx=10, pady=5)

botao_ponto_zero_z = ttk.Button(frame_eixos, text="Definir Ponto Zero Z", command=definir_ponto_zero_z)
botao_ponto_zero_z.grid(row=2, column=6, padx=10, pady=5)

# Frame para configuração de passo e feed rate
frame_config = ttk.LabelFrame(root, text="Configurações")
frame_config.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# ComboBox para definir o passo (editável)
label_passo = ttk.Label(frame_config, text="Passo:")
label_passo.grid(row=0, column=0, padx=5, pady=5)
combo_passo = ttk.Combobox(frame_config, values=["0.1", "0.2", "0.5", "1.0", "2.0", "5.0"], state="normal")
combo_passo.grid(row=0, column=1, padx=5, pady=5)
combo_passo.set("0.1")  # Define o valor padrão

# ComboBox para definir o feed rate (editável)
label_feed_rate = ttk.Label(frame_config, text="Feed Rate:")
label_feed_rate.grid(row=1, column=0, padx=5, pady=5)
combo_feed_rate = ttk.Combobox(frame_config, values=["100", "200", "300", "400", "500", "1000"], state="normal")
combo_feed_rate.grid(row=1, column=1, padx=5, pady=5)
combo_feed_rate.set("100")  # Define o valor padrão

# Frame para enviar comandos diretamente
frame_comandos = ttk.LabelFrame(root, text="Enviar Comandos G-code")
frame_comandos.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

# Campo de entrada para comandos G-code
label_comando = ttk.Label(frame_comandos, text="Comando:")
label_comando.grid(row=0, column=0, padx=5, pady=5)
entry_comando = ttk.Entry(frame_comandos, width=30)
entry_comando.grid(row=0, column=1, padx=5, pady=5)

# Botão para enviar comando
botao_enviar_comando = ttk.Button(frame_comandos, text="Enviar", command=enviar_comando_direto)
botao_enviar_comando.grid(row=0, column=2, padx=5, pady=5)

# Atualizar as portas seriais ao iniciar
atualizar_portas()

# Iniciar a interface
root.mainloop()