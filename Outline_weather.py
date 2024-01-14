from tkinter import *
import tkinter as tk
import requests
from PIL import Image, ImageTk
from tkinter import *

api_key = 'API KEY'
root = tk.Tk()  # create a root widget
root.title("Weather App")
root.configure(background="light cyan")

root.maxsize(500, 500)
root.geometry("500x500")  # width x height + x + y
city_var = tk.StringVar()


def convert_kelvin_to_farhrenhiet(kelvin):
    Fahrenheit = (kelvin - 273.15) * 9 / 5 + 32

    return Fahrenheit


def weather_function():
    city_name = my_entry.get()
    city_var.set("")
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']

        desc = data['weather'][0]['description']
        New_temp = round(convert_kelvin_to_farhrenhiet(temp))
        New_text(New_temp)

        print(f'Temperature: {New_temp} F')
        print(f'Description: {desc}')

    else:
        print("City Doesn't Exist")


def New_text(Temperature):
    msg = tk.Message(root, text=f"Temperature: {Temperature} F",pady = 26,bg="light cyan")
    msg.place(x=200,y=200)
    if Temperature <= 32:
        frame_image = Frame(root, borderwidth=1)
        frame_image.pack(side=TOP, fill="x")

        frame_image.picture = PhotoImage(file="images/clouds.png")
        frame_image.label = Label(frame_image, image=frame_image.picture)
        frame_image.label.pack()




my_label = tk.Label(root, text="Enter City", bg="light cyan")
my_label.place(x=100,y=70)

my_entry = tk.Entry(root)
my_entry.place(x=200, y=70)


image = PhotoImage(file=r"images/search.png")

photoimage = image.subsample(3, 3)

my_button = tk.Button(root, text="Submit",relief=RAISED,bg="light cyan",image=photoimage, command=weather_function)
my_button.place(x=320, y=69)




root.mainloop()
