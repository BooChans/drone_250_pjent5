#ce programme liste les composants connectés en série à l'ordinateur (PC ou Raspberry)
import serial.tools.list_ports
print("Available serial ports:")
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port)
