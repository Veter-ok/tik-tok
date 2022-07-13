from tkinter import *
import pyowm

def search():
	observation = owm.weather_manager().weather_at_place(city.get())
	weather = observation.weather
	labelWeather.configure(text="Погода - "+str(weather.detailed_status))
	labelHumidty.configure(text="Влажность - "+str(weather.humidity)+"%")
	labelTemp.configure(text="Температура - "+str(weather.temperature('celsius')['temp']))
	labelMaxTemp.configure(text="Максимальная температура - "+str(weather.temperature('celsius')['temp_max']))
	labelMinTemp.configure(text="Минимальная температура - "+str(weather.temperature('celsius')['temp_min']))

owm = pyowm.OWM("347a140363f071901c55aed50511ccf7")

window = Tk()
window.geometry('350x400')
window.title("Weather app")

labelCity = Label(window, text="city", font=("Arial", 20)).grid(column=0, row=0)
city = StringVar()
inputCity = Entry(window, textvariable=city, width=26).grid(column=1, row=0)
buttonSearch = Button(window, text="Ввод", command=search).grid(column=2, row=0)

labelWeather = Label(window, text="Погода")
labelWeather.place(x=50, y=80)

labelHumidty = Label(window, text="Влажность")
labelHumidty.place(x=50, y=100)

labelTemp = Label(window, text="Температура")
labelTemp.place(x=50, y=120)

labelMaxTemp = Label(window, text="Максимальная температура")
labelMaxTemp.place(x=50, y=140)

labelMinTemp = Label(window, text="Минимальная температура")
labelMinTemp.place(x=50, y=160)



window.mainloop()