from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter import ttk as ttk
from turtle import *
import turtle
import pymysql

# global add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame
# global manageAppointmentBtn, addAppointmentBtn, addPatientBtn, managePatientBtn


def db_connection():
    global conn
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            db='clinic',
        )
    except:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
        )
        cur = conn.cursor()
        cur.execute("create database clicic")
        cur.execute("use clicic")
    return conn


db_connection()


def hideAllFrames():
    # global frame3, frame4, frame2, frame1
    for widgets in add_patient_frame.winfo_children():
        widgets.destroy()
    for widgets in manage_patient_frame.winfo_children():
        widgets.destroy()
    for widgets in add_appointment_frame.winfo_children():
        widgets.destroy()
    for widgets in manage_appointmnet_frame.winfo_children():
        widgets.destroy()
    for widgets in show_patient_info_frame.winfo_children():
        widgets.destroy()
    add_patient_frame.pack_forget()
    manage_patient_frame.pack_forget()
    add_appointment_frame.pack_forget()
    manage_appointmnet_frame.pack_forget()
    show_patient_info_frame.pack_forget()


def addPatientBody(addPatient):
    header = Label(addPatient, text="Add Patient",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N, fill='x', expand=0)

    patient_info_frame = Frame(addPatient, bg="white", pady=10)
    patient_info_frame.pack(fill='x', expand=0, pady=10)

    patient_first_name_label = Label(patient_info_frame, text="Patient First Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_first_name_label.grid(pady=5, column=0, row=0)
    patient_first_name_entry = Entry(patient_info_frame, width=25)
    patient_first_name_entry.grid(pady=5, column=1, row=0)

    patient_middle_name_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                      text="Patient Middle Name:", width=25, bg='white')
    patient_middle_name_label.grid(pady=5, column=2, row=0)
    patient_middle_name_entry = Entry(
        patient_info_frame, width=25)
    patient_middle_name_entry.grid(pady=5, column=3, row=0)

    patient_last_name_label = Label(patient_info_frame, text="Patient Last Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_last_name_label.grid(pady=5, column=4, row=0)
    patient_last_name_entry = Entry(patient_info_frame, width=25)
    patient_last_name_entry.grid(pady=5, column=5, row=0)

    patient_age_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                              text="Age:", width=25, bg='white')
    patient_age_label.grid(pady=5, column=0, row=1)
    patient_age_entry = Entry(patient_info_frame, width=25)
    patient_age_entry.grid(pady=5, column=1, row=1)

    patient_gender_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                 text="Patient gender:", width=25, bg='white')
    patient_gender_label.grid(padx=10, column=2, row=1)
    patient_gender_combobox = Combobox(patient_info_frame, width=24)
    patient_gender_combobox['values'] = (
        'Male', 'Female', 'Transgender', 'Other')
    patient_gender_combobox.set('select gender')
    patient_gender_combobox.grid(pady=5, column=3, row=1)

    patient_bloodGroup_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                     text="Blood Group:", width=25, bg='white')
    patient_bloodGroup_label.grid(pady=5, column=4, row=1)
    patient_bloodGroup_combobox = Combobox(patient_info_frame, width=24)
    patient_bloodGroup_combobox['values'] = (
        'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O')
    patient_bloodGroup_combobox.set('select Blood Group')
    patient_bloodGroup_combobox.grid(pady=5, column=5, row=1)

    patient_contactNumber_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                        text="Patient Contact Number:", width=25, bg='white')
    patient_contactNumber_label.grid(pady=5, column=0, row=2)
    patinet_contactNumber_entry = Entry(patient_info_frame, width=25)
    patinet_contactNumber_entry.grid(pady=5, column=1, row=2)

    patient_email_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                text="Patient Email ID:", width=25, bg='white')
    patient_email_label.grid(padx=5, column=2, row=2)
    patient_email_entry = Entry(patient_info_frame, width=25)
    patient_email_entry.grid(padx=5, column=3, row=2)

    patinet_relativeName_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                       text="Relative Name:", width=25, bg='white')
    patinet_relativeName_label.grid(pady=5, column=0, row=3)
    patient_relativeName_entry = Entry(patient_info_frame, width=25)
    patient_relativeName_entry.grid(padx=5, column=1, row=3)

    patient_relativeRelation_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                           text="Relation:", width=25, bg='white')
    patient_relativeRelation_label.grid(pady=5, column=2, row=3)
    patient_relativeRelation_entry = Entry(patient_info_frame, width=25)
    patient_relativeRelation_entry.grid(padx=5, column=3, row=3)

    patinet_relativeContactNO_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                            text="Relative Contact No.", width=25, bg='white')
    patinet_relativeContactNO_label.grid(pady=5, column=0, row=4)
    patinet_relativeContactNO_entry = Entry(patient_info_frame, width=25)
    patinet_relativeContactNO_entry.grid(padx=5, column=1, row=4)

    patinet_relativeEmailId_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                          text="Relative Contact Email Id", width=25, bg='white')
    patinet_relativeEmailId_label.grid(pady=5, column=2, row=4)
    patinet_relativeEmailId_entry = Entry(patient_info_frame, width=25)
    patinet_relativeEmailId_entry.grid(padx=5, column=3, row=4)

    # Patient Address
    patient_address_info_frame = Frame(addPatient, bg="white", pady=10)
    patient_address_info_frame.pack(fill='x', expand=0)

    patient_address_label = Label(patient_address_info_frame, font=("times new roman", 16, "bold"),
                                  text="Address:", bg="white")
    patient_address_label.grid(pady=5, column=0, row=0)
    patient_address_textArea = Text(patient_address_info_frame, width=50, height=2,
                                    bg="white")
    patient_address_textArea.grid(column=1, row=0, columnspan=2)

    patient_streetName_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                     text="street name", bg="white")
    patient_streetName_label.grid(pady=2, column=0, row=1)
    patient_streetName_entry = Entry(patient_address_info_frame, width=35)
    patient_streetName_entry.grid(pady=5, column=1, row=1)

    patient_streetLine_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                     text="street line", bg="white")
    patient_streetLine_label.grid(pady=2, column=2, row=1)
    patinet_streetLine_entry = Entry(patient_address_info_frame, width=35)
    patinet_streetLine_entry.grid(pady=5, column=3, row=1)

    patinet_city_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                               text="City", bg="white")
    patinet_city_label.grid(pady=2, column=0, row=2)
    patinet_city_entry = Entry(patient_address_info_frame, width=35)
    patinet_city_entry.grid(pady=5, column=1, row=2)

    patinet_state_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                text="State", bg="white")
    patinet_state_label.grid(pady=2, column=2, row=2)
    patinet_state_entry = Entry(patient_address_info_frame, width=35)
    patinet_state_entry.grid(pady=5, column=3, row=2)

    patinet_pincode_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                  text="Pincode", bg="white")
    patinet_pincode_label.grid(pady=2, column=0, row=3)
    patinet_pincode_entry = Entry(patient_address_info_frame, width=35)
    patinet_pincode_entry.grid(pady=5, column=1, row=3)

    # dignosis frame
    digonosis_frame = Frame(addPatient, bg="white")
    # digonosis_frame.pack(fill='x', expand=0, pady=10)

    digonosis_frame.pack(fill='both', expand=1, pady=10)
    doctor_name_label = Label(digonosis_frame, text="Doctor's Name:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_name_label.grid(pady=5, column=0, row=0)
    doctor_name_combobox = Combobox(digonosis_frame, width=24)
    doctor_name_combobox['values'] = (
        'dr. abc', 'dr. xyz', 'dr. pqr', 'dr. lmn')
    doctor_name_combobox.set('select Doctor')
    doctor_name_combobox.grid(pady=5, column=1, row=0)

    doctor_digonosis_label = Label(digonosis_frame, text="Digonosis:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_digonosis_label.grid(pady=5, column=2, row=0)
    doctor_digonosis_entry = Combobox(digonosis_frame, width=24)
    doctor_digonosis_entry['values'] = (
        'abc', 'xyz', 'pqr', 'lmn')
    doctor_digonosis_entry.set('select Digonosis')
    doctor_digonosis_entry.grid(pady=5, column=3, row=0)

    patient_digonosisHistory_label = Label(digonosis_frame, text="History:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    patient_digonosisHistory_label.grid(pady=5, column=0, row=1)
    patient_digonosisHistory_textArea = Text(
        digonosis_frame, height=5, width=50)
    patient_digonosisHistory_textArea.grid(
        pady=5, column=1, row=1, columnspan=2)


def addPatient():
    # Nikhat Code
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#33A7FF')
    # addAppointmentBtn.configure(bg='#33A7FF')
    addPatientBtn.configure(bg='white')
    managePatientBtn.configure(bg='#33A7FF')
    add_patient_frame.pack(fill='both', expand=1)
    la1 = Label(add_patient_frame, text="add Patient", bg="white")
    addPatientBody(add_patient_frame)
    # la1.pack(fill="both", expand=1)


def managePatient():
    # Reyana
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#33A7FF')
    # addAppointmentBtn.configure(bg='#33A7FF')
    addPatientBtn.configure(bg='#33A7FF')
    managePatientBtn.configure(bg='white')
    manage_patient_frame.pack(fill='both', expand=1)


def addAppointment():
    # Iqra
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#33A7FF')
    addPatientBtn.configure(bg='#33A7FF')
    managePatientBtn.configure(bg='#33A7FF')
    add_appointment_frame.pack(fill='both', expand=1)

# manage Appintment Body // Zaid


def manageAppintmentBody(frame, conn):
    try:
        cur = conn.cursor()
        cur.execute("select * from appointment_list")
    except:
        cur = conn.cursor()
        cur.execute("create table appointment_list(patient_id varchar(10) primary key not null, name varchar(30) not null, age int not null, gender char not null, time time, date date, phone_no varchar(10) not null unique, doctor_name varchar(30), status boolean)")
        cur.execute("select * from appointment_list")

    def connect():
        global appointment_list
        cur.execute("select * from appointment_list")
        appointment_list = cur.fetchall()

    def search_name(name, conn):
        # reset()
        cur = conn.cursor()
        cur.execute('select * from appointment_list where name=%s', name)
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
        cur.execute('select * from appointment_list where patient_id=%s', id)
        global appointment_list
        patient_info = cur.fetchall()
        return patient_info

    def select():
        option = filter_menu.get()
        if option == 'apt id' or option == 'Apt id':
            apt_id = search.get()
            patient_Info(apt_id, conn)
            hideAllFrames()
            show_patient_info_frame.pack(fill='both', expand=1)
            patient_info_scrollBar = Scrollbar(
                show_patient_info_frame, orient="vertical")
            patient_info_scrollBar.pack(side=RIGHT, fill=Y)
            patient_info = Frame(show_patient_info_frame, bg='#33A7FF')
            appointment_id = '101'
            # print(appointment_id)

            cur = conn.cursor()
            cur.execute(
                "select * from patient_info pat, appointment_list app where app.patient_id=%s and app.patient_info_id = pat.patient_id" % appointment_id)
            global patient_info_data
            patient_info_data = cur.fetchall()
            print(patient_info_data)

            patient_info.pack(fill=X, expand=0, pady=20)
            l1 = Label(patient_info, text="Patient Id:", font=(
                "times new roman", 10, "bold"), width=25).grid(pady=5, column=1, row=1)
            e1 = Entry(patient_info, width=25)
            e1.grid(pady=5, column=2, row=1)
            e1.insert(0, patient_info_data[0][0])
            e1.configure(state='disabled')

            l2 = Label(patient_info, text="Patient First Name:", font=(
                "times new roman", 10, "bold"), width=25).grid(pady=5, column=1, row=2)
            e2 = Entry(patient_info, width=25)
            e2.grid(pady=5, column=2, row=2)
            e2.insert(0, patient_info_data[0][1])
            e2.configure(state='disabled')

            l3 = Label(patient_info, font=("times new roman", 10, "bold"),
                       text="Patient Middle Name:", width=25).grid(pady=5, column=3, row=2)
            e3 = Entry(patient_info, width=25)
            e3.grid(pady=5, column=4, row=2)
            e3.insert(0, patient_info_data[0][2])
            e3.configure(state='disabled')

            l4 = Label(patient_info, text="Patient Last Name:", font=(
                "times new roman", 10, "bold"), width=25).grid(pady=5, column=5, row=2)
            e4 = Entry(patient_info, width=25)
            e4.grid(pady=5, column=6, row=2)
            e4.insert(0, patient_info_data[0][3])
            e4.configure(state='disabled')

            l5 = Label(patient_info, font=("times new roman", 10, "bold"),
                       text="Age:", width=25).grid(pady=5, column=1, row=4)
            e5 = Entry(patient_info, width=25)
            e5.grid(pady=5, column=2, row=4)
            e5.insert(0, patient_info_data[0][4])
            e5.configure(state='disabled')

            l6 = Label(patient_info, font=("times new roman", 10, "bold"),
                       text="Patient gender:", width=25).grid(padx=10, column=3, row=4)
            # e6 = Entry(patient_info, width=25).grid(pady=5, column=4, row=4)
            filter_Genders = Combobox(patient_info, width=24)
            filter_Genders['values'] = (
                'Male', 'Female', 'Transgender', 'Other')
            filter_Genders.grid(pady=5, column=4, row=4)
            filter_Genders.insert(0, patient_info_data[0][5])
            filter_Genders.configure(state='disabled')

            l7 = Label(patient_info, font=("times new roman", 10, "bold"),
                       text="Blood Group:", width=25).grid(pady=5, column=5, row=4)
            e7 = Entry(patient_info, width=25)
            e7.grid(pady=5, column=6, row=4)
            e7.insert(0, patient_info_data[0][6])
            e7.configure(state='disabled')

            l14 = Label(patient_info, font=("times new roman", 10, "bold"),
                        text="Email ID:", width=25).grid(padx=5, column=1, row=11)
            e14 = Entry(patient_info, width=35)
            e14.grid(padx=5, column=2, row=11)
            e14.insert(0, patient_info_data[0][7])
            e14.configure(state='disabled')

            l15 = Label(patient_info, font=("times new roman", 10, "bold"),
                        text="Contact No.", width=25).grid(pady=5, column=1, row=12)
            e15 = Entry(patient_info, width=35)
            e15.grid(padx=5, column=2, row=12)
            e15.insert(0, patient_info_data[0][8])
            e15.configure(state='disabled')

            l16 = Label(patient_info, font=("times new roman", 10, "bold"),
                        text="Relative Name:", width=25).grid(pady=5, column=1, row=13)
            e16 = Entry(patient_info, width=35)
            e16.grid(padx=5, column=2, row=13)
            e16.insert(0, patient_info_data[0][9])
            e16.configure(state='disabled')

            l17 = Label(patient_info, font=("times new roman", 10, "bold"),
                        text="Relation:", width=25).grid(pady=5, column=3, row=13)
            e17 = Entry(patient_info, width=35)
            e17.grid(padx=5, column=4, row=13)
            e17.insert(0, patient_info_data[0][10])
            e17.configure(state='disabled')

            patient_address_frame = Frame(
                show_patient_info_frame, bg='#33A7CF')
            patient_address_frame.pack(fill=X, expand=0)

            l8 = Label(patient_address_frame, font=("times new roman", 10, "bold"),
                       text="Address:").grid(pady=5, column=0, row=0)
            addinputtxt = Text(patient_address_frame, width=50, height=2,
                               bg="light yellow").grid(column=1, row=0, columnspan=2)
            # e8 = Entry(patient_address_frame, width=35).grid(pady=5, column=2, row=5)

            l9 = Label(patient_address_frame, font=("Microsoft Himalaya", 15),
                       text="street name").grid(pady=2, column=0, row=1)
            e9 = Entry(patient_address_frame, width=35).grid(
                pady=5, column=1, row=1)

            l10 = Label(patient_address_frame, font=("Microsoft Himalaya", 15),
                        text="street line").grid(pady=2, column=2, row=1)
            e10 = Entry(patient_address_frame, width=35).grid(
                pady=5, column=3, row=1)

            l11 = Label(patient_address_frame, font=("Microsoft Himalaya", 15),
                        text="City").grid(pady=2, column=0, row=2)
            l11 = Entry(patient_address_frame, width=35).grid(
                pady=5, column=1, row=2)

            l12 = Label(patient_address_frame, font=("Microsoft Himalaya", 15),
                        text="State").grid(pady=2, column=2, row=2)
            e12 = Entry(patient_address_frame, width=35).grid(
                pady=5, column=3, row=2)

            l13 = Label(patient_address_frame, font=("Microsoft Himalaya", 15),
                        text="Pincode").grid(pady=2, column=0, row=3)
            e13 = Entry(patient_address_frame, width=35).grid(
                pady=5, column=1, row=3)
            # l13 = Label(patient_info, font=("times new roman", 10, "bold"),
            #             text="Email ID", width=25).grid(padx=5, column=1, row=11)

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
            name = search.get()
            if name == '':
                pass
            else:
                search_name(name, conn)
                deleteAll()
                un_seen_item()
                seen_item()
        elif option == 'age' or option == 'Age':
            try:
                age = int(search.get())
                search_age(age, conn)
                deleteAll()
                un_seen_item()
                seen_item()
            except:
                messagebox.showwarning(
                    "showwarning", "Enter integer value for age")

        elif option == 'gender' or option == 'Gender':
            gender = search.get()
            if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
                search_gender(gender, conn)
                deleteAll()
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
            name = search.get()
            if name == '' or name == ' ':
                pass
            else:
                dr_name = 'dr. ' + name
                search_dr_name(dr_name, conn)
                deleteAll()
                un_seen_item()
                seen_item()
        elif option == 'phone no.' or option == 'phone no.':
            phone_no = search.get()
            search_phone_no(phone_no, conn)
            deleteAll()
            un_seen_item()
            seen_item()
        elif option == 'apt id' or option == 'Apt id':
            apt_id = search.get()
            search_apt_id(apt_id, conn)
            deleteAll()
            un_seen_item()
            seen_item()
        else:
            messagebox.showwarning("showwarning", "NO Search Option Available")

    def un_seen_body():
        list_app['columns'] = ("Patient Name", "Age", "Gender",
                               "Time", "Date", "Phone Number", "Doctor Name", "Status")
        # placing header
        for i in header_list:
            list_app.column(i, anchor=W, width=170, minwidth=25)
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
        seen_app['columns'] = ("Patient Name", "Age", "Gender",
                               "Time", "Date", "Phone Number", "Doctor Name", "Status")
        # placing header
        for i in header_list:
            seen_app.column(i, anchor=W, width=170, minwidth=25)
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
            if i[8] == 0:
                if count % 2 == 0:
                    list_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'unseen'), tags=('evenrow',)
                    )
                else:
                    list_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'unseen'), tags=('oddrow',)
                    )
            count += 1

    def seen_item():
        counts = 0
        for i in appointment_list:
            if i[8] == 1:
                if counts % 2 == 0:
                    seen_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'seen'), tags=('evenrow')
                    )
                else:
                    seen_app.insert(parent='', index='end', iid=i[0], text=i[0], values=(
                        i[1], i[2], i[3], i[4], i[5], i[6], i[7], 'seen'), tags=('oddrow')
                    )
                counts += 1

    headerFrame = Frame(frame, bg='white')
    header = Label(headerFrame, text="Appointment List",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N)
    headerFrame.pack(anchor=N, fill='x', expand=0)
    # search
    # search Frame
    search_frame = Frame(frame, bg="#33A7FF", pady=7)
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
    addAppointmentBtn = Button(
        search_frame, text="Add Appointment", command=addAppointment)
    addAppointmentBtn.pack(side="right")
    header_list = ["Patient Name", "Age", "Gender",
                   "Time", "Date", "Phone Number", "Doctor Name", "Status"]
