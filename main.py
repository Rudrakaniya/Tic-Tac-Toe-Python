print("Hello World!!")

import tkinter as tk
r = tk.Tk()

r.title("Tic Tac Toe")

button = tk.Button(r, text='Stop', width=25, command = r.destroy, activeforeground = 'green')
button.pack()

r.mainloop()
