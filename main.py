import tkinter as tk
from tkinter import ttk
from register import register_user
from authenticate import authenticate_user

def main():
    window = tk.Tk()
    window.title("Face Authentication System")
    window.geometry("450x350")
    window.configure(bg="#f0f0f0")
    window.resizable(False, False)

    
    title = tk.Label(
        window,
        text="🔒 Face Recognition Authentication",
        font=("Arial", 16, "bold"),
        bg="#f0f0f0",
        fg="#333"
    )
    title.pack(pady=20)

    
    btn_frame = tk.Frame(window, bg="#f0f0f0")
    btn_frame.pack(pady=30)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 12), padding=8)

    btn_register = ttk.Button(btn_frame, text="Register", command=register_user)
    btn_register.grid(row=0, column=0, padx=20, pady=10)

    btn_auth = ttk.Button(btn_frame, text="Authenticate", command=authenticate_user)
    btn_auth.grid(row=1, column=0, padx=20, pady=10)

    btn_exit = ttk.Button(btn_frame, text="Exit", command=window.quit)
    btn_exit.grid(row=2, column=0, padx=20, pady=10)

    
    status_label = tk.Label(window, text="Welcome! Please choose an option.", 
                            font=("Arial", 10), bg="#f0f0f0", fg="gray")
    status_label.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