# Treeview
    connect()
    # unseen treeview
    list_app_frame = Frame(frame)
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
    seen_app_frame = Frame(frame)
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


def manageAppointment():
    # Zaid
    hideAllFrames()
    # changeOnHover(manageAppointmentBtn, 'white', 'red')
    manageAppointmentBtn.configure(bg='white')
    # addAppointmentBtn.configure(bg='#33A7FF')
    addPatientBtn.configure(bg='#33A7FF')
    managePatientBtn.configure(bg='#33A7FF')
    manage_appointmnet_frame.pack(fill='both', expand=1)
    manageAppintmentBody(manage_appointmnet_frame, conn)


global winTotal
winTotal = 0


def info(root):
    root.destroy()
    loginPageBody(conn)


def navBar(root):
    global manageAppointmentBtn, addAppointmentBtn, addPatientBtn, managePatientBtn
    topBar = Frame(root, bg='#33A7FF')
    title = Label(topBar, text="Clinc Management System",
                  font=("sans-serif", 10), bg='#33A7FF', fg='black')
    title.pack(side='left', padx=10)
    topBarBtn = Frame(topBar, bg='#33A7FF')
    addPatientBtn = Button(topBarBtn, text="Add Patient",
                           command=addPatient, bg='#33A7FF', pady=10)
    addPatientBtn.pack(side="left")
    managePatientBtn = Button(
        topBarBtn, text="Manage Patient", command=managePatient, bg='#33A7FF', pady=10)
    managePatientBtn.pack(side="left")
    manageAppointmentBtn = Button(
        topBarBtn, text="Manage Appointmnet", command=manageAppointment, bg='#33A7FF', pady=10)
    manageAppointmentBtn.pack(side="left")
    topBarBtn.pack(side="left", padx=20)
    profileName = Button(topBar, text="LogOut",
                         bg='#33A8FF', command=lambda: info(root))
    profileName.pack(side="right", padx=20)
    topBar.pack(side='top', fill="both", expand=0)


