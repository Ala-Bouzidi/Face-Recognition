import cv2
import face_recognition
import pickle
import os
import tkinter.simpledialog as sd
import tkinter.messagebox as mb

def register_user():
    name = sd.askstring("Register", "Enter user name:")
    if not name:
        return

    cap = cv2.VideoCapture(0)

    mb.showinfo("Info", "Press 's' to capture image")

    while True:
        ret, frame = cap.read()
        cv2.imshow("Register - Press S", frame)

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

    # Save encoding
    if os.path.exists("database.pkl"):
        with open("database.pkl", "rb") as f:
            database = pickle.load(f)
    else:
        database = {}

    database[name] = encoding

    with open("database.pkl", "wb") as f:
        pickle.dump(database, f)

    mb.showinfo("Success", "User registered successfully!")
