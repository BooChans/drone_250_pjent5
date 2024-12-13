import serial
from pymavlink import mavutil

# Configurer le port série et le baud rate pour le module SiK V3
serial_port = '/dev/ttyUSB0'  # Mettre à jour votre port série, COMx sur Windows et /dev/ttyUSB0 sur Linux
BAUD_RATE = 57600             # Baud par défaut

# ouvrir le port série avec pySerial
try:
    # ouvrir le port série Serial
    ser = serial.Serial(serial_port, baud_rate, timeout=1)
    print(f"Serial port {serial_port} opened successfully.")
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit(1)

# Créer la connection MAVLink en utilisant la dénomination string du port série (pas l'objet Serial en lui même)
try:
    mav = mavutil.mavlink_connection(serial_port, baud=baud_rate)
    print("MAVLink connection established.")
except Exception as e:
    print(f"Error creating MAVLink connection: {e}")
    exit(1)

# Début de la reception des messages
print("Receiving MAVLink messages...")

try:
    while True:
        # Bloque jusqu'à la réception du message
        msg = mav.recv_match(blocking=True)
        
        # Si le message est reçu on l'affiche
        if msg:
            print(f"Received message: {msg}")
            print(f"Message type: {msg.get_type()}")

            # On peut accéder à des champs particuliers du message
            if msg.get_type() == 'HEARTBEAT':
                print(f"Heartbeat received: {msg}")
            
            elif msg.get_type() == 'GPS_RAW_INT':
                print(f"GPS Data: {msg.lat}, {msg.lon}, {msg.alt}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Fermer la connection série. 
    ser.close()
    print("Serial connection closed.")