def body():
    global add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame, show_patient_info_frame
    clinic_body = Tk()
    clinic_body.title("Clinic Management System")
    height = clinic_body.winfo_screenheight()
    width = clinic_body.winfo_screenwidth()

    clinic_body.geometry('%dx%d+0+0' % (width, height))
    # clinic_body.state('zoomed')
    clinic_body.configure(bg='white')

    body = Frame(clinic_body)

    add_patient_frame = Frame(body, bg='#33A7FF')
    manage_patient_frame = Frame(body, bg='#55CAD4')
    add_appointment_frame = Frame(body)
    manage_appointmnet_frame = Frame(body, bg='#33A7FF')
    show_patient_info_frame = Frame(body)
    navBar(clinic_body)
    # manageAppointment()
    addPatient()
    body.rowconfigure(0, weight=1)
    body.columnconfigure(0, weight=1)

    body.pack(fill='both', expand=1)
    clinic_body.mainloop()


def hideAllLoginFrames():
    # global frame3, frame4, frame2, frame1
    for widgets in login_frame.winfo_children():
        widgets.destroy()
    for widgets in register_frame.winfo_children():
        widgets.destroy()
    for widgets in forgot_password_frame.winfo_children():
        widgets.destroy()

    login_frame.pack_forget()
    register_frame.pack_forget()
    forgot_password_frame.pack_forget()


