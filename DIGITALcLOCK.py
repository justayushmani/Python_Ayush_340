import tkinter as tk
import time
def utime():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, utime)
window=tk.Tk()
window.title("Digital Clock")
window.geometry("300x100")
label=tk.Label(window, font=("Arial", 48), bg="black", fg="white")
label.pack(fill="both", expand=1)
utime()
window.mainloop()