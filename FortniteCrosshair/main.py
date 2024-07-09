import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from PIL import Image, ImageTk
import keyboard


def on_press():
    root.withdraw()


    

    win = tk.Tk()
    win.geometry("500x500")
    win.overrideredirect(True) 

    def choose_color():
        color_code = colorchooser.askcolor(title ="Choose color")
        print(color_code)
        root["bg"] = color_code[1]
        messagebox.showinfo("Успешно!", "Цвет выбран!")


    btn_color = ttk.Button(master=win, text="Изменить цвет", command=choose_color)
    btn_color.place(x=250, y=100, anchor="center")


    def close():
        win.destroy()
        root.deiconify()

    

    btn = ttk.Button(master=win, text="Закрыть и сохранить", command=close)
    btn.place(x=250, y=200, anchor="center")

    def exit():
        win.destroy()
        root.destroy()

    btn_close = ttk.Button(master=win, text="Нажмите, чтобы закрыть программу", command=exit)
    btn_close.place(x=250, y=300, anchor="center")

    win.mainloop()
    

keyboard.add_hotkey("F2", on_press)


root = tk.Tk()
root.overrideredirect(True)
window_width = 15
window_height = 15
root.geometry(f"{window_width}x{window_height}")

root["bg"] = "red"

root.attributes("-topmost",True)


root.attributes("-disabled", True)
root.attributes("-transparentcolor", "white")



# Получить размеры экрана
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Вычислить координаты x и y для размещения окна в центре экрана
center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

root.geometry(f'+{center_x}+{center_y}')


root.mainloop()

