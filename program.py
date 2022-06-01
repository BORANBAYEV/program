from tkinter import *

def click_btn():
    print("Всё работает хорошо")

root = Tk()
root.title("Заголовок окна программы")
root.geometry("400x300+300+250")
btn = Button(text="Это кнопка",
             command=click_btn,
             background="#555",
             foreground="#ccc",
             padx="50",
             pady="25",
             font="16"
             )

btn.pack()

root.mainloop()
