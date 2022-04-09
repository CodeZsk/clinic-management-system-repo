from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar
from datetime import datetime, date


def updateAppointmentBody(frame, conn, apt_id):
    cur = conn.cursor()
    cur.execute(
        "select * from appointment_list where appointment_id=%s " % apt_id)
    global patient_info_data
    patient_info_data = cur.fetchall()
    print(patient_info_data)

    pageTitle = Label(frame,
                      text="Appointment Information", bg="white")
    pageTitle.pack(expand=0, fill=X)

    patient_info_frame = Frame(
        frame, bg="white", pady=10)
    patient_info_frame.pack(fill='x', expand=0, pady=10)

    patient_id_label = Label(patient_info_frame, text="Patient Id:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_id_label.grid(pady=5, column=0, row=0)
    patient_id_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_id_entry.grid(
        pady=5, column=1, row=0)
    patient_id_entry.insert(0, patient_info_data[0][0])
    patient_id_entry.configure(state='disabled')

    patient_first_name_label = Label(patient_info_frame, text="Patient First Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_first_name_label.grid(pady=5, column=0, row=1)
    patient_first_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_first_name_entry.grid(
        pady=5, column=1, row=1)
    patient_first_name_entry.insert(0, patient_info_data[0][1])
    patient_first_name_entry.configure(state='disabled')

    patient_middle_name_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                      text="Patient Middle Name:", width=25, bg='white')
    patient_middle_name_label.grid(pady=5, column=2, row=1)
    patient_middle_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_middle_name_entry.grid(
        pady=5, column=3, row=1)
    patient_middle_name_entry.insert(0, patient_info_data[0][2])
    patient_middle_name_entry.configure(state='disabled')

    patient_last_name_label = Label(patient_info_frame, text="Patient Last Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_last_name_label.grid(pady=5, column=4, row=1)
    patient_last_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_last_name_entry.grid(pady=5, column=5, row=1)
    patient_last_name_entry.insert(0, patient_info_data[0][3])
    patient_last_name_entry.configure(state='disabled')

    patient_age_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                              text="Age:", width=25, bg='white')
    patient_age_label.grid(pady=5, column=0, row=2)
    patient_age_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_age_entry.grid(pady=5, column=1, row=2)
    patient_age_entry.insert(0, patient_info_data[0][4])
    patient_age_entry.configure(state='disabled')

    patient_gender_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                 text="Patient gender:", width=25, bg='white')
    patient_gender_label.grid(padx=10, column=2, row=2)
    patient_gender_combobox = Combobox(
        patient_info_frame, width=24)
    patient_gender_combobox['values'] = (
        'Male', 'Female', 'Transgender', 'Other')
    patient_gender_combobox.set('select gender')
    patient_gender_combobox.grid(
        pady=5, column=3, row=2)
    patient_gender_combobox.delete(0, END)
    patient_gender_combobox.insert(0, patient_info_data[0][5])
    patient_gender_combobox.configure(state='disabled')

    patient_bloodGroup_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                     text="Blood Group:", width=25, bg='white')
    patient_bloodGroup_label.grid(pady=5, column=4, row=2)
    patient_bloodGroup_combobox = Combobox(
        patient_info_frame, width=24)
    patient_bloodGroup_combobox['values'] = (
        'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-')
    patient_bloodGroup_combobox.set('select Blood Group')
    patient_bloodGroup_combobox.grid(pady=5, column=5, row=2)
    patient_bloodGroup_combobox.delete(0, END)
    patient_bloodGroup_combobox.insert(0, patient_info_data[0][6])
    patient_bloodGroup_combobox.configure(state='disabled')

    patient_contactNumber_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                        text="Patient Contact Number:", width=25, bg='white')
    patient_contactNumber_label.grid(pady=5, column=0, row=3)
    patinet_contactNumber_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patinet_contactNumber_entry.grid(pady=5, column=1, row=3)
    patinet_contactNumber_entry.insert(0, patient_info_data[0][7])
    patinet_contactNumber_entry.configure(state='disabled')

    patient_email_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                text="Patient Email ID:", width=25, bg='white')
    patient_email_label.grid(padx=5, column=2, row=3)
    patient_email_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_email_entry.grid(padx=5, column=3, row=3)
    patient_email_entry.insert(0, patient_info_data[0][8])
    patient_email_entry.configure(state='disabled')

    digonosis_frame = Frame(frame, bg="white")
    # digonosis_frame.pack(fill='x', expand=0, pady=10)

    digonosis_frame.pack(fill='both', expand=1, pady=10)
    doctor_name_label = Label(digonosis_frame, text="Doctor's Name:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_name_label.grid(pady=5, column=0, row=0)
    doctor_name_combobox = Combobox(digonosis_frame, width=24)
    doctor_name_combobox['values'] = ('Dr.Azam(Allergists)', 'Dr.Raj(Anesthesiologists)', 'Dr.Vikas(Cardiologists)', 'Dr.Kamad(Dermatologists)', 'Dr.Sakina(gynaecologist)',
                                      'Dr.Danish(Genral Surgen)', 'Dr.Jateen(Nephrologists)', 'Dr.Tahira(Oncologists)', 'Dr.Arham(Orthopedic)', 'Dr.Zoha(Pediatricians)')
    doctor_name_combobox.grid(pady=5, column=1, row=0)
    doctor_name_combobox.insert(0, patient_info_data[0][9])
    doctor_name_combobox.configure(state='disabled')

    doctor_digonosis_label = Label(digonosis_frame, text="Digonosis:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_digonosis_label.grid(pady=5, column=2, row=0)
    doctor_digonosis_entry = Entry(
        digonosis_frame, width=24, borderwidth=1, relief="solid")
    doctor_digonosis_entry.grid(pady=5, column=3, row=0)
    doctor_digonosis_entry.insert(0, patient_info_data[0][10])
    doctor_digonosis_entry.configure(state='disabled')

    todayDate = date.today()
    month = todayDate.month
    day = todayDate.day
    year = todayDate.year

    selectDateLabel = Label(digonosis_frame, text="Select Date:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    selectDateLabel.grid(pady=5, column=0, row=1)
    # selectDateEntry.configure(state='disabled')

    cal = Calendar(digonosis_frame, selectmode='day',
                   year=year, month=month, day=day)

    cal.grid(pady=5, column=1, row=2)

    selectDateLa = Label(digonosis_frame, text=cal.get_date())
    # dateselectDateLaLa.grid(pady=5, column=3, row=0)
    selectDateLa.grid(pady=5, column=1, row=1)

    global selectDate
    selectDate = ''

    def grad_date():
        selectDateLa.config(text="Selected Date is: " + cal.get_date())
        selectDate = cal.get_date()
    # Add Button and Label
    Button(digonosis_frame, text="Get Date",
           command=grad_date).grid(pady=5, column=1, row=3)

    patient_Time_label = Label(digonosis_frame, font=("times new roman", 13, "bold"),
                               text="Select Time:", width=25, bg='white')
    patient_Time_label.grid(pady=5, column=2, row=1)
    patinet_Time_entry = Entry(
        digonosis_frame, width=25, borderwidth=1, relief="solid")
    patinet_Time_entry.grid(pady=5, column=3, row=1)

    patient_Time_label = Label(digonosis_frame, font=("times new roman", 13, "bold"),
                               text="Select Status:", width=25, bg='white')
    patient_Time_label.grid(pady=5, column=4, row=1)
    status_combobox = Combobox(
        digonosis_frame, width=24)
    status_combobox['values'] = (
        'Unseen', 'Seen', 'Cancelled')
    status_combobox.set('Unseen')
    status_combobox.grid(pady=5, column=5, row=1)

    def callback():
        id = patient_id_entry
        first_name = patient_first_name_entry.get()
        middle_name = patient_middle_name_entry.get()
        last_name = patient_last_name_entry.get()
        age = patient_age_entry.get()
        gender = patient_gender_combobox.get()
        blood_group = patient_bloodGroup_combobox.get()
        phone = patinet_contactNumber_entry.get()
        email = patient_email_entry.get()
        doctor = doctor_name_combobox.get()
        digonosis = doctor_digonosis_entry.get()
        time = patinet_Time_entry.get()
        date = selectDate
        status = status_combobox.get()
        if date and time and status:
            if status == 'Seen' or status == 'Unseen' or status == 'Cancelled':
                # "create table appointment_list(appointment_id int primary key auto_increment , patient_id int , first_name varchar(30) not null , middle_name varchar(30) not null , last_name varchar(30) not null , age int not null, gender varchar(20) not null , blood_group varchar(20) not null , phone_no varchar(10) not null , email_id varchar(40) not null , doctor_name varchar(40) not null , diagonosis varchar(255) , time time, date date, status varchar(30), FOREIGN KEY(patient_id) REFERENCES patient_info(patient_id));"
                cur = conn.cursor()
                # cur = conn.connect()
                column = "insert into appointment_list(patient_id,first_name, middle_name, last_name, age,gender, blood_group, phone_no, email_id, doctor_name,digonosis, time, date, status) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                values = (id, first_name, middle_name, last_name, age, gender,
                          blood_group, phone, email, doctor, digonosis, time, date)
                messagebox.showinfo(
                    "Done", "Successfull!")
                cur.execute(column, values)
                cur.execute("commit;")
                conn.commit()
            else:
                messagebox.showwarning(
                    "showwarning", "invalid value for status")
        else:
            messagebox.showwarning("showwarning", "Some value is empty")
        # print(name, age, gender, doctor, date, time, phone)

    # messagebox.showinfo("Appointment Added")
    b1 = Button(patient_info_frame, text="Add Appointment", command=callback,
                activeforeground="black", activebackground="#7acaff", pady=10)
    b1.grid(column=5, row=4)
