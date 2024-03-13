## Import all libraries
from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
import os
from PIL import ImageTk, Image
from tkinter import messagebox


import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt

from backend import *


background = "#f0ddd5"
framebg = "#62a7ff"
framefg= "#fefbfb"

root=Tk()
root.title("Heart attack prediction system")
root.geometry("1366x730+0+20")
root.resizable(False,False)
root.config(bg=background)


######## Analysis ###########################
def analysis():
    name= Name.get()
    D1=Date.get()
    today=datetime.date.today()
    A=today.year-DOB.get()

    try:
        B=selection()
    except:
        messagebox.showerror("Notice","Please select a gender")
        return
    
    try:
        F=selection2()
    except:
        messagebox.showerror("Notice","Please select fbs")
        return
    
    try:
        I=selection3()
    except:
        messagebox.showerror("Notice","Please select exang")
        return
    
    try:
        C=int(selection4())
    except:
        messagebox.showerror("Notice","Please select cp")
        return
    
    try:
        G=int(restecg_combobox.get())
    except:
        messagebox.showerror("Notice","Please select restcg")
        return
    
    try:
        K=int(selection5())
    except:
        messagebox.showerror("Notice","Please select slope")
        return
    
    try:
        L=int(ca_combobox.get())
    except:
        messagebox.showerror("Notice","Please select ca")
        return
    
    try:
        M=int(thal_combobox.get())
    except:
        messagebox.showerror("Notice","Please select thal")
        return
    
    try:
        D=int(trestbps.get())
        E=int(cole.get())
        H=int(thalach.get())
        J=int(oldpeak.get())
    except:
        messagebox.showerror("Notice no data","No input data")
        return
    
    print ("A is age", A)
    print ("B is gender", B)
    print ("C is cp", C)
    print ("D is trestbps", D)
    print ("E is cholesterol", E)
    print ("F is fbs", F)
    print ("G is restcg", G)
    print ("H is thalach", H)
    print ("I is Exang", I)
    print ("J is oldpeak", J)
    print ("K is slope", K)
    print ("L is ca", L)
    print ("M is thal", M)
    
    
