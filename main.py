import tkinter as tk
from register import register_user
from authenticate import authenticate_user

def main():
    window = tk.Tk()
    window.title("Face Authentication System")
    window.geometry("400x300")

    title = tk.Label(window, text="Face Recognition Authentication", font=("Arial", 14))
    title.pack(pady=20)

    btn_register = tk.Button(window, text="Register", width=20, command=register_user)
    btn_register.pack(pady=10)

    btn_auth = tk.Button(window, text="Authenticate", width=20, command=authenticate_user)
    btn_auth.pack(pady=10)

    btn_exit = tk.Button(window, text="Exit", width=20, command=window.quit)
    btn_exit.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
