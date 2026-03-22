from flask import Flask, render_template, redirect
import cv2
import os
import json
#from deepface import DeepFace
import asyncio
from bleak import BleakScanner

app = Flask(__name__)

# ================= LOAD USERS =================
def load_users():
    with open("users.json", "r") as f:
        return json.load(f)

# # ================= FACE =================
# def capture_face():
#     cap = cv2.VideoCapture(0)
#     ret, frame = cap.read()
#     cap.release()

#     path = "temp.jpg"
#     cv2.imwrite(path, frame)

#     return path

# def match_face(img_path):
    users = load_users()

    for user in users:
        try:
            result = DeepFace.verify(img_path, user["image"], enforce_detection=False)
            if result["verified"]:
                return user["name"]
        except:
            pass
    return None

# ================= BLUETOOTH =================
async def get_nearby_devices():
    devices = await BleakScanner.discover(timeout=3.0)
    return [d.name for d in devices if d.name]

def match_bluetooth():
    users = load_users()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    nearby = loop.run_until_complete(get_nearby_devices())

    for user in users:
        if user["bluetooth_name"] in nearby:
            return user["name"]

    return None

# ================= AUTO LOGIN =================
@app.route("/")
def auto_login():

    # # Face Login
    # img = capture_face()
    # user = match_face(img)
    # if user:
    #     return redirect("/home")

    # Bluetooth Login
    user = match_bluetooth()
    if user:
        return redirect("/home")

    return """
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="refresh" content="2">
<style>
body {
    text-align: center;
    font-family: Arial;
    background: black;
    color: lime;
}
h1 {
    margin-top: 100px;
    font-size: 40px;
}
</style>
</head>

<body>
<h1>🔍 Scanning...</h1>
<p>Face ID / Bluetooth</p>
</body>
</html>
"""

@app.route("/home")
def home():
    return "<h1>🔓 Access Granted</h1>"

# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)