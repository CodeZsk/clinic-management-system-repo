from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview
import pymysql

global add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame
global manageAppointmentBtn, addAppointmentBtn, addPatientBtn, managePatientBtn

conn = pymysql.connect(
    host='localhost',
    user='root',
    password="root",
    db='clinic',
)


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
    add_patient_frame.pack_forget()
    manage_patient_frame.pack_forget()
    add_appointment_frame.pack_forget()
    manage_appointmnet_frame.pack_forget()


def addPatient():
    # Nikhat Code
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#D2042D')
    addAppointmentBtn.configure(bg='#D2042D')
    addPatientBtn.configure(bg='white')
    managePatientBtn.configure(bg='#D2042D')
    add_patient_frame.pack(fill='both', expand=1)
    la1 = Label(add_patient_frame, text="add Patient", bg="white")
    la1.pack(fill="both", expand=1)


def managePatient():
    # Iqra
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#D2042D')
    addAppointmentBtn.configure(bg='#D2042D')
    addPatientBtn.configure(bg='#D2042D')
    managePatientBtn.configure(bg='white')
    manage_patient_frame.pack(fill='both', expand=1)
    la2 = Label(manage_patient_frame, text="manage Patient", bg="white")
    la2.pack(fill="both", expand=1)


def addAppointment():
    # Reyana
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#D2042D')
    addAppointmentBtn.configure(bg='white')
    addPatientBtn.configure(bg='#D2042D')
    managePatientBtn.configure(bg='#D2042D')
    add_appointment_frame.pack(fill='both', expand=1)
    la3 = Label(add_appointment_frame, text="add Appointment", bg="white")
    la3.pack(fill="both", expand=1)

# manage Appintment Body // Zaid