def forgot_password(login_frame, register_frame, forgot_password_frame, conn):
    hideAllLoginFrames()
    forgot_password_frame.pack(fill='both', expand=1)
    framefp = Frame(forgot_password_frame, width=480, height=215,
                    highlightbackground="Silver", highlightthickness="2")
    framefp.place(anchor='center', relx=0.5, rely=0.5)
    # framefp.configure(bg='#7EC0F5')

    username = Label(framefp, text="Username", font=("Times new roman", 17))
    username.place(x=10, y=20)
    phoneno = Label(framefp, text="Phone No", font=("Times new roman", 17))
    phoneno.place(x=10, y=55)
    question = Label(framefp, text="Security question",
                     font=("Times new roman", 17))
    question.place(x=10, y=90)
    answer = Label(framefp, text="Your answer", font=("Times new roman", 17))
    answer.place(x=10, y=125)

    username_en = ttk.Entry(framefp, width=33)
    username_en.place(x=190, y=24)
    phoneno_en = ttk.Entry(framefp, width=33)
    phoneno_en.place(x=190, y=59)
    question_en = ttk.Combobox(framefp, width=30)
    question_en['values'] = ['select', 'What is your pet name?',
                             'What is your favourite colour?', 'What is your favourite game?']
    question_en.current(0)
    question_en.place(x=190, y=94)
    answer_en = ttk.Entry(framefp, width=33)
    answer_en.place(x=190, y=129)

    def getpwd(conn):
        name = username_en.get().strip()
        s_question = question_en.get()
        s_answer = answer_en.get()
        phone = phoneno_en.get()
        if name and s_question and s_answer and phone:
            try:
                phone = int(phone)
                cur = conn.cursor()
                cur.execute("select * from login where username=%s", name)
                data = cur.fetchall()
                if data == ():
                    messagebox.showerror("Error", "Username is Not Valid!")
                else:
                    # print(data)
                    # print(name == data[0][0] and phone == data[0][5]
                    #       and s_question == data[0][6] and s_answer == data[0][7])
                    phone = str(phone)
                    if name == data[0][0] and phone == data[0][5] and s_question == data[0][6] and s_answer == data[0][7]:
                        password = data[0][1]
                        messagebox.showinfo(
                            "Get Password", "Your Password is '"+password+"'.")
                    else:
                        messagebox.showerror(
                            "Error", "Please Fill the Correct Information2")
            except:
                messagebox.showerror(
                    "Error", "Phone Number Should be an Integer Value")
        else:
            messagebox.showerror(
                "Error", "Something is Empty.")

        conn.commit()

    global a
    a = 1

    def chpwd(conn):
        name = username_en.get().strip()
        s_question = question_en.get()
        s_answer = answer_en.get()
        phone = phoneno_en.get()
        try:
            cur = conn.cursor()
            cur.execute("select * from login where username=%s", name)
            data = cur.fetchall()
            if data == ():
                print("username is not valid!")
            else:
                if (name == data[0][0] and phone == data[0][5]) and (s_question == data[0][6] and s_answer == data[0][7]):
                    global a
                    if a < 2:
                        win1 = Toplevel()
                        win1.title("Change password")
                        appwidth = 500
                        appheight = 500
                        scwidth = win1.winfo_screenwidth()
                        scheight = win1.winfo_screenheight()
                        x = (scwidth/2)-(appwidth/2)
                        y = (scheight/2)-(appheight/2)
                        win1.geometry(
                            f'{appwidth}x{appheight}+{int(x)}+{int(y)}')
                        win1.minsize(500, 500)
                        win1.maxsize(500, 500)

                        frame = Frame(win1, width=300, height=200,
                                      highlightbackground="Silver", highlightthickness="2")
                        frame.place(anchor="center", relx=0.5, rely=0.5)

                        newpass = Label(frame, text="New password",
                                        font=("Times new roman", 14))
                        c_pass = Label(frame, text="Confirm password",
                                       font=("Times new roman", 14))
                        newpass_en = ttk.Entry(frame)
                        c_pass_en = ttk.Entry(frame)

                        newpass.place(x=14, y=20)
                        c_pass.place(x=14, y=55)
                        newpass_en.place(x=160, y=23)
                        c_pass_en.place(x=160, y=58)

                        def ch(conn):
                            password = str(newpass_en.get().strip())
                            c_password = str(c_pass_en.get().strip())
                            try:
                                if password == c_password:
                                    name = str(username_en.get())
                                    sql = "update login set password=%s where username=%s"
                                    value = (password, name)
                                    cur.execute(sql, value)
                                    conn.commit()
                                    messagebox.showinfo("Done", "Successfull!")
                                    win1.destroy()
                                    # forgot_password_frame.destroy()
                                    login(login_frame, register_frame,
                                          forgot_password_frame, conn)
                                else:
                                    messagebox.showerror(
                                        "Invalid", "Check your password!")
                            except:
                                messagebox.showerror(
                                    "Invalid", "Check your password!")

                        btn = Button(frame, text="Update",
                                     command=lambda: ch(conn))
                        btn.place(x=190, y=165)
                        win1.mainloop()
                    else:
                        messagebox.showwarning(
                            "Error", "You have already opened a window!")
                else:
                    messagebox.showerror(
                        "Error", "Username or password is not valid!")
        except:
            messagebox.showerror("DataError", "Data is invalid!")

    btn1 = ttk.Button(framefp, cursor='hand2', text='GET PASSWORD',
                      command=lambda: getpwd(conn))
    btn1.place(x=50, y=165)
    btn2 = ttk.Button(framefp, cursor='hand2',
                      text='CHANGE PASSWORD', command=lambda: chpwd(conn))
    btn2.place(x=233, y=165)


