
# Import Required Library
from tkinter import *
from tkcalendar import Calendar
from datetime import datetime, date
# Create Object
root = Tk()

# Set geometry
root.geometry("400x400")

# Add Calendar
todayDate = date.today()
month = todayDate.month
day = todayDate.day
year = todayDate.year

cal = Calendar(root, selectmode='day',
               year=year, month=month, day=day)

cal.pack(pady=20)


def grad_date():
    dateLa.config(text="Selected Date is: " + cal.get_date())


# Add Button and Label
Button(root, text="Get Date",
       command=grad_date).pack(pady=20)

dateLa = Label(root, text="")
dateLa.pack(pady=20)

# Execute Tkinter
root.mainloop()
