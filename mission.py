# mission.py
import keyboard
from tello import Tello
import time

# Dictionnaire pour suivre l'état des touches
key_states = {
    "bas": 0,    # Descendre
    "haut": 0,   # Monter
    "droite": 0, # Déplacement droite
    "gauche": 0, # Déplacement gauche
    "space": 0,  # Décollage/Atterrissage
    "r": 0,      # Caméra
    "v": 0       # Enregistrement vidéo
}

class Mission:
    def __init__(self):
        self.tello_drone = Tello()
    
    @staticmethod
    def on_key_event(event):
        """Met à jour l'état des touches."""
        if event.event_type == "down":
            key_states[event.name] = 1
        elif event.event_type == "up":
            key_states[event.name] = 0
    
    def control_loop(self):
        """Boucle principale pour contrôler le drone."""
        keyboard.hook(self.on_key_event)
        
        try:
            while True:
                if key_states["space"]:
                    self.tello_drone.takeoff()
                    time.sleep(1) 

                if key_states["r"]:
                    self.tello_drone.camera()
                    time.sleep(1)

                if key_states["v"]:
                    self.tello_drone.toggle_enregistrement() 
                    time.sleep(1)

                if self.tello_drone.get_flight_status():
                    if key_states["haut"]:
                        self.tello_drone.move_up()

                    if key_states["bas"]:
                        self.tello_drone.move_down()

                    if key_states["droite"]:
                        self.tello_drone.move_right()

                    if key_states["gauche"]:
                        self.tello_drone.move_left()

                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print("Programme arrêté par l'utilisateur")

if __name__ == "__main__":
    mission = Mission()
    mission.control_loop() #    