def register(login_frame, register_frame, forgot_password_frame, conn):
    hideAllLoginFrames()
    register_frame.pack(fill='both', expand=1)
    frame = Frame(register_frame, width=550, height=500,
                  highlightbackground="Silver", highlightthickness="2")

    frame.place(anchor="center", relx=0.5, rely=0.5)

    username_ = Label(frame, text="Username", font=("Times new roman", 20))
    username_.place(x=14, y=70)
    _username = ttk.Entry(frame, width=35)
    _username.place(x=240, y=78)
    password_ = Label(frame, text="Password", font=("Times new roman", 20))
    password_.place(x=14, y=110)
    _password = ttk.Entry(frame, width=35)
    _password.place(x=240, y=118)
    name_ = Label(frame, text="Name", font=("Times new roman", 20))
    name_.place(x=14, y=150)
    _name = ttk.Entry(frame, width=35)
    _name.place(x=240, y=158)
    age_ = Label(frame, text="Age", font=("Times new roman", 20))
    age_.place(x=14, y=190)
    _age = ttk.Entry(frame, width=35)
    _age.place(x=240, y=198)
    gender_ = Label(frame, text="Gender", font=("Times new roman", 20))
    gender_.place(x=14, y=230)
    _gender = IntVar()
    R1 = Radiobutton(frame,
                     text="Male",
                     font=("Times new roman", 14),
                     variable=_gender,
                     value=1)
    R1.place(x=235, y=233)
    R2 = Radiobutton(frame,
                     text="Female",
                     font=("Times new roman", 14),
                     variable=_gender,
                     value=2)
    R2.place(x=320, y=233)
    phoneno_ = Label(frame, text="Phone no", font=("Times new roman", 20))
    phoneno_.place(x=14, y=270)
    _phone_no = ttk.Entry(frame, width=35)
    _phone_no.place(x=240, y=278)
    s_question_ = Label(frame, text="Security question",
                        font=("Times new roman", 20))
    s_question_.place(x=14, y=310)
    _security_question = ttk.Combobox(frame, width=32)
    _security_question['values'] = ['What is your pet name?',
                                    'What is your favourite colour?', 'What is your favourite game?']
    _security_question.set('Filter')
    # _security_question.current(0)
    _security_question.place(x=240, y=318)
    s_answer_ = Label(frame, text="Security answer",
                      font=("Times new roman", 20))
    s_answer_.place(x=14, y=350)
    _security_answer = ttk.Entry(frame, width=35)
    _security_answer.place(x=240, y=358)

    def check_register(conn):
        username = _username.get().strip()
        password = _password.get()
        name = _name.get().strip()
        gender = _gender.get()
        security_answer = _security_answer.get().strip()
        security_question = _security_question.get().strip()
        age = str(_age.get())
        phone_no = str(_phone_no.get())
        if username and password and name and age and gender and phone_no and security_question and security_answer:
            try:
                age = int(_age.get())
                phone_no = int(_phone_no.get())
                age = str(age)
                phone_no = str(phone_no)
                if len(password) > 7:
                    if len(phone_no) == 10:
                        if security_question == 'What is your pet name?' or security_question == 'What is your favourite colour?' or security_question == 'What is your favourite game?':
                            try:
                                isTaken = False
                                cur = conn.cursor()
                                cur.execute("select username from login")
                                data = cur.fetchall()
                                print(data)
                                for i in data:
                                    for k in i:
                                        if k == username:
                                            messagebox.showerror(
                                                "Error", "user name is already taken")
                                            isTaken = True
                                if isTaken == False:
                                    columns = "insert into login(username,password,name,age,gender,phone_no,security_question,security_answer) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                    values = (username, password, name, age, gender,
                                              phone_no, security_question, security_answer)
                                    cur.execute(columns, values)
                                    messagebox.showinfo("Done", "Successfull!")
                                    login(login_frame, register_frame,
                                          forgot_password_frame, conn)
                                    conn.commit()
                                else:
                                    pass
                            except:
                                print("hello world!")
                                cur = conn.cursor()
                                cur.execute(
                                    "create table login(username varchar(30) primary key,password varchar(30) not null,name varchar(30) not null,age int not null,gender varchar(20) not null,phone_no varchar(10) not null,security_question varchar(70) not null,security_answer varchar(70) not null)")
                                columns = "insert into login(username,password,name,age,gender,phone_no,security_question,security_answer) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                values = (username, password, name, age, gender,
                                          phone_no, security_question, security_answer)
                                cur.execute(columns, values)
                                messagebox.showinfo("Done", "Successfull!")
                                conn.commit()
                                login(login_frame, register_frame,
                                      forgot_password_frame, conn)
                        else:
                            messagebox.showerror(
                                "Error", "Security Question Wrong.")
                    else:
                        messagebox.showerror("Error", "Phone Number is Wrong.")
                else:
                    messagebox.showerror(
                        "Error", "Password Should be at least 8 Characters.")
            except ValueError:
                messagebox.showerror(
                    "Error", "Age and Phone Number Should be an Number Value")
        else:
            messagebox.showerror(
                "Error", "Something is Empty.")

    btn1 = ttk.Button(frame, cursor="hand2", text="Exit",
                      command=lambda: login(login_frame, register_frame, forgot_password_frame, conn))
    btn1.place(x=398, y=0)
    btn2 = ttk.Button(frame, cursor="hand2",
                      text="                  Register                   ", command=lambda: check_register(conn))
    btn2.place(x=150, y=400)


