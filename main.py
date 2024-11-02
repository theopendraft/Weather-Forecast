from tkinter import *
from configparser import ConfigParser    #to read api
import requests
from tkinter import messagebox
    # importing module for time zone and locatio access
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime


url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"

api_file= 'weather.key'
file_reader = ConfigParser()
file_reader.read(api_file)
api_key =file_reader['api_key']['key']


def weather_input(city):
    info= requests.get(url_api.format(city,api_key))
    if info:
        json_file= info.json()
        city = json_file["name"]
        wind =json_file["wind"]["speed"] 
        humidity = json_file["main"]["humidity"]
        pressure =json_file["main"]["pressure"]
        description= json_file["weather"][0]["description"]
        visibility= json_file["visibility"]
        tempeature=json_file["main"]["temp"]
        temp_C = int(tempeature - 273)
        feelsLike= json_file["main"]["feels_like"]
        feels_like_c = int(feelsLike- 273)
        country= json_file["sys"]["country"]

        result = (city, wind ,humidity, pressure,description, visibility, tempeature,temp_C, feelsLike,feels_like_c,country)
        return result 
    else :
        return None
    

def getWeather():
    city = search_city.get()


    # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")


    # getting Latitude and Longitude
    location = geolocator.geocode(city)


    # pass the Latitude and Longitude
    # into a timezone_at
    # and it return timezone
    obj = TimezoneFinder()

    # returns 'Europe/Berlin'
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    home= pytz.timezone(result)
    local_time = datetime.now(home)
    current_time= local_time.strftime("%H:%M:%S")
    label_t.config(text=current_time)
    label_name.config(text= "Current Time")

    weather = weather_input(city)
    

    if weather:
        label1_w["text"]= weather[1]
        label2_h["text"]= weather[2]
        label3_p["text"]= weather[3]
        label4_d["text"]= weather[4]
        label_v["text"]= weather[5]
        temp["text"]='{} C'.format(weather[7])
        feels["text"]= '{} '.format(weather[9])
        city_name["text"]= weather[0]
        country_name["text"]= weather[10]


    else :
        messagebox.showerror("Error", "Please Enter a Valid Name")

    #weather
    
    deg =Label(main_window ,fg= "orange" , bg="azure",text="o"  , font=("Helvetica", 15, "bold"))
    deg.place(x= 510 , y =210 )

    vis= Label(main_window ,fg= "black",text= "Visibility" , bg = "aqua" , font=("Helvetica", 15, "bold"))
    vis.place(x= 55 , y =290 )

    feels_text =Label(main_window,text="Feels Like" ,fg= "black" , bg = "azure" , font=("Helvetica", 13, "bold"))
    feels_text.place(x= 440, y =300 )


main_window=Tk()
main_window.title("Weather App")
main_window.minsize(width = 600 , height = 650)
main_window.resizable(False, False)
main_window["bg"]= "azure"



#Search Box

search_img = PhotoImage(file="Copy of search.png" , )
img1 = Label(image= search_img , bg= "azure" )
img1.place(relx=0.5, y =80 , anchor=CENTER)

search_city = StringVar() 
text_entry = Entry(main_window,textvariable=search_city, justify='center',width = 20,bd= 0,bg= "#404040", font=("poppins", 20, "bold"), fg= "white" )
text_entry.place(x =100, y = 63)

search_icon= PhotoImage(file= "Copy of search_icon.png" )
search_button= Button(main_window, image=search_icon , bd=0,bg= "#404040", cursor="hand2" , command=getWeather)
search_button.place(x= 435 , y = 52)


#logo

logo = PhotoImage(file= "Copy of logo.png")
logo_label= Label(image=logo,bg= "azure")
logo_label.place(relx=0.5, y =260 , anchor=CENTER)


#BOX

box= PhotoImage(file= "Copy of box.png")
box_label = Label(image= box, bg = "azure")
box_label.place(x=-150, y =500)


#labels
label1= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="WIND" , font=("Helvetica", 15, "bold"))
label1.place(x= 20 , y =530 )

label2= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="HUMIDITY" , font=("Helvetica", 15, "bold"))
label2.place(x= 140 , y =530 )

label3= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="PRESSURE" , font=("Helvetica", 15, "bold"))
label3.place(x= 290 , y =530 )

label4= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="DESRIPTION" , font=("Helvetica", 15, "bold"))
label4.place(x= 440 , y =530 )


label1_w= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="" , font=("Helvetica", 15, "bold"))
label1_w.place(x= 20 , y =560)

label2_h= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="" , font=("Helvetica", 15, "bold"))
label2_h.place(x= 140 , y =560 )

label3_p= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="" , font=("Helvetica", 15, "bold"))
label3_p.place(x= 290 , y =560 )

label4_d= Label(main_window ,fg= "black" , bg = "#1ab5ef", text ="" , font=("Helvetica", 15, "bold"))
label4_d.place(x= 435 , y =560 )

#time

label_name= Label(main_window ,fg= "black" ,text="", bg = "aqua", font=("Helvetica", 15, "bold"))
label_name.place(x= 35 , y =190)
label_t= Label(main_window ,fg= "black" ,text="", bg = "aqua" , font=("Helvetica", 15, "bold"))
label_t.place(x= 55 , y =230 )

#visibility
# vis= Label(main_window ,fg= "black",text= "Visibility" , bg = "aqua" , font=("Helvetica", 15, "bold"))
# vis.place(x= 55 , y =290 )

label_v= Label(main_window ,fg= "black" , bg = "aqua", text="" , font=("Helvetica", 15, "bold"))
label_v.place(x= 70 , y =330 )

#temp & feels like
temp= Label(main_window ,fg= "orange" , bg="azure",text=""  , font=("Helvetica", 50, "bold"))
temp.place(x= 430 , y =220 )

# deg =Label(main_window ,fg= "orange" , bg="azure",text="o"  , font=("Helvetica", 15, "bold"))
# deg.place(x= 510 , y =210 )

# feels_text =Label(main_window,text="Feels Like" ,fg= "black" , bg = "azure" , font=("Helvetica", 13, "bold"))
# feels_text.place(x= 440, y =300 )

feels =Label(main_window ,fg= "black" , bg = "azure",text="" , font=("Helvetica", 13, "bold"))
feels.place(x= 525, y =300 )

#city and country

city_name =Label(main_window ,fg= "black" , bg = "azure", text= "", font=("Helvetica", 25, "bold"))
city_name.place(relx=0.5, y =420 , anchor=CENTER)

country_name =Label(main_window ,fg= "black" , bg = "azure" ,text= "", font=("Helvetica", 25, "bold"))
country_name.place(relx=0.5, y =470 , anchor=CENTER)

main_window.mainloop()