def manageAppintmentBody(frame, conn):
    try:
        def connect():
            cur = conn.cursor()
            cur.execute("select * from appointment_list")
            global appointment_list
            appointment_list = cur.fetchall()

    except:
        def connect():
            cur = conn.cursor()
            cur.execute("create table appointment_list(patient_id varchar(10) primary key not null, name varchar(30) not null, age int not null, gender char not null, time time, date date, phone_no varchar(10) not null unique, doctor_name varchar(30), status boolean")
            cur.execute("select * from appointment_list")
            global appointment_list
            appointment_list = cur.fetchall()

    def search_name(name, conn):
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

    def deleteAll():
        for record in list_app.get_children():
            list_app.delete(record)

    def reset():
        deleteAll()
        connect()
        List_body()

    def filter_list():
        option = filter_menu.get()
        if option == 'name' or option == 'Name':
            name = search.get()
            search_name(name, conn)
            deleteAll()
            item()
        elif option == 'age' or option == 'Age':
            try:
                age = int(search.get())
                search_age(age, conn)
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
            if gender == 'M' or gender == 'm' or gender == 'F' or gender == 'f':
                search_gender(gender, conn)
                deleteAll()
                item()
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
            item()
        elif option == 'time' or option == 'Time':
            time = search.get()
            try:
                search_time(time, conn)
            except:
                messagebox.showwarning(
                    "showwarning", "Enter Time In This (HH:MM:SS) Format Only")
            deleteAll()
            item()
        elif option == 'dr. name' or option == 'Dr. Name':
            name = search.get()
            dr_name = 'dr. ' + name
            print(dr_name)
            search_dr_name(dr_name, conn)
            deleteAll()
            item()
        elif option == 'phone no.' or option == 'phone no.':
            phone_no = search.get()
            search_phone_no(phone_no, conn)
            deleteAll()
            item()
        else:
            messagebox.showwarning("showwarning", "NO Search Option Available")

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

    def item():
        srNo = 1
        count = 0
        for i in appointment_list:
            list_app.insert(parent='', index='end', iid=count, text=srNo, values=(
                i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
            )
            count += 1
            srNo += 1
    headerFrame = Frame(frame, bg='white')
    header = Label(headerFrame, text="Appointment List",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N)
    headerFrame.pack(anchor=N, fill='x', expand=0)
    # search
    # search Frame
    search_frame = Frame(frame, bg="#D2042D", pady=7)
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
    # search btn
    search_btn = Button(search_frame, text="Search", command=filter_list)
    search_btn.pack(side=LEFT, padx=7)
    # reset btn
    reset_btn = Button(search_frame, text='Reset', command=reset)
    reset_btn.pack(side=LEFT, padx=6)
    header_list = ["Patient Name", "Age", "Gender",
                   "Time", "Date", "Phone Number", "Doctor Name", "Status"]
# Treeview
    connect()
    global list_app
    list_app = Treeview(frame)
    List_body()
    pass


def manageAppointment():
    # Zaid
    hideAllFrames()
    # changeOnHover(manageAppointmentBtn, 'white', 'red')
    manageAppointmentBtn.configure(bg='white')
    addAppointmentBtn.configure(bg='#D2042D')
    addPatientBtn.configure(bg='#D2042D')
    managePatientBtn.configure(bg='#D2042D')
    manage_appointmnet_frame.pack(fill='both', expand=1)
    manageAppintmentBody(manage_appointmnet_frame, conn)


def navBar(root):
    global manageAppointmentBtn, addAppointmentBtn, addPatientBtn, managePatientBtn
    topBar = Frame(root, bg='#D2042D')
    title = Label(topBar, text="Clinc Management System",
                  font=("sans-serif", 10), bg='#D2042D', fg='black')
    title.pack(side='left', padx=10)
    topBarBtn = Frame(topBar, bg='#D2042D')
    addPatientBtn = Button(topBarBtn, text="Add Patient",
                           command=addPatient, bg='#D2042D', pady=10)
    addPatientBtn.pack(side="left")
    managePatientBtn = Button(
        topBarBtn, text="Manage Patient", command=managePatient, bg='#D2042D', pady=10)
    managePatientBtn.pack(side="left")
    addAppointmentBtn = Button(
        topBarBtn, text="Add Appointment", command=addAppointment, bg='#D2042D', pady=10)
    addAppointmentBtn.pack(side="left")
    manageAppointmentBtn = Button(
        topBarBtn, text="Manage Appointmnet", command=manageAppointment, bg='#D2042D', pady=10)
    manageAppointmentBtn.pack(side="left")
    topBarBtn.pack(side="left", padx=20)
    profileName = Button(topBar, text="Profile Name", bg='#D2042D')
    profileName.pack(side="right", padx=20)
    topBar.pack(side='top', fill="both", expand=0)


def body():
    global add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame
    clinic_body = Tk()
    clinic_body.title("Clinic Management System")
    clinic_body.geometry('700x600')
    clinic_body.configure(bg='white')

    body = Frame(clinic_body)

    add_patient_frame = Frame(body)
    manage_patient_frame = Frame(body)
    add_appointment_frame = Frame(body)
    manage_appointmnet_frame = Frame(body, bg='#D2042D')
    navBar(clinic_body)
    manageAppointment()
    body.rowconfigure(0, weight=1)
    body.columnconfigure(0, weight=1)

    body.pack(fill='both', expand=1)
    clinic_body.mainloop()


def loginPage():
    win = Tk()
    win.title("Login")
    win.geometry("500x500")

    title = Label(win, text="Login Page", font=(
        "Times new roman", 30), foreground="SkyBlue3")
    title.place(x=155, y=80)

    frame = Frame(win, width=500, height=500,
                  highlightbackground="Silver", highlightthickness="2")
    frame.place(anchor="center", relx=0.5, rely=0.5)

    fakelbl1 = Label(frame)
    fakelbl1.grid(column=3, row=0)
    fakelbl2 = Label(frame)
    fakelbl2.grid(column=3, row=1)
    fakelbl4 = Label(frame)
    fakelbl4.grid(column=3, row=10)
    fakelbl5 = Label(frame)
    fakelbl5.grid(column=3, row=4)
    fakelbl6 = Label(frame)
    fakelbl6.grid(column=3, row=6)

    username = Label(frame, text="Username", font=("sans-serif", 15))
    username.grid(column=3, row=3)
    userentry = Entry(frame, width=30)
    userentry.grid(column=5, row=3)

    password = Label(frame, text="Password", font=("sans-serif", 15))
    password.grid(column=3, row=5)
    passentry = Entry(frame, width=30, show="•")
    passentry.grid(column=5, row=5)
    fakelabe3 = Label(frame)

    fakelabe3.grid(column=3, row=8)
    fgpass = Button(frame, text="Forgot password?", foreground="Red",
                    command=lambda: win.destroy(), relief="flat")
    fgpass.grid(column=3, row=9)

    redg = Button(frame, text="      Don't have an account,Register?      ",
                  foreground="Green", command=win.destroy, relief="flat")
    redg.grid(column=5, row=9)

    submit = Button(frame, text="LOGIN", font=("sans-serif", 10), fg="DarkBlue",
                    command=lambda: handelSubmit(userentry, passentry, win), relief="raised")
    submit.grid(column=5, row=7)
    win.mainloop()


def handelSubmit(username, password, root):
    name = username.get()
    passWord = password.get()
    if passWord == "root" and name == "root":
        root.destroy()
        body()
    else:
        pass


loginPage()
# body()
conn.close()
