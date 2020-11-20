from tkinter import *
import requests


window = Tk()
window.geometry("850x500")
window.title("Weather forcast")
window.configure(background = "indigo")

locate = Entry(window)
locate.place(x = 200, y = 10)


# The function of the weather
def weather_api():
    try:
        api_key = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+locate.get()+'&appid=6fb4c4043b76ad4e48fe65e3a7d92120')
        req_obj = api_key.json()
    except Exception as error:
        api_key = "Error..."

    # The layout of the weather
    lt = Label(window, text = "Temperature")
    lt.place(x = 10, y = 100)

    lh = Label(window, text = "Humidity")
    lh.place(x = 300, y = 100)

    lws = Label(window, text = "Wind Speed")
    lws.place(x = 10, y = 200 )

    lcc = Label(window, text = "Cloud Cover")
    lcc.place (x = 300, y = 200)

    lmax = Label(window, text = "Maximum: ")
    lmax.place(x = 10, y = 300)

    lmin = Label(window, text = "Minimum: ")
    lmin.place(x = 300, y = 300)


# Results will display when you type in the place name and then press the button
    temp = str(round(req_obj['main']['temp'] -  235,1)) + u"\u00b0" + "C"
    lt.config(text="Temperature: "+ str(temp))
    max = str(round(req_obj['main']['temp_max'] -  235,1)) + u"\u00b0" + "C"
    lmax.config(text = "Maximum:" + str(max))
    min = str(round(req_obj['main']['temp_min'] -  235,1)) + u"\u00b0" + "C"
    lmin.config(text = "Minimum: " + str(min))
    humid = req_obj['main']['humidity']
    lh.config(text = "Humidity: " + str(humid))
    lcc.config(text ="Cloud cover is: " + req_obj['weather'][0] ['description'])
    lws.config(text = "Wind Speed is: " + str(req_obj['wind']['speed']) +  "km/h")

# Weather button
btn = Button(window, text="Button", command=weather_api)
btn.place(x = 250, y = 50)

window.mainloop()
