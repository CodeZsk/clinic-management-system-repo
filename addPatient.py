from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox, Treeview, Scrollbar
from tkinter import ttk as ttk
from turtle import *
from datetime import datetime, date
import re
import pymysql


def addPatientBody(addPatient, conn):
    header = Label(addPatient, text="Add Patient",
                   font=("sans-serif", 10), bg="white",)
    header.pack(anchor=N, fill='x', expand=0)

    patient_info_frame = Frame(addPatient, bg="white", pady=10)
    patient_info_frame.pack(fill='x', expand=0, pady=10)

    patient_first_name_label = Label(patient_info_frame, text="Patient First Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_first_name_label.grid(pady=5, column=0, row=0)
    patient_first_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_first_name_entry.grid(pady=5, column=1, row=0)

    patient_middle_name_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                      text="Patient Middle Name:", width=25, bg='white')
    patient_middle_name_label.grid(pady=5, column=2, row=0)
    patient_middle_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_middle_name_entry.grid(pady=5, column=3, row=0)

    patient_last_name_label = Label(patient_info_frame, text="Patient Last Name:", font=(
        "times new roman", 13, "bold"), width=25, bg='white')
    patient_last_name_label.grid(pady=5, column=4, row=0)
    patient_last_name_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_last_name_entry.grid(pady=5, column=5, row=0)

    patient_age_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                              text="Age:", width=25, bg='white')
    patient_age_label.grid(pady=5, column=0, row=1)
    patient_age_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
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
        'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O', 'O-', "NA")
    patient_bloodGroup_combobox.set('select Blood Group')
    patient_bloodGroup_combobox.grid(pady=5, column=5, row=1)

    patient_contactNumber_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                        text="Patient Contact Number:", width=25, bg='white')
    patient_contactNumber_label.grid(pady=5, column=0, row=2)
    patinet_contactNumber_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patinet_contactNumber_entry.grid(pady=5, column=1, row=2)

    patient_email_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                text="Patient Email ID:", width=25, bg='white')
    patient_email_label.grid(padx=5, column=2, row=2)
    patient_email_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_email_entry.grid(padx=5, column=3, row=2)

    patinet_relativeName_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                       text="Relative Name:", width=25, bg='white')
    patinet_relativeName_label.grid(pady=5, column=0, row=3)
    patient_relativeName_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_relativeName_entry.grid(padx=5, column=1, row=3)

    patient_relativeRelation_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                           text="Relation:", width=25, bg='white')
    patient_relativeRelation_label.grid(pady=5, column=2, row=3)
    patient_relativeRelation_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patient_relativeRelation_entry.grid(padx=5, column=3, row=3)

    patinet_relativeContactNO_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                            text="Relative Contact No.", width=25, bg='white')
    patinet_relativeContactNO_label.grid(pady=5, column=0, row=4)
    patinet_relativeContactNO_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patinet_relativeContactNO_entry.grid(padx=5, column=1, row=4)

    patinet_relativeEmailId_label = Label(patient_info_frame, font=("times new roman", 13, "bold"),
                                          text="Relative Email Id", width=25, bg='white')
    patinet_relativeEmailId_label.grid(pady=5, column=2, row=4)
    patinet_relativeEmailId_entry = Entry(
        patient_info_frame, width=25, borderwidth=1, relief="solid")
    patinet_relativeEmailId_entry.grid(padx=5, column=3, row=4)

    # Patient Address
    patient_address_info_frame = Frame(addPatient, bg="white", pady=10)
    patient_address_info_frame.pack(fill='x', expand=0)

    patient_address_label = Label(patient_address_info_frame, font=("times new roman", 16, "bold"),
                                  text="Address:", bg="white")
    patient_address_label.grid(pady=5, column=0, row=0)
    patient_address_textArea = Text(patient_address_info_frame, width=50, height=2,
                                    bg="white", borderwidth=1, relief="solid")
    patient_address_textArea.grid(column=1, row=0, columnspan=2)

    patinet_city_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                               text="City", bg="white")
    patinet_city_label.grid(pady=2, column=0, row=2)
    patinet_city_entry = Entry(
        patient_address_info_frame, width=35, borderwidth=1, relief="solid")
    patinet_city_entry.grid(pady=5, column=1, row=2)

    patinet_state_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                text="State", bg="white")
    patinet_state_label.grid(pady=2, column=2, row=2)
    patinet_state_entry = Entry(
        patient_address_info_frame, width=35, borderwidth=1, relief="solid")
    patinet_state_entry.grid(pady=5, column=3, row=2)

    patinet_pincode_label = Label(patient_address_info_frame, font=("Microsoft Himalaya", 15),
                                  text="Pincode", bg="white")
    patinet_pincode_label.grid(pady=2, column=0, row=3)
    patinet_pincode_entry = Entry(
        patient_address_info_frame, width=35, borderwidth=1, relief="solid")
    patinet_pincode_entry.grid(pady=5, column=1, row=3)

    # dignosis frame
    digonosis_frame = Frame(addPatient, bg="white")
    # digonosis_frame.pack(fill='x', expand=0, pady=10)

    digonosis_frame.pack(fill='both', expand=1, pady=10)
    doctor_name_label = Label(digonosis_frame, text="Doctor's Name:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_name_label.grid(pady=5, column=0, row=0)
    doctor_name_combobox = Combobox(digonosis_frame, width=24)
    doctor_name_combobox['values'] = ('Dr.Azam(Allergists)', 'Dr.Raj(Anesthesiologists)', 'Dr.Vikas(Cardiologists)', 'Dr.Kamad(Dermatologists)', 'Dr.Sakina(gynaecologist)',
                                      'Dr.Danish(Genral Surgen)', 'Dr.Jateen(Nephrologists)', 'Dr.Tahira(Oncologists)', 'Dr.Arham(Orthopedic)', 'Dr.Zoha(Pediatricians)')
    doctor_name_combobox.set('select Doctor')
    doctor_name_combobox.grid(pady=5, column=1, row=0)

    doctor_digonosis_label = Label(digonosis_frame, text="Digonosis:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    doctor_digonosis_label.grid(pady=5, column=2, row=0)
    doctor_digonosis_entry = Entry(
        digonosis_frame, width=24, borderwidth=1, relief="solid")
    doctor_digonosis_entry.grid(pady=5, column=3, row=0)

    patient_digonosisHistory_label = Label(digonosis_frame, text="History:", font=(
        "times new roman", 13, "bold"), width=25, bg="white")
    patient_digonosisHistory_label.grid(pady=5, column=0, row=1)
    patient_digonosisHistory_textArea = Text(
        digonosis_frame, height=5, width=50, borderwidth=1, relief="solid")
    patient_digonosisHistory_textArea.grid(
        pady=5, column=1, row=1, columnspan=2)

    def calback(conn):
        first_name = patient_first_name_entry.get().strip()
        middle_name = patient_middle_name_entry.get().strip()
        last_name = patient_last_name_entry.get().strip()
        age = patient_age_entry.get().strip()
        gender = patient_gender_combobox.get()
        blood_group = patient_bloodGroup_combobox.get()
        phone = patinet_contactNumber_entry.get().strip()
        email = patient_email_entry.get()
        relative = patient_relativeName_entry.get().strip()
        relation = patient_relativeRelation_entry.get().strip()
        relative_contact = patinet_relativeContactNO_entry.get().strip()
        relative_email = patinet_relativeEmailId_entry.get().strip()
        address = patient_address_textArea.get("1.0", 'end-1c')
        city = patinet_city_entry.get().strip()
        state = patinet_state_entry.get().strip()
        pincode = patinet_pincode_entry.get().strip()
        doctor_name = doctor_name_combobox.get()
        digonosis = doctor_digonosis_entry.get().strip()
        history = patient_digonosisHistory_textArea.get("1.0", 'end-1c')

        if first_name and middle_name and last_name and age and gender and blood_group and phone and email and relative and relation and relative_contact and relative_email and address and city and state and pincode and doctor_name and digonosis and history:
            if age.isnumeric() and phone.isnumeric() and relative_contact.isnumeric() and pincode.isnumeric():
                if first_name.isalpha() and middle_name.isalpha() and last_name.isalpha() and relative.isalpha():
                    if gender == 'Male' or gender == 'Female' or gender == 'Transgender' or gender == 'Other':
                        if blood_group == 'A+' or blood_group == 'A-' or blood_group == 'B+' or blood_group == 'B-' or blood_group == 'AB+' or blood_group == 'AB-' or blood_group == 'O' or blood_group == 'O-' or blood_group == "NA":
                            if doctor_name == 'Dr.Azam(Allergists)' or doctor_name == 'Dr.Raj(Anesthesiologists)' or doctor_name == 'Dr.Vikas(Cardiologists)' or doctor_name == 'Dr.Kamad(Dermatologists)' or doctor_name == 'Dr.Sakina(gynaecologist)' or doctor_name == 'Dr.Danish(Genral Surgen)' or doctor_name == 'Dr.Jateen(Nephrologists)' or doctor_name == 'Dr.Tahira(Oncologists)' or doctor_name == 'Dr.Arham(Orthopedic)' or doctor_name == 'Dr.Zoha(Pediatricians)':
                                if len(phone) == 10:
                                    if len(pincode) == 6:
                                        today_date = date.today()
                                        time = datetime.now()
                                        mainTime = time.strftime("%H:%M:%S")
                                        try:
                                            cur = conn.cursor()
                                            # cur = conn.connect()
                                            phone = str(phone)
                                            column = "insert into patient_info(first_name,middle_name, last_name, age,gender, blood_group, phone_no, email_id, relative_name, 	relation, relative_number, relative_email, address, city, state, pin_code, doctor_name,digonosis, history, date, time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            values = (first_name, middle_name, last_name, age,
                                                      gender, blood_group, phone, email, relative, relation, relative_contact, relative_email, address, city, state, pincode, doctor_name, digonosis, history, today_date, mainTime)
                                            messagebox.showinfo(
                                                "Done", "Successfull!")
                                            cur.execute(column, values)
                                            cur.execute("commit;")
                                            conn.commit()

                                        except:
                                            cur = conn.cursor()
                                            cur = conn.connect()

                                            cur.execute("create table patient_info(patient_id int primary key auto_increment, first_name varchar(30) not null, middle_name varchar(30) not null, last_name varchar(30) not null, age int not null, gender varchar(20) not null, blood_group varchar(5), phone_no varchar(10) not null, email_id varchar(30), relative_name varchar(20), relation varchar(20), relative_number varchar(10), relative_email varchar(30), address varchar(70), city varchar(10), state varchar(20), pin_code varchar(6), doctor_name varchar(30), digonosis varchar(30), history varchar(200), date date, time time)")
                                            column = "insert into patient_info(first_name,middle_name, last_name, age,gender, blood_group, phone_no, email_id, relative_name, 	relation, relative_number, relative_email, address, city, state, pin_code, doctor_name,digonosis, history, date, time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                            values = (first_name, middle_name, last_name, age,
                                                      gender, blood_group, phone, email, relative, relation, relative_contact, relative_email, address, city, state, pincode, doctor_name, digonosis, history, today_date, mainTime)
                                            cur.execute(column, values)
                                            messagebox.showinfo(
                                                "Done", "Successfull2!")
                                            conn.commit()
                                    else:
                                        messagebox.showwarning(
                                            "showwarning", "pincode is wrong")
                                else:
                                    messagebox.showwarning(
                                        "showwarning", "Phone number is incorrect")
                            else:
                                messagebox.showwarning(
                                    "showwarning", "please select a valid doctor name from the list")
                        else:
                            messagebox.showwarning(
                                "showwarning", "please select a valid blood group")
                    else:
                        messagebox.showwarning(
                            "showwarning", "Gender should be male or female or transgender or other")
                else:
                    messagebox.showwarning(
                        "showwarning", "Names should be a alphabetic character")
            else:
                messagebox.showwarning(
                    "showwarning", "Enter Numeric Value for phone number and age and pincode")
        else:
            messagebox.showwarning("showwarning", "Some value is empty")

    bttn = Button(patient_info_frame, text="Add Patinet info", command=lambda: calback(conn),
                  activeforeground="black", activebackground="#7acaff", pady=10)
    bttn.grid(column=5, row=14)
