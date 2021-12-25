from tkinter import *

def start():
	label = Label(text="Запуск...").pack()

window = Tk() # Создаём окно
window.title("Первое desktop приложение") # Заголовок для окна
window.geometry('400x250') # Размер окна 1 - ширина 2 - высота

button = Button(window, text="Start", command=start).pack()

window.mainloop()