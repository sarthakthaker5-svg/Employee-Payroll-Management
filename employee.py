from tkinter import*
from tkinter import ttk,messagebox,ttk
import sqlite3
import time
import re
import calendar
from tkcalendar import DateEntry
from datetime import date, timedelta, datetime
import os
import tempfile

class EmployeeSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1360x700+0+0")
        self.root.config(bg="white")
        title=Label(self.root,text="Employee Payroll Management System",font=("algerian",30,"bold"),bg="red",fg="White",anchor="w",padx=10).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="Employee",command=self.employee_frame,font=("arial",13,"bold"),bg="orange",fg="Black",cursor="hand2").place(x=1000,y=10,width=150,height=30)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Frame1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Variables>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.var_emp_code=StringVar()
        self.var_designation=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_proof_id=StringVar()
        self.var_contact=StringVar()
        self.var_status=StringVar()
        self.var_experience=StringVar()

        Frame1=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=750,height=620)

        title2=Label(Frame1,text="Employee Details",font=("arial",20),bg="green",fg="Black",padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code:",font=("arial",20),bg="white",fg="Black").place(x=10,y=60)
        self.txt_code = Entry(Frame1, font=("arial",15), textvariable=self.var_emp_code, bg="lightyellow", fg="Black")
        self.txt_code.place(x=220,y=70,width=180)
        btn_search=Button(Frame1,text="Search",command=self.search,font=("arial",20),bg="orange",fg="Black",cursor="hand2").place(x=450,y=70,width=150,height=30)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_designation=Label(Frame1,text="Designation:",font=("arial",20),bg="white",fg="Black").place(x=10,y=120)
        self.txt_designation=Entry(Frame1,font=("arial",15),textvariable=self.var_designation,bg="lightyellow",fg="Black")
        self.txt_designation.place(x=180,y=125,width=180)

        today = date.today()
        lbl_dob=Label(Frame1,text="D.O.B.:",font=("arial",20),bg="white",fg="Black").place(x=390,y=120)
        txt_dob = DateEntry(Frame1, font=("arial", 15), textvariable=self.var_dob,background="darkblue", foreground="white", date_pattern="dd-mm-yyyy",maxdate=today)
        txt_dob.place(x=550, y=125, width=150)
        txt_dob.bind("<<DateEntrySelected>>", self.update_age)
        lbl_doj=Label(Frame1,text="D.O.J.:",font=("arial",20),bg="white",fg="Black").place(x=390,y=170)
        txt_doj = DateEntry(Frame1, font=("arial", 15), textvariable=self.var_doj,background="darkblue", foreground="white", date_pattern="dd-mm-yyyy",maxdate=today) 
        txt_doj.place(x=550, y=175, width=150)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_name=Label(Frame1,text="Name:",font=("arial",20),bg="white",fg="Black").place(x=10,y=170)
        self.txt_name=Entry(Frame1,font=("arial",15),textvariable=self.var_name,bg="lightyellow",fg="Black")
        self.txt_name.place(x=180,y=175,width=180)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_age=Label(Frame1,text="Age:",font=("arial",20),bg="white",fg="Black").place(x=10,y=230)
        txt_age=Entry(Frame1,font=("arial",15),textvariable=self.var_age,bg="lightyellow",fg="Black",state="readonly").place(x=180,y=235,width=180)

        lbl_experience = Label(Frame1, text="Experience:", font=("arial",20), bg="white", fg="Black")
        lbl_experience.place(x=390,y=230)
        self.spin_experience = Spinbox(Frame1, from_=0, to=60, textvariable=self.var_experience,font=("arial",15), width=10, bg="lightyellow", fg="black")
        self.spin_experience.place(x=550, y=235, width=150)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW4>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_gender=Label(Frame1,text="Gender:",font=("arial",20),bg="white",fg="Black").place(x=10,y=280)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"),state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_gender.place(x=190, y=360, width=180)
        cmb_gender.current(0)

        lbl_proof_id=Label(Frame1,text="Proof ID:",font=("arial",20),bg="white",fg="Black").place(x=390,y=280)
        cmb_proof_id = ttk.Combobox(self.root, textvariable=self.var_proof_id, values=("Select", "Aadhar Card", "Pan Card", "License"),state='readonly', justify=CENTER, font=("times new roman", 15))
        cmb_proof_id.place(x=563, y=360, width=150)
        cmb_proof_id.current(0)
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW5>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_email=Label(Frame1,text="Email:",font=("arial",20),bg="white",fg="Black").place(x=10,y=330)
        self.txt_email=Entry(Frame1,font=("arial",15),textvariable=self.var_email,bg="lightyellow",fg="Black")
        self.txt_email.place(x=180,y=335,width=180)

        lbl_contact=Label(Frame1,text="Contact:",font=("arial",20),bg="white",fg="Black").place(x=390,y=330)
        vcmd = self.root.register(self.validate_contact)
        self.txt_contact = Entry(Frame1,font=("arial",15),textvariable=self.var_contact,bg="lightyellow",fg="Black",validate="key", validatecommand=(vcmd,"%P"))
        self.txt_contact.place(x=550, y=335, width=150)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW6>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_hired=Label(Frame1,text="Hired:",font=("arial",20),bg="white",fg="Black").place(x=10,y=380)
        txt_hired=Entry(Frame1,font=("arial",15),textvariable=self.var_hr_location,bg="lightyellow",fg="Black").place(x=180,y=385,width=180)

        lbl_status=Label(Frame1,text="Status:",font=("arial",20),bg="white",fg="Black").place(x=390,y=380)
        cmb_status=ttk.Combobox(self.root,textvariable=self.var_status,values=("Select","Active","Inactive"),state='readonly',justify=CENTER,font=("arial",15))
        cmb_status.place(x=563,y=455,width=150)
        cmb_status.current(0)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW7>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_address=Label(Frame1,text="Address:",font=("arial",20),bg="white",fg="Black").place(x=10,y=430)
        self.txt_address = Text(Frame1, font=("arial",15), bg="lightyellow", fg="Black")
        self.txt_address.place(x=180, y=435, width=520, height=150)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Frame2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Variables>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_t_days=StringVar()
        self.var_absent=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()

        Frame2=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=770,y=70,width=580,height=300)

        title3=Label(Frame2,text="Employee Salary Details",font=("arial",20),bg="green",fg="Black",padx=10).place(x=0,y=0,relwidth=1)

        lbl_month = Label(Frame2, text="Month:", font=("arial",16), bg="white", fg="Black")
        lbl_month.place(x=5, y=60)
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        cmb_month = ttk.Combobox(Frame2, textvariable=self.var_month, values=months, state='readonly', font=("arial",15), justify=CENTER)
        cmb_month.place(x=75, y=60, width=100)
        cmb_month.current(0)
        cmb_month.bind("<<ComboboxSelected>>", self.update_total_days)

        lbl_year=Label(Frame2,text="Year:",font=("arial",16),bg="white",fg="Black").place(x=180,y=60)
        current_year = datetime.now().year
        years = [str(y) for y in range(current_year, current_year-100, -1)]
        cmb_year = ttk.Combobox(Frame2, textvariable=self.var_year, values=years, state='readonly', font=("arial",15), justify=CENTER)
        cmb_year.place(x=240, y=60, width=100)
        cmb_year.current(0)
        cmb_year.bind("<<ComboboxSelected>>", self.update_total_days)
        
        lbl_salary=Label(Frame2,text="Basic Salary:",font=("arial",15),bg="white",fg="Black").place(x=345,y=60)
        txt_salary=Entry(Frame2,font=("arial",15),textvariable=self.var_salary,bg="lightyellow",fg="Black").place(x=470,y=60,width=100)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW1>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_days=Label(Frame2,text="Total Days:",font=("arial",18),bg="white",fg="Black").place(x=10,y=120)
        txt_days=Entry(Frame2,font=("arial",15),textvariable=self.var_t_days,bg="lightyellow",fg="Black",state='readonly').place(x=145,y=125,width=150)

        lbl_absent=Label(Frame2,text="Absent:",font=("arial",18),bg="white",fg="Black").place(x=300,y=120)
        txt_absent=Entry(Frame2,font=("arial",15),textvariable=self.var_absent,bg="lightyellow",fg="Black").place(x=420,y=125,width=150)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW2>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_medical=Label(Frame2,text="Medical:",font=("arial",18),bg="white",fg="Black").place(x=10,y=150)
        txt_medical=Entry(Frame2,font=("arial",15),textvariable=self.var_medical,bg="lightyellow",fg="Black").place(x=145,y=155,width=150)

        lbl_pf=Label(Frame2,text="PF:",font=("arial",18),bg="white",fg="Black").place(x=300,y=150)
        txt_pf=Entry(Frame2,font=("arial",15),textvariable=self.var_pf,bg="lightyellow",fg="Black").place(x=420,y=155,width=150)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<ROW3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        lbl_convence=Label(Frame2,text="Convence:",font=("arial",18),bg="white",fg="Black").place(x=10,y=180)
        txt_convence=Entry(Frame2,font=("arial",15),textvariable=self.var_convence,bg="lightyellow",fg="Black").place(x=145,y=185,width=150)

        lbl_netsalary=Label(Frame2,text="Net Salary:",font=("arial",16),bg="white",fg="Black").place(x=300,y=180)
        txt_netsalary=Entry(Frame2,font=("arial",15),textvariable=self.var_net_salary,bg="lightyellow",fg="Black",state= 'readonly').place(x=420,y=185,width=150)
        
        self.btn_delete=Button(Frame2,text="Delete",state=DISABLED,command=self.delete,font=("arial",18),bg="yellow",fg="Black",cursor="hand2")
        self.btn_delete.place(x=150,y=260,width=190,height=30)
        btn_calculate=Button(Frame2,text="Calculate",command=self.calculate,font=("arial",18),bg="yellow",fg="Black",cursor="hand2").place(x=150,y=225,width=120,height=30)
        self.btn_save=Button(Frame2,text="Save",command=self.add,font=("arial",18),bg="yellow",fg="Black",cursor="hand2")
        self.btn_save.place(x=285,y=225,width=120,height=30)
        btn_clear=Button(Frame2,text="Clear",command=self.clear,font=("arial",18),bg="yellow",fg="Black",cursor="hand2").place(x=420,y=225,width=120,height=30)
        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update,font=("arial",18),bg="yellow",fg="Black",cursor="hand2")
        self.btn_update.place(x=350,y=260,width=190,height=30)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Footer>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        footer=Label(self.root,text="EMS-Employee Payroll Management System | Hiya Patel",font=("Bahnschrift Semi Bold",11),bg="green",fg="white").pack(side=BOTTOM,fill=X)
        
        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Frame3>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        Frame3=Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=770,y=380,width=580,height=280)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Calculator>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.var_txt=StringVar()
        self.var_operator=''

        Cal_Frame = Frame(Frame3, bg="White", bd=2, relief=RIDGE)
        Cal_Frame.place(x=2, y=2, width=246, height=280)

        txt_Result=Entry(Cal_Frame,bg="lightyellow",textvariable=self.var_txt,font=("Arial",20,"bold"),justify=RIGHT).place(x=0, y=0, relwidth=1,height=40)

        # Calculator Buttons
        Button(Cal_Frame, text='7', font=('arial', 15, 'bold'),command=lambda: self.btn_click(7), cursor="hand2").place(x=0, y=39, w=60, h=52.5)
        Button(Cal_Frame, text='8', font=('arial', 15, 'bold'),command=lambda: self.btn_click(8), cursor="hand2").place(x=61, y=39, w=60, h=52.5)
        Button(Cal_Frame, text='9', font=('arial', 15, 'bold'),command=lambda: self.btn_click(9), cursor="hand2").place(x=122, y=39, w=60, h=52.5)
        Button(Cal_Frame, text='+', font=('arial', 15, 'bold'),command=lambda: self.btn_click('+'), cursor="hand2").place(x=183, y=39, w=60, h=52.5)

        Button(Cal_Frame, text='4', font=('arial', 15, 'bold'),command=lambda: self.btn_click(4), cursor="hand2").place(x=0, y=91.5, w=60, h=52.5)
        Button(Cal_Frame, text='5', font=('arial', 15, 'bold'),command=lambda: self.btn_click(5), cursor="hand2").place(x=61, y=91.5, w=60, h=52.5)
        Button(Cal_Frame, text='6', font=('arial', 15, 'bold'),command=lambda: self.btn_click(6), cursor="hand2").place(x=122, y=91.5, w=60, h=52.5)
        Button(Cal_Frame, text='-', font=('arial', 15, 'bold'),command=lambda: self.btn_click('-'), cursor="hand2").place(x=183, y=91.5, w=60, h=52.5)

        Button(Cal_Frame, text='1', font=('arial', 15, 'bold'),command=lambda: self.btn_click(1), cursor="hand2").place(x=0, y=144, w=60, h=52.5)
        Button(Cal_Frame, text='2', font=('arial', 15, 'bold'),command=lambda: self.btn_click(2), cursor="hand2").place(x=61, y=144, w=60, h=52.5)
        Button(Cal_Frame, text='3', font=('arial', 15, 'bold'),command=lambda: self.btn_click(3), cursor="hand2").place(x=122, y=144, w=60, h=52.5)
        Button(Cal_Frame, text='*', font=('arial', 15, 'bold'),command=lambda: self.btn_click('*'), cursor="hand2").place(x=183, y=144, w=60, h=52.5)

        Button(Cal_Frame, text='0', font=('arial', 15, 'bold'),command=lambda: self.btn_click(0), cursor="hand2").place(x=0, y=196.5, w=60, h=43.5)
        Button(Cal_Frame, text='c', font=('arial', 15, 'bold'),command=self.clear_cal, cursor="hand2").place(x=61, y=196.5, w=60, h=43.5)
        Button(Cal_Frame, text='=', font=('arial', 15, 'bold'),command=self.result, cursor="hand2").place(x=122, y=196.5, w=60, h=43.5)
        Button(Cal_Frame, text='/', font=('arial', 15, 'bold'),command=lambda: self.btn_click('/'), cursor="hand2").place(x=183, y=196.5, w=60, h=43.5)

        #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Salary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        sal_Frame=Frame(Frame3,bg="White", bd=2, relief=RIDGE)
        sal_Frame.place(x=250,y=2,width=323, height=350)
        title_sal=Label(sal_Frame,text="Salary Receipt",font=("arial",18),bg="green",fg="Black",padx=10).place(x=0,y=0,relwidth=1)

        sal_Frame2=Frame(sal_Frame,bg="white",bd=2,relief=RIDGE)
        sal_Frame2.place(x=0,y=30,relwidth=1,height=230)
        sample=f'''\tCompany Name, TechSolution \n\tAddress: TechSolution, Floor4
-------------------------------------------------
Employee Code\t\t: 
Employee Name\t\t:
Salary Of\t\t: Mon-YYYY
Generated On\t\t: DD-MM-YYYY
-------------------------------------------------
Total Days\t\t: DD
Total Present\t\t: DD
Total Absent\t\t: DD
Convence\t\t: Rs.----
Medical\t\t: Rs.----
PF\t\t: Rs.----
Gross Payment\t\t: Rs.--------
Net Salary\t\t: Rs.--------
-------------------------------------------------
This is computer generated slip, not
required any signature
'''
        scroll_y=Scrollbar(sal_Frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)

        self.txt_salary_reciept=Text(sal_Frame2,font=("arial",13),bg="lightyellow",yscrollcommand=scroll_y.set)
        self.txt_salary_reciept.pack(fill=BOTH,expand=2)
        scroll_y.config(command=self.txt_salary_reciept.yview)
        self.txt_salary_reciept.insert(END,sample)
        self.btn_print=Button(Cal_Frame,text="Print",state=DISABLED,command=self.print,font=("arial",18),bg="orange",fg="Black",cursor="hand2")
        self.btn_print.place(x=0,y=240,width=245,height=30)

        self.check_connection()

    def btn_click(self, num):
        self.var_operator = self.var_operator + str(num)
        self.var_txt.set(self.var_operator)

    def validate_dates(self):
        try:
            dob_str = self.var_dob.get()
            doj_str = self.var_doj.get()
            if not dob_str or not doj_str:
                return False
            dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
            doj = datetime.strptime(doj_str, "%d-%m-%Y").date()
            
            if doj < dob + timedelta(days=365*21):
                messagebox.showerror("Error", "Employee must be at least 21 years old at the time of joining.", parent=self.root)
                return False
            return True
        except Exception as ex:
            messagebox.showerror("Error", f"Invalid date format: {str(ex)}", parent=self.root)
            return False
        
    def update_age(self, event=None):
        try:
            dob_str = self.var_dob.get()
            if dob_str:
                dob = datetime.strptime(dob_str, "%d-%m-%Y").date()
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                self.var_age.set(str(age))
                max_exp = max(age - 21, 0)
                self.spin_experience.config(to=max_exp)
                try:
                    if int(self.var_experience.get()) > max_exp:
                        self.var_experience.set(str(max_exp))
                except:
                    self.var_experience.set("0")
        except Exception:
            self.var_age.set("")
            self.spin_experience.config(to=60)

    def validate_experience(self):
        """Check that experience is within valid range"""
        try:
            exp=int(self.var_experience.get())
            age=int(self.var_age.get()) if self.var_age.get().isdigit() else 0
            max_exp=max(age - 21, 0)
            if exp<0 or exp>max_exp:
                messagebox.showerror("Error",f"Experience must be between 0 and {max_exp} years.",parent=self.root)
                return False
            return True
        except ValueError:
            messagebox.showerror("Error","Experience must be a number.",parent=self.root)
            return False
        
    def validate_contact(self, P):
        if P == "":
            return True
        if P.isdigit() and len(P) <= 10:
            return True
        else:
            return False
        
    def validate_email(self, email):
        """Return True if email is in valid format"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return bool(re.match(pattern, email))
    
    import calendar
    
    def update_total_days(self, event=None):
        try:
            month_str = self.var_month.get()
            year_str = self.var_year.get()
            if month_str and year_str:
                month_num = time.strptime(month_str, "%b").tm_mon
                year_num = int(year_str)
                total_days = calendar.monthrange(year_num, month_num)[1]
                self.var_t_days.set(str(total_days))
        except:
            self.var_t_days.set("")

    def validate_days(self):
        try:
            total = int(self.var_t_days.get())
            absent = int(self.var_absent.get())
            if absent > total:
                messagebox.showerror("Error", "Absent days cannot be greater than Total Days")
                return False
            return True
        except:
            messagebox.showerror("Error", "Invalid number for days")
            return False

    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)
        self.btn_print.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.var_emp_code.set("")
        self.var_designation.set("")
        self.var_name.set("")
        self.var_age.set("Select")
        self.var_email.set("")
        self.var_hr_location.set("")
        self.var_experience.set("")
        self.var_proof_id.set("")
        self.var_contact.set("")
        self.txt_address.delete('1.0', END)
        self.var_status.set("")
        self.var_month.set("")
        self.var_year.set("")
        self.var_salary.set("")
        self.var_t_days.set("")
        self.var_absent.set("")
        self.var_medical.set("")
        self.var_pf.set("")
        self.var_convence.set("")
        self.var_net_salary.set("")
        
    def result(self):
        try:
            res = str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator = ''
        except:
            self.var_txt.set("Error")
            self.var_operator = ''

    def clear_cal(self):
        self.var_operator = ""
        self.var_txt.set("")

    def delete(self):
        self.var_operator = ""
        self.var_txt.set("")

    def is_alpha_space(self, text):
        """Return True if text contains only letters and spaces"""
        return bool(re.match(r'^[A-Za-z ]+$', text))
    
    def calculate(self):
        try:
                emp_code = self.var_emp_code.get()
                designation = self.var_designation.get()
                name = self.var_name.get()
                contact = self.var_contact.get()
                email = self.var_email.get()
                if not emp_code.isdigit():
                    messagebox.showerror("Error", "Employee Code must contain only digits", parent=self.root)
                    return
                elif not self.is_alpha_space(designation):
                    messagebox.showerror("Error", "Designation must contain only letters", parent=self.root)
                    return
                elif not self.is_alpha_space(name):
                    messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
                    return
                if not self.validate_dates():
                    return
                if not self.validate_experience():
                    return
                if not contact.isdigit() or len(contact) != 10:
                    messagebox.showerror("Error", "Contact Number must be exactly 10 digits", parent=self.root)
                    return
                if not self.validate_email(email):
                    messagebox.showerror("Error", "Invalid Email format", parent=self.root)
                    return
                if not self.validate_days():
                    return 
                con = sqlite3.connect("emp.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM e_salary WHERE emp_code=?",(self.var_emp_code.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","This Employee Code is Already Assigned", parent=self.root)
                    if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_t_days.get()=='' or self.var_absent.get()=='' or self.var_medical.get()=='' or self.var_pf.get()=='' or self.var_convence.get()=='':
                        messagebox.showerror('Error','All fields are required')
                else:
                    try:
                        per_day=int(self.var_salary.get())/int(self.var_t_days.get())
                        work_day=int(self.var_t_days.get())-int(self.var_absent.get())
                        sal_=per_day*work_day
                        deduct=int(self.var_medical.get())+int(self.var_pf.get())
                        addition=int(self.var_convence.get())
                        net_sal=sal_-deduct+addition
                        self.var_net_salary.set(str(round(net_sal,2)))
                    except ValueError:
                        messagebox.showerror("Error", "Please enter valid numeric values for salary, days, absent, medical, PF, and convence")
                        return
                    
            #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Update Reciept>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                    new_sample=f'''\tCompany Name, TechSolution\n\tAddress: TechSolution, Floor4           
-------------------------------------------------
Employee Code\t\t: {self.var_emp_code.get()}
Employee Name\t\t: {self.var_name.get()}
Salary Of\t\t: {self.var_month.get()}-{self.var_year.get()}
Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}
-------------------------------------------------
Total Days\t\t: {self.var_t_days.get()}
Total Present\t\t: {str(int(self.var_t_days.get())-int(self.var_absent.get()))}
Total Absent\t\t: {self.var_absent.get()}
Convence\t\t: Rs.{self.var_convence.get()}
Medical\t\t: Rs.{self.var_medical.get()}
PF\t\t: Rs.{self.var_pf.get()}
Gross Payment\t\t: Rs.{self.var_salary.get()}
Net Salary\t\t: Rs.{self.var_net_salary.get()}
-------------------------------------------------
This is computer generated slip, not
required any signature
'''
                    self.txt_salary_reciept.delete('1.0',END)
                    self.txt_salary_reciept.insert(END,new_sample)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        try:
            folder = "salary_receipts"
            if not os.path.exists(folder):
                os.makedirs(folder)
                    
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM e_salary WHERE emp_code=?", (self.var_emp_code.get(),))
            row = cur.fetchone()
                
            if row is None:
                messagebox.showerror("Error", "Invalid Employee Code, Please Enter Valid Employee Code", parent=self.root)
            else:
                #print(row)
                self.var_emp_code.set(row[0])
                self.var_designation.set(row[1])
                self.var_name.set(row[2]) 
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_dob.set(row[7])
                self.var_doj.set(row[8])
                self.var_proof_id.set(row[9])
                self.var_contact.set(row[10])
                self.var_status.set(row[11])
                self.var_experience.set(row[12])
                self.txt_address.delete('1.0', END)
                self.txt_address.insert(END, row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_t_days.set(row[17])
                self.var_absent.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                self.txt_salary_reciept.delete('1.0', END)  # Clear previous
                receipt = f"""