def login(login_frame, register_frame, forgot_password_frame, conn):
    hideAllLoginFrames()
    login_frame.pack(fill='both', expand=1)
    title = Label(login_frame, text="Login Page", font=(
        "Times new roman", 30), foreground="SkyBlue3")
    title.place(x=155, y=80)

    frame = Frame(login_frame, width=420, height=340,
                  highlightbackground="Silver", highlightthickness="2")
    frame.place(anchor="center", relx=0.5, rely=0.5)

    title = Label(frame, text="Login", font=(
        "Times new roman", 30), foreground="SkyBlue3")
    title.place(x=0, y=0, anchor="center", relx=0.5, rely=0.1)

    username = Label(frame, text="Username", font=("Times new roman", 20))
    username.place(x=12, y=110)
    userentry = ttk.Entry(frame, width=30)
    userentry.place(x=150, y=117)

    password = Label(frame, text="Password", font=("Times new roman", 20))
    password.place(x=12, y=150)
    passentry = ttk.Entry(frame, width=30, show="•")
    passentry.place(x=150, y=157)

    fgpass = Button(frame, cursor='hand2', text="Forgot password?",
                    foreground="Red", command=lambda: forgot_password(login_frame, register_frame, forgot_password_frame, conn), relief="flat")
    fgpass.place(x=9, y=250)

    redg = Button(frame, cursor='hand2', text="Don't have an account,Register?",
                  foreground="Green", command=lambda: register(login_frame, register_frame, forgot_password_frame, conn), relief="flat")
    redg.place(x=160, y=250)

    def check_login(conn):
        name = userentry.get()
        password = passentry.get()
        cur = conn.cursor()
        cur.execute("select * from login where username=%s", name)
        data = cur.fetchall()
        if name:
            if data == ():
                messagebox.showerror("Error", "Username is not valid!")
                userentry.delete(0, END)
                # e1.insert(0, patient_info_data[0][0])
            else:
                if (name == data[0][0] and password == data[0][1]):
                    win.destroy()
                    body()
                else:
                    messagebox.showerror(
                        "Error", "password is not valid!")
                    passentry.delete(0, END)
        else:
            pass
    submit = ttk.Button(frame, cursor='hand2',
                        text="LOGIN", command=lambda: check_login(conn))
    submit.place(x=12, y=200)


