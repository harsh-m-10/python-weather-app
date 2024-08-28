from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

#weather getting

def getWeather():
    try:
        city=textfield.get()
        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj1=TimezoneFinder()
        result=obj1.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        localTime=datetime.now(home)
        currentTime=localTime.strftime("%I:%M %p")
        clock.config(text=currentTime)
        name.config(text="Current Time")

        #weather
        api_key='6c8899eaeeb86a57f5e969a874cc8733'
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6c8899eaeeb86a57f5e969a874cc8733"
        jsonData=requests.get(api).json()
        crntweather=jsonData['weather'][0]['main']
        conditions=jsonData['weather'][0]['description']
        temp=int(jsonData['main']['temp']-273.15)
        pressure=jsonData['main']['pressure']
        wind=jsonData['wind']['speed']
        humidity=jsonData['main']['humidity']
        #configuration
        t.config(text=(temp,"°C"))
        c.config(text=(crntweather,"|","FEELS","LIKE",temp,"°C"))
        w.config(text=(wind,"mph"))
        h.config(text=(humidity,"%"))
        c1.config(text=conditions)
        p.config(text=(pressure,"mmHg"))

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!!")

#Search Box
Search_image=PhotoImage(file="searchbox.png") 
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="searchicon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo
logoImage=PhotoImage(file="appicon.png")
logo=Label(image=logoImage)
logo.place(x=150,y=100)

#Bottom box
frameImage=PhotoImage(file="searchbox1.png")
frame_myimage=Label(image=frameImage)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

# 5dayweather
# frame1=PhotoImage(file="5day (1).png")
# frame5day=Label(image=frame1)
# frame5day.pack(padx=5,pady=5,side=RIGHT)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)

#label
label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=150,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=280,y=400)

label3=Label(root,text="CONDITIONS",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=450,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=630,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=130,y=430)

h=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=300,y=430)

c1=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
c1.place(x=470,y=430)

p=Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=640,y=430)

root.mainloop()