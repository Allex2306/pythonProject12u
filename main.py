import tkinter as tk


win = tk.Tk()
canvas =tk.Canvas(win,bg="black",width=700,height=700)
canvas.create_oval((300,300),(500,500),fill='green')
canvas.create_line((0,0),(100,200),(300,300),(200,100),(0,0),fill="blue")
canvas.pack()