########################## First graph #######################

    f = Figure(figsize=(5,5), dpi=80)
    a= f.add_subplot(111)
    a.plot(["Gender","fbs","exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH)
    canvas._tkcanvas.place(width=250,height=250, x=530,y=225)

    ########################## Second graph #######################

    f2 = Figure(figsize=(5,5), dpi=80)
    a2= f2.add_subplot(111)
    a2.plot(["age","trestbps","cholesterol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=250,height=250, x=795,y=225)

########################## Third graph #######################

    f3 = Figure(figsize=(5,5), dpi=80)
    a3= f3.add_subplot(111)
    a3.plot(["Oldpeak","resticg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=250,height=250, x=530,y=470)

########################## Fourth graph #######################

    f4 = Figure(figsize=(5,5), dpi=80)
    a4= f4.add_subplot(111)
    a4.plot(["Slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=250,height=250, x=795,y=470)



####### Input data #######################
    input_data=(A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy=np.asanyarray(input_data)
    
    input_data_reshape=input_data_as_numpy.reshape(1,-1)

    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0]==0):
        print("This person does not have heart disease")
        reporte.config(text=f"Report: {0}",fg="#8dc63f")
        reporte1.config(text=f"{name}, does not have heart disease")
    
    else:
        print("This person has heart disease")
        reporte.config(text=f"Report: {1}",fg="#ed1c24")
        reporte1.config(text=f"{name}, has heart disease")



### info window#############################################################
def Info():
    Icon_window= Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+350+100")

    # set the icon image 
    icon_image=PhotoImage(file ="Images/info.png" )
    Icon_window.iconphoto(False,icon_image)

    #Heading
    Label(Icon_window,text="Information related to the dataset", font="robot 20 bold").pack(padx=20, pady=20)


    # Info  (alt+shift+down arrow is to copy an entire line of code)
    Label (Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
    Label (Icon_window,text="gender - gender (1 = Male; 0 = Female)",font="arial 11").place(x=20,y=130)
    Label (Icon_window,text="cp - Chest pain type (0 = typical angina; 1 = atypical angina; 2 = non-anginal pain; 3=asymptomatic)",font="arial 11").place(x=20,y=160)
    Label (Icon_window,text="trestbps - resting blood pressure (in mm Hg)",font="arial 11").place(x=20,y=190)
    Label (Icon_window,text="cholesterol - serum cholesterol in mg/dl",font="arial 11").place(x=20,y=220)
    Label (Icon_window,text="fbs - fasting blood sugar > 120mg/dl (1=true;0=false)",font="arial 11").place(x=20,y=250)
    Label (Icon_window,text="restecg - resting electrocardiographic results (0 = normal; 1 = ST-T; 2 = hypertrophy)",font="arial 11").place(x=20,y=280)
    Label (Icon_window,text="thalach - maximum heart rate",font="arial 11").place(x=20,y=310)
    Label (Icon_window,text="exang - exercise induced angina (1 = yes;0 = no)",font="arial 11").place(x=20,y=340)
    Label (Icon_window,text="oldpeak - ST depression induced by exercise",font="arial 11").place(x=20,y=370)
    Label (Icon_window,text="slope - the slope of the peak exercise ST segment (0 = upsloping; 1= flat; 2=downsloping)",font="arial 11").place(x=20,y=400)
    Label (Icon_window,text="ca - number of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=430)
    Label (Icon_window,text="thal  0 = normal; 1 = fixed defect; 2 = reversible defect",font="arial 11").place(x=20,y=460)


    Icon_window.mainloop()

############## Used to close the window##########
def logout():
    root.destroy()

######## clear all cells with a single click
def Clear ():
    Name.get("")
    DOB.get("")
    trestbps.get("")
    cole.get("")
    thalach.set("")
    oldpeak.set("")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#Icon 1
#Double slash for python to recognize the command
imagen_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,imagen_icon)

# Title section
logo = PhotoImage (file = "Images/header.png")
myimagen= Label(image=logo,bg=background)
myimagen.place(x=0,y=0)


#<<<<<<frame3<<<<<<<<<<<<
heading_entry= Frame(root, width=800, height=190, bg="#df2d4b")
heading_entry.place(x=600, y=20)

Label(heading_entry, text="Registration No.", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=30,y=0)
Label(heading_entry, text="Date", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=430,y=0)

Label(heading_entry, text="Patient Name", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=30,y=90)
Label(heading_entry, text="Year of Birth", font= "arial 13", bg= "#df2d4b",fg=framefg).place(x=430,y=90)


#<<<<<<<<<<<<<<<<<<<MISSING IMAGES>>>>>>>>>>>>>>>>>>>>>>>>>>
entry_image=PhotoImage(file="Images/Rounded Rectangle 1.png")    
entry_image2=PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(heading_entry, image=entry_image, bg="#df2d4b").place(x=20,y=30)
Label(heading_entry, image=entry_image, bg="#df2d4b").place(x=405,y=30)

Label(heading_entry, image=entry_image2, bg="#df2d4b").place(x=20,y=120)
Label(heading_entry, image=entry_image2, bg="#df2d4b").place(x=405,y=120)

# The following command is used to enter data where specified
Registration = IntVar()
reg_entry= Entry(heading_entry,textvariable=Registration, width=30, font="arial 15", bg="#0e5363",fg="white", bd=0)
reg_entry.place(x=30,y=45)

Date= StringVar()
today = date.today()
d1=today.strftime("%d/%m/%Y")
date_entry=Entry(heading_entry, textvariable=Date,width=15, font="arial 15", bg="#0e5363", fg="white",bd=0 )
date_entry.place(x=430,y=45)
Date.set(d1)


Name = StringVar()
name_entry= Entry(heading_entry,textvariable=Name, width=20, font="arial 15", bg="#ededed",fg="#222222", bd=0)
name_entry.place(x=30,y=135)

DOB = IntVar()
dob_entry= Entry(heading_entry,textvariable=DOB, width=20, font="arial 15", bg="#ededed",fg="#222222", bd=0)
dob_entry.place(x=430,y=135)


#################################################### Body ################################################ 4 

Detail_entry = Frame(root, width=490, height=260, bg="#dbe0e3")
Detail_entry.place(x=30,y=450)


################################# Radio button ##########################################################3 5
Label (Detail_entry, text= "Gender:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=10)
Label (Detail_entry, text= "fbs:", font="arial 13", bg=framebg, fg=framefg).place(x=180,y=10)
Label (Detail_entry, text= "exang:", font="arial 13", bg=framebg, fg=framefg).place(x=335,y=10)


def selection():
    if gen.get()==1:
        Gender=1
        return(Gender)
        print(Gender)
    elif gen.get()==2:
        Gender=0
        return(Gender)
        print(Gender)
    else:
        print(Gender)


def selection2():
    if fbs.get()==1:
        Fbs=1
        return(Fbs)
        print(Gender)
    elif fbs.get()==2:
        Fbs=0
        return(Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang=1
        return(Exang)
        print(Exang)
    elif exang.get()==2:
        Exang=0
        return(Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1= Radiobutton(Detail_entry, text= "Male", variable=gen, value=1, command=selection)
R2= Radiobutton(Detail_entry, text= "Female", variable=gen, value=2, command=selection)
R1.place(x=53, y=10)
R2.place(x=120,y=10)

fbs = IntVar()
R3= Radiobutton(Detail_entry, text= "True", variable=fbs, value=1, command=selection2)
R4= Radiobutton(Detail_entry, text= "False", variable=fbs, value=2, command=selection2)
R3.place(x=213, y=10)
R4.place(x=273,y=10)

exang = IntVar()
R5= Radiobutton(Detail_entry, text= "Yes", variable=exang, value=1, command=selection3)
R6= Radiobutton(Detail_entry, text= "No", variable=exang, value=2, command=selection3)
R5.place(x=387, y=10)
R6.place(x=430,y=10)


################################## Combobox ###############################  6
Label(Detail_entry, text="cp", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=50)
Label(Detail_entry, text="restecg", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=90)
Label(Detail_entry, text="slope", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=130)
Label(Detail_entry, text="ca:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=170)
Label(Detail_entry, text="thal:", font="arial 13", bg=framebg, fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input=="0 = typical angina":
        return(0)
    elif input=="1 = atypical angina":
        return(1)
    elif input == "2 = non-anginal pain":
        return(2)
    elif input =="3=asymptomatic":
        return(3)
    else:
        print(Exang)

def selection5():
    input=slope_combobox.get()
    if input=="0 = upsloping":
        return(0)
    elif input=="1= flat":
        return(1)
    elif input == "2=downsloping":
        return(2)
    else:
        print(Exang)



cp_combobox=Combobox(Detail_entry, values=["0 = typical angina", "1 = atypical angina", "2 = non-anginal pain", "3=asymptomatic"],font="arial 12",state="r",width=14)
restecg_combobox=Combobox(Detail_entry, values=["0", "1", "2"],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry, values=["0 = upsloping", "1= flat", "2=downsloping"],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry, values=["0","1","2","3","4"],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry, values=["0 ", "1", "2"],font="arial 12",state="r",width=14)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)


##################### Data entry box  #########################3 7
Label (Detail_entry, text="Smoker:", font = "arial 13", width=8, bg="#dbe0e3",fg="black").place(x=240,y=50)
Label (Detail_entry, text="trestbps", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=90)
Label (Detail_entry, text="cholesterol", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=130)
Label (Detail_entry, text="thalach", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=170)
Label (Detail_entry, text="oldpeak", font = "arial 13", width=8, bg=framebg,fg=framefg).place(x=240,y=210)


trestbps=StringVar()
cole=StringVar()
thalach=StringVar()
oldpeak=StringVar()

trestbps_entry=Entry(Detail_entry,textvariable=trestbps,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
cole_entry=Entry(Detail_entry,textvariable=cole,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
thalach_entry=Entry(Detail_entry,textvariable=thalach,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)
oldpeak_entry=Entry(Detail_entry,textvariable=oldpeak,width=10,font="arial 15",bg="#ededed",fg="#222222",bd=0)

trestbps_entry.place(x=330,y=90)
cole_entry.place(x=330,y=130)
thalach_entry.place(x=330,y=170)
oldpeak_entry.place(x=330,y=210)
#############################################################################################################


############################### Report ################################ 8

imagen_reporte=PhotoImage(file="Images/Report.png")
reporte_background =Label(image=imagen_reporte,bg=background)
reporte_background.place(x=1070,y=340)

reporte=Label(root,text="hello",font="arial 25 bold",bg="white", fg="#8dc63f")
reporte.place(x=1120,y=520)

reporte1= Label(root,text="hello",font="arial 10 bold",bg="white")
reporte1.place(x=1100,y=570)

#######################################################################################


################################### Graph ####################################### 9
grafica_imagen=PhotoImage(file="Images/graph.png")
Label(image=grafica_imagen).place(x=540,y=270)
Label(image=grafica_imagen).place(x=780,y=270)
Label(image=grafica_imagen).place(x=540,y=500)
Label(image=grafica_imagen).place(x=780,y=500)



########################### Button ####################  10

boton_analisis= PhotoImage(file="Images/Analysis.png")
Button(root,image=boton_analisis, bd=0,bg=background, cursor="hand2",command=analysis).place (x=1085,y=240)

############################# Info button ########################
boton_info= PhotoImage(file="Images/info.png")
Button(root,image=boton_info, bd=0,bg=background, cursor="hand2",command= Info).place (x=10,y=240)


############################# Save button ########################
boton_save= PhotoImage(file="Images/save.png")
Button(root,image=boton_save, bd=0,bg=background, cursor="hand2").place (x=1300,y=250)

############################# Smoker and non-smoker button ######################## 11
button_mode=True
choice= "Smoker"

def changemode():
    global button_mode
    global choice
    if button_mode:
        choice = "Non-smoker"
        mode.config(image=no_fumador_icon,activebackground="white")
        button_mode=False
    else:
        choice = "Smoker"
        mode.config(image=fumador_icon,activebackground="white")
        button_mode=True

    print(choice)

fumador_icon=PhotoImage(file="Images/smoker.png")
no_fumador_icon=PhotoImage(file="Images/non-smoker.png")
mode=Button(root,image=fumador_icon,bg="#dbe0e3",bd=0,cursor="hand2",command=changemode)
mode.place(x=370,y=495)



################################## Logout button ####################################### 12

logout_icon=PhotoImage(file="Images/logout.png")
logout_boton= Button(root, image=logout_icon,bg="#df2d4b", cursor="hand2",bd=0,command=logout)
logout_boton.place(x=1300,y=5)


###############################################################################################


root.mainloop()

## info window (info button)<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<