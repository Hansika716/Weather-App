import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import requests

HEIGHT = 700
WIDTH = 800

#key  - de87a100214ed3ad1a548d3c6e931005
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def get_weather(city):
    weather_key = 'de87a100214ed3ad1a548d3c6e931005'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)
    icon_name = weather['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'City: %s \nConditions: %s \nTemperature(\'F): %s' %(name,desc,temp)
    except:
        final_str = 'there was a problem'
    return final_str

root = tk.Tk()

background_image = tk.PhotoImage(file = 'landscape.png')
background_label = tk.Label(root, image = background_image)
background_label.image = background_image
background_label.pack()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()
                           #to set up border of 5
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.15 ,rely = 0.1, relwidth=0.7 ,relheight=0.1)
                          #setting up font size
entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth = 0.65, relheight=1)
 #we use lambda function here as it is redefined everytime we click it, we get the current state of entry using it
button = tk.Button(frame, font=('Courier', 12), text='Get weather', command=lambda: get_weather(entry.get()))
         #keeping a 0.05 gap btw the 2 , entry and button
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=5)
lower_frame.place(relx=0.15, rely=0.25, relwidth=0.7, relheight =0.5)

label = tk.Label(lower_frame , bg='white', font=('Courier', 18), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
