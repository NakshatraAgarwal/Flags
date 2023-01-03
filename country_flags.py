from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root=Tk()
root.title("Country Flags")
root.geometry("600x400")
root.configure(background="lightblue")

get_input = Entry(root)
show_label = Label(root)

india_flag = ImageTk.PhotoImage(Image.open ("India.jpg"))
america_flag = ImageTk.PhotoImage(Image.open ("America.jpg"))
australia_flag = ImageTk.PhotoImage(Image.open ("Australia.png"))
japan_flag = ImageTk.PhotoImage(Image.open ("Japan.jpg"))
philippines_flag = ImageTk.PhotoImage(Image.open ("Philippines.png"))

flags_dictionary = { "India" : india_flag , 
                    "America" : america_flag ,
                    "Australia" : australia_flag ,
                    "Philippines" : philippines_flag,
                    "Japan" : japan_flag,}

def showFlags():
    flag_name = get_input.get()
    # Add a try and except block to handle the error created by the following line of code
    try:
        show_label['image'] = flags_dictionary[flag_name]
    except:
       messagebox.showinfo("Key Error", "Sorry! This Country Flag is not present in our system")


btn = Button(root , text="Show Flag", bg="green", command=showFlags)
get_input.place(relx=0.5, rely=0.1, anchor=CENTER)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
show_label.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()