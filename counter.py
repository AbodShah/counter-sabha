import customtkinter
import datetime
import time
from PIL import Image




def time_now():

    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M")
    label2.configure(text=formatted_time)
    label2.after(1000, time_now)




customtkinter.set_appearance_mode("system")  
customtkinter.set_default_color_theme("dark-blue")  



root = customtkinter.CTk()
root.after(201, lambda :root.iconbitmap("sabha.ico")) 
root.geometry("650x600")
root.title("Tasbeeh")
root.resizable(False,False)


tasbeha = 000

def onclickbutton1():
    global tasbeha
    tasbeha = tasbeha + 1
    label1.configure(text = tasbeha)

def onclickbutton2():
    global tasbeha
    tasbeha = 000
    label1.configure(text = tasbeha)





font1 = customtkinter.CTkFont(size=45)
label1 = customtkinter.CTkLabel(master=root , text=tasbeha , font=font1 )
label1.pack()
label1.place(relx="0.5" , rely = "0.5")


font3 = customtkinter.CTkFont(size=20 , family="arial")
label2 = customtkinter.CTkLabel(master=root  , font=font3 )
label2.pack()
label2.place(relx = "0.1" , rely = "0.1")
time_now()


click_image = customtkinter.CTkImage(light_image=Image.open("clickfinger.jpg"),
                                  dark_image=Image.open("clickfinger.jpg"),
                                    size=(60, 60))

font4 = customtkinter.CTkFont(size=25)
button1 = customtkinter.CTkButton(master = root,
 text="Tasbeh",
  width=160,
   height=40,
    image=click_image,
     command=onclickbutton1,
     corner_radius=10)
root.bind("x", lambda event: button1.invoke())
button1.pack()
button1.place(relx="0.412" , rely = "0.66")


label3 = customtkinter.CTkLabel(master=root , text="Press x ")
label3.pack()
label3.place(relx="0.412" , rely = "0.59")


restart_image = customtkinter.CTkImage(light_image=Image.open("refresh-flat.png"),
                                  dark_image=Image.open("refresh-flat.png"),
                                  size=(30, 30))


button2 = customtkinter.CTkButton(master = root , text="Reset" ,
 width=10 ,
  height=40  ,
   corner_radius=1000,
    command=onclickbutton2,
    image=restart_image)
button2.pack()
button2.place(relx="0.01" , rely = "0.85")




switch_var = customtkinter.StringVar(value="on")

def theme():
    global on_off
    on_off = switch_var.get()
    if on_off == "on" :
             customtkinter.set_appearance_mode("dark")
    elif on_off == "off" : 
             customtkinter.set_appearance_mode("light")
theme()
     

switch_1 = customtkinter.CTkSwitch(master=root, text="Dark mode 🌙", 
 onvalue="on" ,
  offvalue="off" ,
   variable=switch_var,
    command=theme )
theme()
switch_1.pack()
switch_1.place(relx="0.01" , rely = "0.93")








root.mainloop()
