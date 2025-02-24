import serial
import time
import sys
import subprocess  # Added to invoke external programs
from datetime import datetime
import winsound


class GRBLController:
    def __init__(self, port, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_conn = None

    def connect(self):
        """Establish connection to the GRBL controller and set absolute positioning."""
        try:
            self.serial_conn = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)  # Wait for GRBL to initialize
            self.serial_conn.flushInput()  # Clear input buffer
            print("Connected to GRBL.")

            # Set absolute positioning mode
            self.send_command("G90")
            self.send_command("G10 L20 P1 X0 Y0 Z0")  # Set machine origin to (0,0,0)
            print("GRBL set to absolute positioning (G90).")

        except serial.SerialException as e:
            print(f"Error connecting to GRBL: {e}")
            sys.exit(1)  # Exit script if connection fails

    def disconnect(self):
        """Close the serial connection."""
        if self.serial_conn:
            self.serial_conn.close()
            print("Disconnected from GRBL.")
        sys.exit(0)  # Clean exit

    def send_command(self, command):
        """Send a parametric G-code command."""
        if self.serial_conn:
            self.serial_conn.write((command + "\n").encode())
            time.sleep(0.1)  # Small delay for stability
            response = self.serial_conn.readline().decode().strip()
        else:
            print("Error: Not connected to GRBL.")

    def invoke_avrdude(self):
        """Invoke avrdude with specific parameters and retry up to 3 times if it fails."""
        global x, y
        try:
            # Define avrdude command with parameters
            command = "avrdude -c arduino_as_isp -p atmega328pb -P COM7 -e -U flash:w:fullAutoStopV2.ino.hex:a -U lfuse:w:0xE2:m -U hfuse:w:0xDF:m -U efuse:w:0xF4:m -U lock:w:0xC0:m"

            for attempt in range(5):  # Retry up to 5 times
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                success = True  # Track if avrdude completes successfully

                stderr_output = process.stderr.read()  # Read stderr output fully

                if "Error" in stderr_output:
                    time.sleep(2)
                    success = False

                process.wait()  # Ensure process completes before moving on

                if success:
                    print(f"✅ Gravação bem sucedida! C{xpos + 1} L{ypos + 1}")
                    winsound.Beep(3000,200)
                    break  # Stop retrying if success

            if not success:
                print(f"❌ Gravação falhou. C{xpos + 1} L{ypos + 1}")
                winsound.Beep(500,1000)

        except FileNotFoundError:
            print("\n[Error] avrdude not found! Ensure it is installed and in the system PATH.")

        except Exception as e:
            print(f"\n[Error] Failed to execute avrdude: {e}")


if __name__ == "__main__":
    global x, y, ypos, xpos
    port = "COM4"  # Update to your CNC's actual port
    grbl = GRBLController(port)
    grbl.connect()
    
    while True:
        hora_inicio = datetime.now()
        print("Data e hora inicio:", hora_inicio.strftime("%d/%m/%Y %H:%M:%S"))
        x, y = 0, 0  # Start position
        grbl.send_command("G1 Z10 F500")
        time.sleep(1)

        for xpos in range(5):
            grbl.send_command(f"G1 X{x} Y{y} F2000")
            time.sleep(1)  # Small pause
            for ypos in range(4):
                #print(f"ypos {ypos}")
                grbl.send_command(f"G1 X{x} Y{y} F2000")  # Move XY
                #print(f"G1 X{x} Y{y} F1500")
                grbl.send_command(f"G1 Z0 F1000")  # Lower Z
                time.sleep(2)
                grbl.invoke_avrdude()  # Instead of waiting, invoke avrdude           
                grbl.send_command(f"G1 Z7 F1500")  # Raise Z
                if xpos % 2 == 0 and ypos < 3:                   
                    y += 43.3  # Increment Y positions
                if xpos % 2 != 0 and ypos < 3:
                    y -= 43.3
                if y < 0:
                    y = 0
            
            x += 42.367  # Increment X position         
        
        print("\n➡️ Moving tool to safe position before waiting... ")
        grbl.send_command("G1 Z25 F1500")
        time.sleep(2)
        grbl.send_command("G1 X240 F2000")
        time.sleep(2)
        grbl.send_command("G1 Y140 F2000")
        time.sleep(2)

        hora_final = datetime.now()
        print("Data e hora final:", hora_final.strftime("%d/%m/%Y %H:%M:%S"))

        diferenca = (hora_final - hora_inicio).total_seconds()
        print(f"A duração do programa é de {diferenca} segundos. | {diferenca / 60} minutos")

        winsound.Beep(900,2000)
        input("\n✅ Press ENTER to continue to the next repeat..")

        print("\n🔄 Retornando ferramenta para a origem...")
        grbl.send_command("G1 X0 Y0 F2000")
        time.sleep(10)
