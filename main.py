from tkinter import *
import requests

window = Tk()
window.geometry("850x500")
window.title("Weather forcast")
window.configure(background = "indigo")


# The layout of the weather

# The Temperature Label
lt = Label(window, text = "Temperature: ", bg = "orange", fg = "black", font =("bold", 20))
lt.place(x = 10, y = 100)

# The Humidity Label
lh = Label(window, text = "Humidity: ", bg = "pink", fg = "black", font = ("bold", 20))
lh.place(x = 400, y = 100)

# The Wind Speed Label
lws = Label(window, text = "Wind Speed: ", bg = "green", fg = "black", font = ("bold", 20))
lws.place(x = 10, y = 200 )

# The Cloud Cover Label
lcc = Label(window, text = "Cloud Cover: ", bg = "light grey", fg = "black", font = ("bold", 20))
lcc.place (x = 400, y = 200)

# The Maximum Label
lmax = Label(window, text = "Maximum: ", bg = "red", fg = "black", font = ("bold", 20))
lmax.place(x = 10, y = 300)

# The Minimum Label
lmin = Label(window, text = "Minimum: ", bg = "blue", fg = "black", font = ("bold", 20))
lmin.place(x = 400, y = 300)

# The Location Entry
locate = Entry(window)
locate.place(x = 200, y = 10)


# The function of the weather
def weather_api():
    try:
        api_key = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+locate.get()+'&appid=6fb4c4043b76ad4e48fe65e3a7d92120')
        req_obj = api_key.json()
    except Exception as error:
        api_key = "Error..."
        print(api_key)

# Results will display when you type in the place name and then press the button
    temp = str(round(req_obj['main']['temp'] -  235,1)) + u"\u2103"
    lt.config(text="Temperature: "+ str(temp))
    max = str(round(req_obj['main']['temp_max'] -  235,1)) + u"\u2103"
    lmax.config(text = "Maximum:" + str(max))
    min = str(round(req_obj['main']['temp_min'] -  235,1)) + u"\u2103"
    lmin.config(text = "Minimum: " + str(min))
    humid = req_obj['main']['humidity']
    lh.config(text = "Humidity: " + str(humid))
    lcc.config(text ="Cloud cover is: " + req_obj['weather'][0] ['description'])
    lws.config(text = "Wind Speed is: " + str(req_obj['wind']['speed']) +  "km/h")

# Weather button
btn = Button(window, text="Check Weather", command=weather_api)
btn.place(x = 250, y = 50)

window.mainloop()