def loginPageBody(conn):
    # zeeshan
    global win
    global login_frame, register_frame, forgot_password_frame
    win = Tk()
    win.title("Login")
    height = win.winfo_screenheight()
    width = win.winfo_screenwidth()
    win.geometry("%dx%d+0+0" % (width, height))
    login_frame = Frame(win)
    register_frame = Frame(win)
    forgot_password_frame = Frame(win)
    login(login_frame, register_frame, forgot_password_frame, conn)
    win.mainloop()


def logo():
    twin = turtle.Screen()
    twin.setup(width=1.0, height=1.0, startx=None, starty=None)
    t = turtle.Turtle()
    turtle.title("Clinic")
    t.penup()
    t.goto(-12, -445)
    t.write("Please wait", move=False, align='center',
            font=('Times new roman', 25, 'normal'))
    t.penup()
    t.goto(61, -443)
    for i in range(4):
        t.write("."*i, move=False, font=('Times new roman', 19, 'normal'))
    t.shape("circle")
    t.pencolor("red")
    t.pensize(17)
    t.penup()
    t.hideturtle()
    t.goto(150, 15)
    t.pendown()
    t.begin_fill()
    t.speed(1)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(250)
    t.pencolor("black")
    t.pencolor("red")
    t.stamp()
    t.penup()
    t.hideturtle()
    t.goto(-150, -65)
    t.pendown()
    t.pencolor("black")
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(250)
    t.pencolor("red")
    t.pencolor("black")
    t.stamp()
    t.penup()
    turtle.clear()
    turtle.bye()
    loginPageBody(conn)


# logo()
# loginPageBody(conn)
body()
conn.close()
