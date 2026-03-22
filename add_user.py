import cv2
import json

name = input("Enter name: ")
bt_name = input("Enter Bluetooth Device Name: ")

# capture face
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

img_path = f"C:\\Users\\Molham\\OneDrive\\Desktop\\HCI\\{name}.jpg"
cv2.imwrite(img_path, frame)

# load json
with open("users.json", "r") as f:
    users = json.load(f)

# add user
users.append({
    "name": name,
    "image": img_path,
    "bluetooth_name": bt_name
})

# save
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

print("User added ✅")