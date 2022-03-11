from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

# connection to database

try:
    def connect():
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='clinic',
        )
        cur = conn.cursor()
        cur.execute("select * from appointment_list")
        global appointment_list
        appointment_list = cur.fetchall()
        conn.close()
except:
    def connect():
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='clinic',
        )
        cur = conn.cursor()
        cur.execute("create table appointment_list(patient_id varchar(10) primary key not null, name varchar(30) not null, age int not null, gender char not null, time time, date date, phone_no varchar(10) not null unique, doctor_name varchar(30), status boolean")
        cur.execute("select * from appointment_list")
        global appointment_list
        appointment_list = cur.fetchall()
        conn.close()

# function
# searching into the database


def search_name(name):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where name=%s', name)
    global appointment_list
    appointment_list = cur.fetchall()

    conn.close()
    return appointment_list


def search_age(age):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where age=%s', age)
    global appointment_list
    appointment_list = cur.fetchall()

    conn.close()
    return appointment_list


def search_gender(gender):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where gender=%s', gender)
    global appointment_list
    appointment_list = cur.fetchall()
    conn.close()
    return appointment_list


def search_date(date):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where date=%s', date)
    global appointment_list
    appointment_list = cur.fetchall()
    conn.close()
    return appointment_list


def search_time(time):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where time=%s', time)
    global appointment_list
    appointment_list = cur.fetchall()
    conn.close()
    return appointment_list


def search_dr_name(name):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where doctor_name=%s', name)
    global appointment_list
    appointment_list = cur.fetchall()
    conn.close()
    return appointment_list


def search_phone_no(number):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="root",
        db='clinic',
    )
    cur = conn.cursor()
    cur.execute('select * from appointment_list where phone_no=%s', number)
    global appointment_list
    appointment_list = cur.fetchall()
    conn.close()
    return appointment_list

# filter list


def filter_list():
    option = filter_menu.get()
    if option == 'name' or option == 'Name':
        name = search.get()
        search_name(name)
        deleteAll()
        item()
    elif option == 'age' or option == 'Age':
        try:
            age = int(search.get())
            search_age(age)
            deleteAll()
            item()
        except:
            messagebox.showwarning(
                "showwarning", "Enter integer value for age")
            # deleteAll()
            # connect()

        # item()
    elif option == 'gender' or option == 'Gender':
        gender = search.get()
        search_gender(gender)
        deleteAll()
        item()
    elif option == 'date' or option == 'Date':
        date = search.get()
        try:
            search_date(date)
        except:
            messagebox.showwarning(
                "showwarning", "Enter Date In This (YYYY-MM-DD) Format Only")
        deleteAll()
        item()
    elif option == 'time' or option == 'Time':
        time = search.get()
        try:
            search_time(time)
        except:
            messagebox.showwarning(
                "showwarning", "Enter Time In This (HH:MM:SS) Format Only")
        deleteAll()
        item()
    elif option == 'dr. name' or option == 'Dr. Name':
        dr_name = search.get()
        search_dr_name(dr_name)
        deleteAll()
        item()
    elif option == 'phone no.' or option == 'phone no.':
        phone_no = search.get()
        search_phone_no(phone_no)
        deleteAll()
        item()
    else:
        messagebox.showwarning("showwarning", "NO Search Option Available")

# delete list


def deleteAll():
    for record in list_app.get_children():
        list_app.delete(record)

# select list


def select():
    selected_item = list_app.selection()[0]


def List_body():
    list_app['columns'] = ("Patient Name", "Age", "Gender",
                           "Time", "Date", "Phone Number", "Doctor Name", "Status")
    # placing header
    for i in header_list:
        list_app.column(i, anchor=W, width=120, minwidth=25)
    # seting header text
    for i in header_list:
        list_app.heading(i, text=i, anchor=W)

    # seting header values
    item()

    # seting default column value
    list_app.column("#0", width=0, minwidth=48)
    list_app.heading("#0", text="Sr.No", anchor=W)

    # placing treeview
    list_app.pack(pady=20, fill=BOTH, expand=True, padx=4)


# list item
def item():
    if appointment_list == ():
        messagebox.showwarning("showwarning", "NO Data Found")
        connect()
        item()
    else:
        srNo = 1
        count = 0
        for i in appointment_list:
            list_app.insert(parent='', index='end', iid=count, text=srNo, values=(
                i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            )
            count += 1
            srNo += 1


# tkinter
root = Tk()
root.title("Appointment")
root.geometry('800x600')
root.configure(bg='white')

# header title
header = Label(text="Appointment List", font=("Arial", 20), bg="white")
header.pack(anchor=N)

# search
# search Frame
search_frame = Frame(root, bg="white")
search_frame.pack(anchor=NE, padx=20)
# serch entry
search = Entry(search_frame, width=25)
search.pack(side=LEFT)
# filter option
filter_menu = Combobox(search_frame, width=8)
filter_menu['values'] = ('name', 'age', 'gender', 'date',
                         'time', 'dr. name', 'phone no.')
filter_menu.set('Filter')
filter_menu.pack(side=LEFT)
# connect to ds
connect()
# search btn
search_btn = Button(search_frame, text="Search", command=filter_list)
search_btn.pack(side=LEFT, padx=7)

# select btn
select_btn = Button(search_frame, text="Select", command=select)
select_btn.pack(side=LEFT, padx=7)

# list rendering

header_list = ["Patient Name", "Age", "Gender",
               "Time", "Date", "Phone Number", "Doctor Name", "Status"]
# Treeview
global list_app
list_app = Treeview(root)
List_body()


root.mainloop()
