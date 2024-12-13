import time
import os
from picamera import PiCamera



def capture_image(camera, output_dir):
    """Captures an image using the camera."""
    filename = os.path.join(output_dir, f"image_{int(time.time())}.jpg")
    camera.capture(filename)
    print(f"Image saved to {filename}")

def record_video(camera, output_dir, duration=10):
    """Records a video using the camera."""
    filename = os.path.join(output_dir, f"video_{int(time.time())}.h264")
    camera.start_recording(filename)
    print(f"Recording started. Video will be saved to {filename}")
    time.sleep(duration)
    camera.stop_recording()
    print("Recording stopped.")

def main():
    # Directory to save images and videos
    output_dir = "/home/pi/camera_outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Initialize the camera
    camera = PiCamera()

    try:
        while True:
            print("\nRaspberry Pi Camera Control")
            print("1. Capture Image")
            print("2. Record Video")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                capture_image(camera, output_dir)
            elif choice == "2":
                duration = input("Enter recording duration in seconds (default 10): ")
                duration = int(duration) if duration.isdigit() else 10
                record_video(camera, output_dir, duration)
            elif choice == "3":
                print("Exiting...")
                break
            else:
                print("Invalid choice! Please try again.")
    finally:
        camera.close()
        print("Camera closed.")

if __name__ == "__main__":
    main()
