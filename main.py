from tkinter import *
import requests


window = Tk()
window.geometry("850x500")
window.title("Weather forcast")
window.configure(background = "indigo")

lt = Label(window, text = "Temperature")
lt.place(x = 10, y = 10)

lh = Label(window, text = "Humidity")
lh.place(x = 10, y = 50)

lws = Label(window, text = "Wind Speed")
lws.place(x = 10, y = 100 )

lcc = Label(window, text = "Cloud Cover")
lcc.place (x = 10, y = 150)

lmax = Label(window, text = "Maximum: ")
lmax.place(x = 10, y = 200)

lmin = Label(window, text = "Minimum: ")
lmin.place(x = 10, y = 250)

locate = Entry(window)
locate.place(x = 10, y = 300)

def weather_api():
    api_key = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+locate.get()+'&appid=6fb4c4043b76ad4e48fe65e3a7d92120')
    req_obj = api_key.json()
    print(api_key)
    print(req_obj)
    temp = round(req_obj['main']['temp']-273,1)
    lt.config(text="temperature: "+str(temp))
    max = round(req_obj['main']['temp_max']- 273,1)
    lmax.config(text = "Maximum:" + str(max))
    min = round(req_obj['main']['temp_min']-273,1)
    lmin.config(text = "Minimum: " + str(min))
    humid = req_obj['main']['humidity']
    lh.config(text = "Humidity: " + str(humid))
    lcc.config(text ="Cloud cover is: " + req_obj['weather'][0]['description'])
    lws.config(text = "Wind Speed is: " + str(req_obj['wind']['speed']) + "km/h")


btn = Button(window, text="Button", command=weather_api)
btn.place(x = 10, y = 350)

window.mainloop()
