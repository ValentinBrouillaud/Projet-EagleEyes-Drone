from flask import Flask, render_template, jsonify
from datetime import datetime
import json
from collections import deque
from tello import Tello

app = Flask(__name__)


actions = {
    "last_action": "Initialisation...",
    "flight_status": False,
    "camera_status": False,
    "recording_status": False,
    "action_history": deque(maxlen=20)  
}


actions["action_history"].append("Initialisation du système...")


class TelloWithHistory(Tello):
    def _update_action(self, action):
        timestamp = datetime.now().strftime("%H:%M:%S")
        action_with_time = f"[{timestamp}] {action}"
        self.last_action = action
        self.actions["last_action"] = action
        self.actions["action_history"].appendleft(action_with_time)


tello_drone = TelloWithHistory(actions)

@app.route("/")
def index():
    return render_template('index.html', time=datetime.now())

@app.route("/drone/status")
def get_drone_status():
    return jsonify({
        'last_action': actions['last_action'],
        'flight_status': tello_drone.en_vol,
        'camera_status': tello_drone.camera_etat,
        'recording_status': tello_drone.est_en_enregistrement,
        'action_history': list(actions['action_history'])  
    })


@app.route("/drone/takeoff")
def drone_takeoff():
    tello_drone.takeoff()
    return jsonify({'status': 'success', 'action': actions['last_action']})

@app.route("/drone/camera")
def toggle_camera():
    tello_drone.camera()
    return jsonify({'status': 'success', 'action': actions['last_action']})

@app.route("/drone/record")
def toggle_recording():
    tello_drone.toggle_enregistrement()
    return jsonify({'status': 'success', 'action': actions['last_action']})

@app.route("/drone/move/<direction>")
def move_drone(direction):
    if tello_drone.en_vol :
        if direction == "up":
            tello_drone.move_up()
        elif direction == "down":
            tello_drone.move_down()
        elif direction == "left":
            tello_drone.move_left()
        elif direction == "right":
            tello_drone.move_right()
        return jsonify({'status': 'success', 'action': actions['last_action']})

if __name__ == "__main__":
    app.run(debug=True)