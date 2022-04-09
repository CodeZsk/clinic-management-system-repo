from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter import ttk as ttk
from turtle import *
from addAppointment import addAppointment
from updateManageAppointment import updateAppointmentBody


def hideAllFrames(manage_appointmnet_frame):
    for widgets in manage_appointmnet_frame.winfo_children():
        widgets.destroy()
    manage_appointmnet_frame.pack_forget()


def manageAppointmentBody(add_patient_frame, manage_patient_frame, add_appointment_frame,
                          manage_appointmnet_frame, show_patient_info_frame, show_patient_Appointment_info_frame, conn):
    try:
        cur = conn.cursor()
        cur.execute("select * from appointment_list")
    except:
        cur = conn.cursor()
        cur.execute("create table appointment_list(appointment_id int primary key auto_increment , patient_id int , first_name varchar(30) not null , middle_name varchar(30) not null , last_name varchar(30) not null , age int not null, gender varchar(20) not null , blood_group varchar(20) not null , phone_no varchar(10) not null , email_id varchar(40) not null , doctor_name varchar(40) not null , diagonosis varchar(255) , time time, date date, status varchar(30), FOREIGN KEY(patient_id) REFERENCES patient_info(patient_id));")
        cur.execute("select * from appointment_list")

    def connect():
        global appointment_list
        cur.execute("select * from appointment_list")
        appointment_list = cur.fetchall()

    def search_name(name, conn):
        # reset()
        cur = conn.cursor()
        cur.execute('select * from appointment_list where first_name=%s', name)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_age(age, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where age=%s', age)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_gender(gender, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where gender=%s', gender)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_date(date, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where date=%s', date)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_time(time, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where time=%s', time)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_dr_name(name, conn):
        cur = conn.cursor()
        cur.execute(
            'select * from appointment_list where doctor_name=%s', name)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_phone_no(number, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where phone_no=%s', number)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def search_apt_id(id, conn):
        cur = conn.cursor()
        cur.execute('select * from appointment_list where patient_id=%s', id)
        global appointment_list
        appointment_list = cur.fetchall()

        return appointment_list

    def deleteAll():
        for record in list_app.get_children():
            list_app.delete(record)
        for record in seen_app.get_children():
            seen_app.delete(record)

    def patient_Info(id, conn):
        cur = conn.cursor()
        cur.execute(
            'select * from appointment_list where appointment_id=%s', id)
        patient_info = cur.fetchall()
        return patient_info

    def check_empty():
        if appointment_list == ():
            messagebox.showwarning(
                "showwarning", "No Information Available")
            connect()

    def select():
        option = filter_menu.get()
        if option == 'apt id' or option == 'Apt id':
            apt_id = search.get()
            int(apt_id)
            str(apt_id)
            patient_info2 = patient_Info(apt_id, conn)
            print(patient_info2)
            hideAllFrames(manage_appointmnet_frame)
            show_patient_Appointment_info_frame.pack(fill='both', expand=1)
            updateAppointmentBody(
                show_patient_Appointment_info_frame, conn, apt_id)
            try:
                int(apt_id)
                str(apt_id)
                patient_info2 = patient_Info(apt_id, conn)
                print(patient_info2)
                hideAllFrames(manage_appointmnet_frame)
                show_patient_Appointment_info_frame.pack(fill='both', expand=1)
                updateAppointmentBody(
                    show_patient_Appointment_info_frame, conn, apt_id)
            except ValueError:
                messagebox.showwarning(
                    "showwarning", "Enter Numeric Value for Appointment Id")

        else:
            messagebox.showwarning(
                "showwarning", "Select option only work with apt id (Appointment id)")

    def reset():
        deleteAll()
        connect()
        un_seen_body()
        seen_body()

    def filter_list():
        option = filter_menu.get()
        if option == 'name' or option == 'Name':
            name = search.get().strip()
            if name:
                search_name(name, conn)
                deleteAll()
                check_empty()
                un_seen_item()
                seen_item()
            else:
                pass
        elif option == 'age' or option == 'Age':
            try:
                age = int(search.get())
                search_age(age, conn)
                deleteAll()
                check_empty()
                un_seen_item()
                seen_item()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Numeric Value for Age")

        elif option == 'gender' or option == 'Gender':
            gender = search.get().strip()
            if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
                search_gender(gender, conn)
                deleteAll()
                check_empty()
                un_seen_item()
                seen_item()
            else:
                messagebox.showwarning(
                    "showwarning", "Gender Should be for Male(M) or female(F)")
                reset()
        elif option == 'date' or option == 'Date':
            date = search.get()
            try:
                search_date(date, conn)
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Date In This (YYYY-MM-DD) Format Only")
            deleteAll()
            un_seen_item()
            seen_item()
        elif option == 'time' or option == 'Time':
            time = search.get()
            try:
                search_time(time, conn)
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Time In This (HH:MM:SS) Format Only")
            deleteAll()
            un_seen_item()
            seen_item()
        elif option == 'dr. name' or option == 'Dr. Name':
            name = search.get().strip()
            if name:
                dr_name = 'dr. ' + name
                search_dr_name(dr_name, conn)
                deleteAll()
                check_empty()
                un_seen_item()
                seen_item()
            else:
                pass
        elif option == 'phone no.' or option == 'phone no.':
            phone_no = search.get()
            try:
                int(phone_no)
                str(phone_no)
                search_phone_no(phone_no, conn)
                deleteAll()
                check_empty()
                un_seen_item()
                seen_item()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Numeric Value for Phone number")
                reset()

        elif option == 'apt id' or option == 'Apt id':
            apt_id = search.get()
            # int(apt_id)
            print(type(apt_id))
            if apt_id:
                int(apt_id)
                search_apt_id(apt_id, conn)
                deleteAll()
                un_seen_item()
                seen_item()
            else:
                messagebox.showwarning(
                    "showwarning", "Enter Numeric Value for Appointment Id")
                reset()
        else:
            messagebox.showwarning("showwarning", "NO Search Option Available")

    def un_seen_body():
        list_app['columns'] = ("Patient Name", "Age", "Gender", "Blood Type",
                               "Time", "Date", "Phone Number", "Doctor Name", "Status")
        # placing header
        for i in header_list:
            list_app.column(i, anchor=W, width=150, minwidth=25)
        # seting header text
        for i in header_list:
            list_app.heading(i, text=i, anchor=W)

        # seting header values
        un_seen_item()
        # print(list_app)

        # seting default column value
        list_app.column("#0", width=0, minwidth=48)
        list_app.heading("#0", text="Apt id", anchor=W)

        # placing treeview
        list_app.pack(fill=BOTH, expand=True)

    def seen_body():
        seen_app['columns'] = ("Patient Name", "Age", "Gender", "Blood Type",
                               "Time", "Date", "Phone Number", "Doctor Name", "Status")
        # placing header
        for i in header_list:
            seen_app.column(i, anchor=W, width=150, minwidth=25)
        # seting header text
        for i in header_list:
            seen_app.heading(i, text=i, anchor=W)

        # seting header values
        seen_item()
        # print(seen_app)

        # seting default column value
        seen_app.column("#0", width=0, minwidth=48)
        seen_app.heading("#0", text="Apt id", anchor=W)

        # placing treeview
        seen_app.pack(fill=BOTH, expand=True)

    def un_seen_item():
        count = 0
        for i in appointment_list:
            if i[14] == "Unseen":
                if count % 2 == 0:
                    list_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[2], i[5], i[6], i[7], i[12], i[13], i[8], i[10], i[14], 'unseen'), tags=('evenrow',)
                    )
                else:
                    list_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[2], i[5], i[6], i[7], i[12], i[13], i[8], i[10], i[14], 'unseen'), tags=('oddrow',)
                    )
                count += 1

    def seen_item():
        print(appointment_list)
        counts = 0
        for i in appointment_list:
            if i[14] == "Seen" or i[14] == "Cancelled":
                if counts % 2 == 0:
                    seen_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[2], i[5], i[6], i[7], i[12], i[13], i[8], i[10], i[14], 'seen'), tags=('evenrow')
                    )
                else:
                    seen_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[2], i[5], i[6], i[7], i[12], i[13], i[8], i[10], i[14], 'seen'), tags=('oddrow')
                    )
                counts += 1

    headerFrame = Frame(manage_appointmnet_frame, bg='white')
    header = Label(headerFrame, text="Appointment List",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N)
    headerFrame.pack(anchor=N, fill='x', expand=0)
    # search
    # search Frame
    search_frame = Frame(manage_appointmnet_frame, bg="#7acaff", pady=7)
    search_frame.pack(fill='both', expand=0, padx=20)
    # serch entry
    search = Entry(search_frame, width=25)
    search.pack(side=LEFT)
    # filter option
    filter_menu = Combobox(search_frame, width=8)
    filter_menu['values'] = ('name', 'age', 'gender', 'date',
                             'time', 'dr. name', 'phone no.', 'apt id')
    filter_menu.set('Filter')
    filter_menu.pack(side=LEFT)
    # search btn
    search_btn = Button(search_frame, text="Search", command=filter_list)
    search_btn.pack(side=LEFT, padx=7)
    # reset btn
    reset_btn = Button(search_frame, text='Reset', command=reset)
    reset_btn.pack(side=LEFT, padx=6)
    # select btn
    select_btn = Button(search_frame, text='Select',
                        command=select)
    select_btn.pack(side=LEFT, padx=6)
    # add appointment
    search = Entry(search_frame, width=25)
    search.pack(side=RIGHT)
    addAppointmentBtn = Button(
        search_frame, text="Add Appointment", command=lambda: addAppointment(add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame, show_patient_info_frame, show_patient_Appointment_info_frame, conn, search))
    addAppointmentBtn.pack(side="right")
    header_list = ("Patient Name", "Age", "Gender", "Blood Type",
                   "Time", "Date", "Phone Number", "Doctor Name", "Status")
# Treeview
    connect()
    # unseen treeview
    list_app_frame = Frame(manage_appointmnet_frame)
    list_app_frame.pack()
    list_app_scrollBar = Scrollbar(
        list_app_frame, orient="vertical")
    list_app_scrollBar.pack(side=RIGHT, fill=Y)
    list_app = Treeview(list_app_frame, yscrollcommand=list_app_scrollBar.set)
    list_app_scrollBar.configure(command=list_app.yview)
    # unseen style
    list_app.tag_configure('oddrow', background="silver")
    list_app.tag_configure('evenrow', background="white")
    un_seen_body()
    # seen teeview
    seen_app_frame = Frame(manage_appointmnet_frame)
    seen_app_frame.pack(pady=20, ipady=60)
    seen_app_scrollBar = Scrollbar(
        seen_app_frame, orient="vertical")
    seen_app_scrollBar.pack(side=RIGHT, fill=Y)
    seen_app = Treeview(seen_app_frame, yscrollcommand=seen_app_scrollBar.set)
    seen_app_scrollBar.configure(command=seen_app.yview)
    # seen style
    seen_app.tag_configure('oddrow', background="silver")
    seen_app.tag_configure('evenrow', background="white")

    seen_body()
