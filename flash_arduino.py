import subprocess

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

    # Verifica se a gravação foi bem-sucedida
    if result.returncode == 0:
        print("Gravação realizada com sucesso!")
    else:
        print("Erro na gravação:")
        print(result.stderr.decode())

# Executa a função de gravação
flash_arduino()