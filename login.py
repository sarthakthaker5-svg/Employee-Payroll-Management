from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox, simpledialog
import os
import subprocess
import smtplib
import random

class Login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        img = Image.open("Image/phones.png")
        img = img.resize((400, 550), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(img)
        self.lbl_image = Label(self.root, image=self.image, bd=0)
        self.lbl_image.place(x=200, y=90)

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="Login System",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Username",font=("Calibri",15),bg="white",fg="gray").place(x=125,y=100)
        self.username=StringVar()
        self.password=StringVar()
        txt_username=Entry(login_frame,textvariable=self.username,font=("times new roman",15),bg="light gray").place(x=50,y=140,width=250)

        lbl_pass=Label(login_frame,text="Password",font=("Calibri",15),bg="white",fg="gray").place(x=125,y=200)
        txt_password=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="light gray").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Login",font=("Arial Rounded MT Bold",18),bg="blue",fg="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="light gray").place(x=50,y=365,width=250,height=2)
        or_=Label(login_frame,text="OR",fg="light gray",bg="white",font=("times new roman",15,"bold")).place(x=150,y=350)
        
        btn_forget = Button(login_frame,text="Forget Password?",command=self.forget_window,font=("Arial Rounded MT Bold", 13),bg="white", fg="blue",cursor="hand2", bd=0,activebackground="white", activeforeground="blue").place(x=100, y=400)

        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="Don't have an account?",font=("Calibri",13),bg="white").place(x=40,y=15)
        btn_signup=Button(register_frame,text="Sign up",font=("Arial Rounded MT Bold",13),bg="white",fg="blue",cursor="hand2",bd=0,activebackground="white",activeforeground="blue").place(x=205,y=13)

        self.im1=ImageTk.PhotoImage(file="Image/socialmedia.png")
        self.im2=ImageTk.PhotoImage(file="Image/signup.png")
        self.im3=ImageTk.PhotoImage(file="Image/Login.jpg")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=330,y=176,width=217,height=387)
        self.animate()
        self.stored_username, self.stored_password = self.load_user_data() # Load stored username and password when program starts

    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)

    def login(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        elif self.username.get() != self.stored_username or self.password.get() != self.stored_password:
            messagebox.showerror("Error", "Invalid Username or Password \n Try Again")
        else:
            self.root.destroy()
            subprocess.Popen(["python", "employee.py"])


    def forget_window(self):
        self.forget_win = Toplevel(self.root)
        self.forget_win.title("Reset Password")
        self.forget_win.geometry("400x350+500+200")
        self.forget_win.config(bg="white")
        self.forget_win.focus_force()
        self.forget_win.grab_set()

        title = Label(self.forget_win, text="Reset Password via OTP", font=("Arial", 16, "bold"), bg="white").pack(pady=20)
        lbl_email = Label(self.forget_win, text="Enter Registered Email:", font=("Arial", 12), bg="white").pack(pady=10)
        self.var_email = StringVar()
        txt_email = Entry(self.forget_win, textvariable=self.var_email, font=("Arial", 12), bg="lightgray").pack(pady=5, ipadx=10, ipady=5)

        send_btn = Button(self.forget_win, text="Send OTP", command=self.send_otp, bg="blue", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def send_otp(self):
        email = self.var_email.get()
        if email == "":
            messagebox.showerror("Error", "Please enter your registered email", parent=self.forget_win)
            return
        
        # ✅ Generate a 6-digit OTP
        self.otp = str(random.randint(100000, 999999))
        
        try:
            # Configure your email sender credentials
            sender_email = "22bsit148@charusat.edu.in"
            sender_pass = "fsjd vbcs cocg oupe"  # Use App Password (not normal password)
            
            # Create SMTP session
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_pass)
            
            subject = "Password Reset OTP"
            body = f"Your OTP for password reset is {self.otp}"
            msg = f"Subject: {subject}\n\n{body}"
            
            server.sendmail(sender_email, email, msg)
            server.quit()

            messagebox.showinfo("Success", f"OTP sent to {email}", parent=self.forget_win)
            
            self.otp_verification_window()

        except Exception as ex:
            messagebox.showerror("Error", f"Failed to send email\n{str(ex)}", parent=self.forget_win)

    def otp_verification_window(self):
        for widget in self.forget_win.winfo_children():
            widget.destroy()

        Label(self.forget_win, text="Enter OTP:", font=("Arial", 12), bg="white").pack(pady=20)
        self.var_otp = StringVar()
        Entry(self.forget_win, textvariable=self.var_otp, font=("Arial", 12), bg="lightgray").pack(pady=5, ipadx=10, ipady=5)
        Button(self.forget_win, text="Verify OTP", command=self.verify_otp, bg="green", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def verify_otp(self):
        if self.var_otp.get() == self.otp:
            messagebox.showinfo("Success", "OTP Verified Successfully", parent=self.forget_win)
            self.reset_password_window()
        else:
            messagebox.showerror("Error", "Invalid OTP", parent=self.forget_win)

    def reset_password_window(self):
        for widget in self.forget_win.winfo_children():
            widget.destroy()

        Label(self.forget_win, text="Enter New Password:", font=("Arial", 12), bg="white").pack(pady=15)
        self.new_pass = StringVar()
        Entry(self.forget_win, textvariable=self.new_pass, font=("Arial", 12), bg="lightgray", show="*").pack(pady=5, ipadx=10, ipady=5)

        Label(self.forget_win, text="Confirm Password:", font=("Arial", 12), bg="white").pack(pady=15)
        self.confirm_pass = StringVar()
        Entry(self.forget_win, textvariable=self.confirm_pass, font=("Arial", 12), bg="lightgray", show="*").pack(pady=5, ipadx=10, ipady=5)

        Button(self.forget_win, text="Reset Password", command=self.reset_password, bg="blue", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

    def reset_password(self):
        if self.new_pass.get() == "" or self.confirm_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.forget_win)
        elif self.new_pass.get() != self.confirm_pass.get():
            messagebox.showerror("Error", "Passwords do not match", parent=self.forget_win)
        else:
            self.save_user_data(self.stored_username, self.new_pass.get())# ✅ Update saved password
            self.stored_username, self.stored_password = self.load_user_data()
            messagebox.showinfo("Success", "Password Reset Successfully!", parent=self.forget_win)
            self.forget_win.destroy()
 

    def load_user_data(self):
        """Load username and password from file."""
        if os.path.exists("user_data.txt"):
            with open("user_data.txt", "r") as f:
                data = f.read().split(",")
                if len(data) == 2:
                    return data[0], data[1]
        return "Student", "123456" # Default username & password

    def save_user_data(self, username, password):
        """Save username and password to file."""
        with open("user_data.txt", "w") as f:
            f.write(f"{username},{password}")


root=Tk()
obj=Login_System(root)
root.mainloop()