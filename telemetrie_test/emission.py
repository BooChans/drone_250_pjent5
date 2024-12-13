from pymavlink import mavutil
import time

# Configurer le port série et le baud rate pour le module SiK V3
SERIAL_PORT = 'COM3'  # Mettre à jour votre port série, COMx sur Windows et /dev/ttyUSB0 sur Linux
BAUD_RATE = 57600             # Baud par défaut

def send_status_message():
    """Send a custom status text message over the MAVLink connection."""
    # Connecter le module SiK V3.
    master = mavutil.mavlink_connection(SERIAL_PORT, baud=BAUD_RATE)

    # Definir un message à envoyer
    message = "Hello from pymavlink! This is a test message."
    
    try:
        # Envoi du message sans attendre le heartbeat du module SiK V3 auquel on veut transmettre des données
        master.mav.statustext_send(
            mavutil.mavlink.MAV_SEVERITY_INFO,  # Définit la sévérité du message, et donc le degré d'importance : Severity (INFO, WARNING, ERROR)
            message.encode('utf-8')  # Encode le message en bits, utf-8. 
        )
        print(f"Sent status message: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")
    finally:
        master.close()  # Ferme le port série
        print("Connection closed.")

if __name__ == "__main__":
    send_status_message()