\tCompany Name, TechSolution
\tAddress: TechSolution, Floor4
--------------------------------------------------
Employee Code\t: {row[0]}
Employee Name\t: {row[2]}
Designation\t: {row[1]}
Salary Of\t: {row[14]}-{row[15]}
Generated On\t: {datetime.now().strftime("%d-%m-%Y")}

--------------------------------------------------
Total Days\t: {row[17]}
Total Absent\t: {row[18]}
Medical\t\t: {row[19]}
Convence\t: {row[21]}
PF\t\t: {row[20]}
Net Salary\t: {row[22]}
--------------------------------------------------
"""
                self.txt_salary_reciept.insert(END, receipt)
                emp_code = str(row[0])
                emp_file = os.path.join(folder, emp_code + ".txt")
                with open(emp_file, "w") as f:
                    f.write(str(row))
            con.close()
            self.btn_save.config(state=DISABLED)
            self.btn_update.config(state=NORMAL)
            self.btn_delete.config(state=NORMAL)
            self.txt_code.config(state='readonly')
            self.btn_print.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def add(self):
        emp_code = self.var_emp_code.get()
        designation = self.var_designation.get()
        name = self.var_name.get()
        contact = self.var_contact.get()
        email = self.var_email.get()
        if self.var_emp_code.get() == "" or self.var_net_salary.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All Fields must be required", parent=self.root)
            return
        elif not emp_code.isdigit():
            messagebox.showerror("Error", "Employee Code must contain only digits", parent=self.root)
            return
        elif not self.is_alpha_space(designation):
            messagebox.showerror("Error", "Designation must contain only letters", parent=self.root)
            return
        elif not self.is_alpha_space(name):
            messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
            return
        if not self.validate_dates():
            return
        if not self.validate_experience():
            return
        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Error", "Contact Number must be exactly 10 digits", parent=self.root)
            return
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid Email format", parent=self.root)
            return
        try:
            folder = "salary_receipts"
            if not os.path.exists(folder):
                os.makedirs(folder)
            emp_file = os.path.join(folder, emp_code + ".txt")
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM e_salary WHERE emp_code=?", (emp_code,))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "This Employee Code is Already Assigned", parent=self.root)
            else:
                cur.execute("INSERT INTO e_salary VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(
                    self.var_emp_code.get(),
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hr_location.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_proof_id.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.var_experience.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),
                    self.var_net_salary.get(),
                    emp_file
                    ))
                con.commit()
                with open(emp_file, "w") as f:
                    f.write(self.txt_salary_reciept.get('1.0', END))
                messagebox.showinfo("Success", f"Employee record added & Salary Receipt saved in '{folder}' folder.", parent=self.root)
                self.btn_print.config(state=NORMAL)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


    def update(self):
        emp_code = self.var_emp_code.get()
        designation = self.var_designation.get()
        name = self.var_name.get()
        contact = self.var_contact.get()
        email = self.var_email.get()

        if self.var_emp_code.get() == "" or self.var_net_salary.get() == "" or self.var_name.get() == "":
            messagebox.showerror("Error", "All Fields must be required", parent=self.root)
            return
        elif not emp_code.isdigit():
            messagebox.showerror("Error", "Employee Code must contain only digits", parent=self.root)
            return
        elif not self.is_alpha_space(designation):
            messagebox.showerror("Error", "Designation must contain only letters", parent=self.root)
            return
        elif not self.is_alpha_space(name):
            messagebox.showerror("Error", "Name must contain only letters", parent=self.root)
            return
        if not self.validate_dates():
            return
        if not self.validate_experience():
            return
        if not contact.isdigit() or len(contact) != 10:
            messagebox.showerror("Error", "Contact Number must be exactly 10 digits", parent=self.root)
            return
        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid Email format", parent=self.root)
            return
        try:
            folder = "salary_receipts"
            if not os.path.exists(folder):
                os.makedirs(folder)
                
            emp_file = os.path.join(folder, emp_code + ".txt")
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
                
            cur.execute("SELECT * FROM e_salary WHERE emp_code=?", (emp_code,))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "This Employee Code does not exist, cannot update!", parent=self.root)
            else:
                try:
                    basic_salary = float(self.var_salary.get())
                    total_days = int(self.var_t_days.get())
                    absent = int(self.var_absent.get())
                    medical = float(self.var_medical.get())
                    pf = float(self.var_pf.get())
                    convence = float(self.var_convence.get())

                    per_day = basic_salary / total_days if total_days > 0 else 0
                    deduction = (absent * per_day) + medical + pf
                    net_salary = basic_salary - deduction + convence
                except Exception:
                    messagebox.showerror("Error", "Invalid numeric input for salary calculation", parent=self.root)
                    return
                
                self.var_net_salary.set(str(round(net_salary, 2)))
                cur.execute("""UPDATE e_salary SET designation=?,name=?,age=?,gender=?,email=?,hr_location=?,dob=?,doj=?,proof_id=?,contact=?,status=?,experience=?,address=?,month=?,year=?,basic_salary=?,total_days=?,absent=?,medical=?,pf=?,convence=?,net_salary=?,salary_reciept=?WHERE emp_code=?""", (
                    self.var_designation.get(),
                    self.var_name.get(),
                    self.var_age.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_hr_location.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_proof_id.get(),
                    self.var_contact.get(),
                    self.var_status.get(),
                    self.var_experience.get(),
                    self.txt_address.get('1.0', END),
                    self.var_month.get(),
                    self.var_year.get(),
                    self.var_salary.get(),
                    self.var_t_days.get(),
                    self.var_absent.get(),
                    self.var_medical.get(),
                    self.var_pf.get(),
                    self.var_convence.get(),
                    self.var_net_salary.get(),
                    emp_file,
                    emp_code
                    ))
                con.commit()
                con.close()
                with open(emp_file, "w") as f:
                    f.write(self.txt_salary_reciept.get('1.0', END))
                messagebox.showinfo("Success", f"Employee record updated and Salary Receipt saved in '{folder}' folder.", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        try:
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM e_salary WHERE emp_code=?", (self.var_emp_code.get(),))
            row = cur.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid Employee Code! Record not found.", parent=self.root)
            else:
                confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this record?", parent=self.root)
                if confirm:
                    cur.execute("DELETE FROM e_salary WHERE emp_code=?", (self.var_emp_code.get(),))
                    emp_file = self.var_emp_code.get() + ".txt"
                    if os.path.exists(emp_file):
                        os.remove(emp_file)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Deleted", "Record Deleted Successfully", parent=self.root)
                    self.clear()
                else:
                    con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def check_connection(self):
        try:
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM e_salary")
            rows = cur.fetchall()
            #print(rows)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def show(self):
        try:
            con = sqlite3.connect("emp.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM e_salary")
            rows = cur.fetchall()
            #print(rows)
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")

    def employee_frame(self):
        self.root2=Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("1000x500+120+60")
        self.root2.config(bg="white")
        title=Label(self.root2,text="Employee Details",font=("algerian",30,"bold"),bg="red",fg="White",anchor="w",padx=10).pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.pack(side=BOTTOM,fill=X)
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('emp_code','designation','name','age','gender','email','hr_location','dob','doj','proof_id','contact','status','experience','address','month','year','basic_salary','total_days','absent','medical','pf','convence','net_salary','salary_reciept'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('emp_code',text='ECode')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='Hr')
        self.employee_tree.heading('dob',text='DOB')
        self.employee_tree.heading('doj',text='DOJ')
        self.employee_tree.heading('proof_id',text='Proof_Id')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('total_days',text='Total Days')
        self.employee_tree.heading('absent',text='Absent Days')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_reciept', text='Salary Receipt')
        self.employee_tree['show']='headings'

        self.employee_tree.column('emp_code',width=100)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('address',width=300)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('total_days',width=100)
        self.employee_tree.column('absent',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_reciept', width=100)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=BOTH,expand=1)
        self.show()

        def open_receipt(event):
            selected_item = self.employee_tree.focus()
            if not selected_item:
                return
            values = self.employee_tree.item(selected_item, "values")
            receipt_path = values[-1]   
            
            if os.path.exists(receipt_path):
                os.startfile(receipt_path) 
            else:
                messagebox.showerror("Error", f"File not found:\n{receipt_path}")
        self.employee_tree.bind("<Double-1>", open_receipt) 

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_reciept.get('1.0',END))
        os.startfile(file_,'print')

        
        self.root2.mainloop()


root=Tk()
obj=EmployeeSystem(root)
root.mainloop()