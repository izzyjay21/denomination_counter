from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def msg():
    message=messagebox.showinfo(title="alert",message=" do you want to calculate the denomination caount?")
    if message=='ok':
        topwin()


    

def topwin():
    top=Toplevel()
    top.geometry("500x500")
    top.title("denomination calculator")
    top.config(bg="light green")
    label=Label(top,text="Enter the amount",bg="light green",fg="teal")
    label.place(x=200,y=50)
    entry0=Entry(top)
    entry0.place(x=180,y=80)
    
    
    label1=Label(top,text="here are the number of notes for each denomination",bg="light green")
    label1.place(x=100,y=140)
    label2=Label(top,text="2000",bg="light green")
    label2.place(x=150,y=170)
    entry1=Entry(top)
    entry1.place(x=200,y=170)
    label3=Label(top,text="500",bg="light green")
    label3.place(x=150,y=200)
    entry2=Entry(top,)
    entry2.place(x=200,y=200)
    label4=Label(top,text="100",bg="light green")
    label4.place(x=150,y=230)
    entry3=Entry(top)
    entry3.place(x=200,y=230)  


    def calculate():
         try:
            global amount
            amount=int(entry0.get())
            note2000=amount//2000
            amount=amount%2000
            note500=amount//500
            amount=amount%500
            note100=amount//100
            entry1.delete(0,END)
            entry1.insert(END,str(note2000))
            entry2.delete(0,END)
            entry2.insert(END,str(note500))
            entry3.delete(0,END)
            entry3.insert(END,str(note100))
         except ValueError:
             messagebox.showerror("error","invaild input")

    button=Button(top, text="calculate",bg="gold",fg="red",command=calculate)
    button.place(x=200,y=110)


window=Tk()

window.title("denomination calculator")
window.config(bg="light blue")
window.geometry("300x300")

upload=Image.open("app_img.jpg")
image=ImageTk.PhotoImage(upload)
upload=upload.resize((300,300))
label=Label(window,image=image)
label.pack()
label1=Label(window,text="welcome to the denomination counter application",bg="light blue")
button=Button(window, text="lets get started",bg="gold",fg="red",command=msg)
label1.pack()
button.pack()
#label1.place(x=50,y=260)








print(2000//100)
window.mainloop()
#print(2000/100)