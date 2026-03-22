import cv2
#import face_recognition
import sqlite3

name = input("Enter name: ")
bt = input("Enter bluetooth MAC: ")

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cap.release()

rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#face = face_recognition.face_encodings(rgb)mm[0]

conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute("INSERT INTO users (name, face, bluetooth) VALUES (?, ?, ?)",
          (name,  bt))

conn.commit()
conn.close()

print("User Saved ✅")