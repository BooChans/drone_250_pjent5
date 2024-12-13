#import des librairies
import time
import datetime
import os

#librairies pour la caméra
from picamera import PiCamera
from pymavlink import mavutil

#librairie pour le port série
import serial
from pymavlink import mavutil

def capture_image(camera, output_dir, date):
    """Captures an image using the camera."""
    filename = os.path.join(output_dir, f"image_{date}.jpg")
    camera.capture(filename)
    print(f"Image saved to {filename}")


serial_port = '/dev/ttyUSB0'  # exemple Linus /dev/ttyUSB0, sur Windows, utiliser le port "COMx"
baud_rate = 57600  # Taux Baud pour la SiK V3

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

#  Début de la reception des messages
print("Receiving MAVLink messages...")

#initialisation du dossier de sauvegarde
output_dir = "/home/pi/camera_outputs"
os.makedirs(output_dir, exist_ok=True)
camera = PiCamera()

try:
    while True:
        # Bloque jusqu'à la réception du message
        msg = mav.recv_match(blocking=True)
        
        # Si le message est reçu on l'affiche
        if msg:
            print(f"Received message: {msg}")
            print(f"Message type: {msg.get_type()}")
            date = datetime.datetime.now()
            #réaliser la capture photo
            try: 
                capture_image(camera, output_dir, date)
            except Exception as e:
                print(f"Camera couldn't capture the scene")

            # On peut accéder à des champs particuliers du message
            if msg.get_type() == 'HEARTBEAT':
                print(f"Heartbeat received: {msg}")
            
            
            elif msg.get_type() == 'GPS_RAW_INT':
                # On écrit la ligne avec les données GPS
                new_line = f"lattitude : {msg.lat}, longitude : {msg.lon}, altitude : {msg.alt}"

                # On spécifie le nom du fichier dans lequel on veut écrire les coordonnées GPS
                file_name = "GPS_coordinates.txt"

                # on ajoute en bout de ligne du document les nouvelles coordonnées 
                with open(file_name, 'a') as file:
                    file.write("\n" + new_line)  # 
                print(f"GPS Data: {msg.lat}, {msg.lon}, {msg.alt}")

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Close the serial connection (if you need it for other purposes)
    ser.close()
    print("Serial connection closed.")





