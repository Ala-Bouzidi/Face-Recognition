import cv2
import face_recognition
import pickle
import tkinter.messagebox as mb
import os
import numpy as np

def authenticate_user():

    if not os.path.exists("database.pkl"):
        mb.showerror("Error", "No registered users!")
        return

    with open("database.pkl", "rb") as f:
        database = pickle.load(f)

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    mb.showinfo("Info", "Press 's' to authenticate")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Authenticate - Press S", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    cap.release()
    cv2.destroyAllWindows()

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_encodings(rgb_frame)

    if len(faces) == 0:
        mb.showerror("Error", "No face detected!")
        return

    encoding = faces[0]

    for name, saved_encoding in database.items():
        distance = np.linalg.norm(saved_encoding - encoding)

        if distance < 0.5:
            mb.showinfo("Access Granted", f"Welcome {name}!")
            return

    mb.showerror("Access Denied", "Unknown user!")
