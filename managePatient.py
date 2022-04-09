from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter import ttk as ttk
from turtle import *
import pymysql
# from app import hideAllFrames


def hideAllFrames(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()
    frame.pack_forget()


def managePatientBody(frame, show_patient_info_frame, conn):
    try:
        cur = conn.cursor()
        cur.execute("select * from patient_info")
    except:
        cur = conn.cursor()
        cur.execute("create table patient_info(patient_id int primary key auto_increment, first_name varchar(30) not null, middle_name varchar(30) not null, last_name varchar(30) not null, age int not null, gender varchar(20) not null, blood_group varchar(5), phone_no varchar(10) not null, email_id varchar(30), relative_name varchar(20), relation varchar(20), relative_number varchar(10), relative_email varchar(30), address varchar(70), city varchar(10), state varchar(20), pin_code varchar(6), doctor_name varchar(30), digonosis varchar(30), history varchar(200), date date, time time)")
        cur.execute("select * from patient_info")

    def connect():
        global patient_list
        cur.execute("select * from patient_info")
        patient_list = cur.fetchall()

    def search_name(name, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where first_name=%s', name)
        global patient_list
        patient_list = cur.fetchall()
        print(patient_list)
        return patient_list

    def search_age(age, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where age=%s', age)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def search_gender(gender, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where gender=%s', gender)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def search_blood_group(blood_group, conn):
        cur = conn.cursor()
        cur.execute(
            'select * from patient_info where blood_group=%s', blood_group)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def search_drName(doctor_name, conn):
        cur = conn.cursor()
        cur.execute(
            'select * from patient_info where doctor_name=%s', doctor_name)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def search_phone_no(number, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where phone_no=%s', number)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def search_date(date, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where date=%s', date)
        global patient_list
        patient_list = cur.fetchall()
        return patient_list

    def patient_Info(id, conn):
        cur = conn.cursor()
        cur.execute('select * from patient_info where patient_id=%s', id)
        global patient_list
        patient_info = cur.fetchall()
        return patient_info

    def select():
        option = filter_menu.get()
        if option == 'pat id' or option == 'Pat id':
            pat_id = search.get()
            patient_Info(pat_id, conn)
            hideAllFrames(frame)
            show_patient_info_frame.pack()
        else:
            messagebox.showwarning(
                "showwarning", "Select option only work with pat id (Patient id)")

    def deleteAll():
        for record in patient_treeView.get_children():
            patient_treeView.delete(record)

    def reset():
        deleteAll()
        connect()
        patient_treeView_body()

    def check_empty():
        if patient_list == ():
            messagebox.showwarning(
                "showwarning", "No Information Available")
            connect()

    def filter_list():
        option = filter_menu.get()
        if option == 'first name' or option == 'First Name':
            name = search.get().strip()
            if name.isalpha():
                search_name(name, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            else:
                messagebox.showwarning(
                    "showwarning", "Names should be a alphabetic character")

        elif option == 'age' or option == 'Age':
            try:
                age = int(search.get())
                search_age(age, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter integer value for age")

        elif option == 'gender' or option == 'Gender':
            gender = search.get()
            if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
                search_gender(gender, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()

            else:
                messagebox.showwarning(
                    "showwarning", "Gender Should be for Male(M) or female(F)")
                reset()

        elif option == 'blood group' or option == 'Blood group':
            blood_group = search.get()
            if blood_group == 'A+' or blood_group == 'A-' or blood_group == 'B+' or blood_group == 'B-' or blood_group == 'AB+' or blood_group == 'AB-' or blood_group == 'O' or blood_group == 'O-' or blood_group == "NA":
                search_blood_group(blood_group, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            else:
                messagebox.showwarning(
                    "showwarning", "please select a valid blood group")

        elif option == 'Dr.Name' or option == 'dr.name':
            dr_name = search.get()
            if dr_name.isascii():
                search_drName(dr_name, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            else:
                messagebox.showwarning(
                    "showwarning", "dr Names should be a Dr.name formate only")

        elif option == 'phone no.' or option == 'Phone No.':
            try:
                phone_no = int(search.get())
                search_phone_no(phone_no, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter numaric value for phone number")

        elif option == 'pat id' or option == 'pat id':
            try:
                pat_id = int(search.get())
                patient_Info(pat_id, conn)
                check_empty()
                deleteAll()
                patient_treeView_body()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter numaric value for pat id")

        elif option == 'date' or option == 'Date':
            date = search.get()
            try:
                search_date(date, conn)
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Date In This (YYYY-MM-DD) Format Only")
            deleteAll()
            patient_treeView_body()

    def patient_treeView_body():
        patient_treeView['columns'] = ("Patient First Name", "Age", "Gender", "Blood Group",
                                       "Phone Number", "Relative Name", "Doctor Name", "Digonosis", "Date")

        for i in header_list:
            patient_treeView.column(i, anchor=W, width=130, minwidth=25)

        for i in header_list:
            patient_treeView.heading(i, text=i, anchor=W)

        patient_treeView_item()

        patient_treeView.column("#0", width=0, minwidth=48)
        patient_treeView.heading("#0", text="Patient Id", anchor=W)

        patient_treeView.pack(pady=20, fill=BOTH, expand=True, padx=4)

    def patient_treeView_item():
        for i in patient_list:

            patient_treeView.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                i[1], i[4], i[5], i[6], i[7], i[9], i[17], i[18], i[20])
            )

    headerFrame = Frame(frame, bg='white')
    header = Label(headerFrame, text="Patient List",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N)
    headerFrame.pack(anchor=N, fill='x', expand=0)
    # search
    # search Frame
    search_frame = Frame(frame, bg="#7acaff", pady=7)
    search_frame.pack(fill='both', expand=0, padx=20)
    # serch entry
    search = Entry(search_frame, width=25)
    search.pack(side=LEFT)
    # filter option
    filter_menu = Combobox(search_frame, width=8)
    filter_menu['values'] = ('pat id', 'first name', 'age', 'gender', 'blood group', 'dr.name', 'date',
                             'phone no.')
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
    header_list = ["Patient First Name", "Age", "Gender", "Blood Group",
                   "Phone Number", "Relative Name", "Doctor Name", "Digonosis", "Date"]
# Treeview
    connect()
    patient_treeView = Treeview(frame)
    patient_treeView_body()
