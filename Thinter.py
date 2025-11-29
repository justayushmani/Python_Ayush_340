import tkinter as tk
window=tk.Tk()#create window
window.title("My First App")#set title
window.geometry("400x300")#set size
label=tk.Label(window,text="Hello, World!")#create label
label.pack()#show label
window.mainloop()#run window