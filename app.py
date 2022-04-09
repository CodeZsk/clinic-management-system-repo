from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter import ttk as ttk
from turtle import *
from PIL import ImageTk, Image
import turtle
import pymysql
from addPatient import addPatientBody
from managePatient import managePatientBody
from manageAppointment import manageAppointmentBody
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
            autocommit=True
        )
    except:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="root",
            autocommit=True
        )
        cur = conn.cursor()
        cur.execute("create database clicic")
        cur.execute("use clicic")
    # return conn


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
    for widgets in show_patient_Appointment_info_frame.winfo_children():
        widgets.destroy()
    add_patient_frame.pack_forget()
    manage_patient_frame.pack_forget()
    add_appointment_frame.pack_forget()
    manage_appointmnet_frame.pack_forget()
    show_patient_info_frame.pack_forget()
    show_patient_Appointment_info_frame.pack_forget()


def addPatient():
    # Nikhat Code
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#7acaff')
    # addAppointmentBtn.configure(bg='#7acaff')
    addPatientBtn.configure(bg='white')
    managePatientBtn.configure(bg='#7acaff')
    add_patient_frame.pack(fill='both', expand=1)
    # la1 = Label(add_patient_frame, text="add Patient", bg="white")
    addPatientBody(add_patient_frame, conn)


def managePatient():
    # Reyana
    hideAllFrames()
    manageAppointmentBtn.configure(bg='#7acaff')
    # addAppointmentBtn.configure(bg='#7acaff')
    addPatientBtn.configure(bg='#7acaff')
    managePatientBtn.configure(bg='white')
    manage_patient_frame.pack(fill='both', expand=1)
    managePatientBody(manage_patient_frame, show_patient_info_frame, conn)


def manageAppointment():
    # Zaid
    hideAllFrames()
    # changeOnHover(manageAppointmentBtn, 'white', 'red')
    manageAppointmentBtn.configure(bg='white')
    # addAppointmentBtn.configure(bg='#7acaff')
    addPatientBtn.configure(bg='#7acaff')
    managePatientBtn.configure(bg='#7acaff')
    manage_appointmnet_frame.pack(fill='both', expand=1)
    manageAppointmentBody(add_patient_frame, manage_patient_frame, add_appointment_frame,
                          manage_appointmnet_frame, show_patient_info_frame, show_patient_Appointment_info_frame, conn)


global winTotal
winTotal = 0


def info(root):
    if messagebox.askokcancel("Quit", "Do you want to logOut?"):
        root.destroy()
        loginPageBody(conn)


def navBar(root):
    global manageAppointmentBtn, addAppointmentBtn, addPatientBtn, managePatientBtn
    topBar = Frame(root, bg='#7acaff')
    title = Label(topBar, text="Clinc Management System",
                  font=("sans-serif", 10), bg='#7acaff', fg='black')
    title.pack(side='left', padx=10)
    topBarBtn = Frame(topBar, bg='#7acaff')
    addPatientBtn = Button(topBarBtn, text="Add Patient",
                           command=addPatient, bg='#7acaff', pady=10)
    addPatientBtn.pack(side="left")
    managePatientBtn = Button(
        topBarBtn, text="Manage Patient", command=managePatient, bg='#7acaff', pady=10)
    managePatientBtn.pack(side="left")
    manageAppointmentBtn = Button(
        topBarBtn, text="Manage Appointmnet", command=manageAppointment, bg='#7acaff', pady=10)
    manageAppointmentBtn.pack(side="left")
    topBarBtn.pack(side="left", padx=20)
    profileName = Button(topBar, text="LogOut",
                         bg='#7acaff', command=lambda: info(root))
    profileName.pack(side="right", padx=20)
    topBar.pack(side='top', fill="both", expand=0)


def body():
    global add_patient_frame, manage_patient_frame, add_appointment_frame, manage_appointmnet_frame, show_patient_info_frame, show_patient_Appointment_info_frame
    clinic_body = Tk()
    clinic_body.title("Clinic Management System")
    height = clinic_body.winfo_screenheight()
    width = clinic_body.winfo_screenwidth()

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            clinic_body.destroy()

    clinic_body.protocol("WM_DELETE_WINDOW", on_closing)

    clinic_body.geometry('%dx%d+0+0' % (width, height))
    # clinic_body.state('zoomed')
    clinic_body.configure(bg='white')

    body = Frame(clinic_body)

    add_patient_frame = Frame(body, bg='#7acaff')
    manage_patient_frame = Frame(body, bg='#7acaff')
    add_appointment_frame = Frame(body, bg='#7acaff')
    manage_appointmnet_frame = Frame(body, bg='#7acaff')
    show_patient_info_frame = Frame(body, bg='#7acaff')
    show_patient_Appointment_info_frame = Frame(body, bg='#7acaff')
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
        s_question = question_en.get().strip()
        s_answer = answer_en.get().strip()
        phone = phoneno_en.get()
        try:
            cur = conn.cursor()
            cur.execute("select * from login where username=%s", name)
            data = cur.fetchall()
            if data == ():
                messagebox.showerror(
                    "Error", "Username is not valid!")
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

    image = "img/istockphoto-1168823446-170667a.jpg"
    # resized = image.resize((width, height), Image.ANTIALIAS)
    img = PhotoImage(image)
    label = Label(
        login_frame,
        image=img
    )
    label.pack()
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
    # bg image
    canvas = Canvas(win, width=width, height=height, bg="white")
    # canvas.pack(fill="both", expand=1)
    # img = ImageTk.PhotoImage(file="img/istockphoto-1168823446-170667a.jpg")
    # canvas.create_image(0, 0, image=img, anchor=NW)
    # resize

    def resize_image(e):
        global image, resized, image2

        image = "img/istockphoto-1168823446-170667a.jpg"
        resized = image.resize((e.width+1, e.height+1), Image.ANTIALIAS)
        image2 = ImageTk.PhotoImage(resized)
        canvas.create_image(0, 0, image=image2, anchor='nw')
    # Bind the function to configure the parent window
    # win.bind("<Configure>", resize_image)

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
# conn.close()
