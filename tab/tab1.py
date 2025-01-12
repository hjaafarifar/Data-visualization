import customtkinter as ctk
from tkinter import messagebox as msg
import matplotlib.pylab as plt
from PIL import Image

# Create a tab class
# ایجاد یک کلاس tab
class Tab1(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master,width=600,height=500,)

        self.label=ctk.CTkLabel(self,text='Creat pie chart')
        self.label.pack(pady=20)

    
        # Get the number of data
        # گرفتن تعداد داده ها
        self.entry=ctk.CTkEntry(self,placeholder_text='Enter sum of date')
        self.entry.pack(pady=20)
        

        # A button to perform the function and make entries
        # دکمه ای برای انجام تابع و ساختن ورودی ها
        self.butt=ctk.CTkButton(self,text='Next',command=self.constract)
        self.butt.pack(pady=10)


    def constract(self):
        # try block to check whether the input is a number
        # بلاک try برای برسی عدد بودن ورودی 
        try:
            self.sum=int(self.entry.get())
            if 2<=int(self.sum)<=10:

                # A list to store the entries we have received from the user
                # لیستی برای ذخیره ورودی هایی که از کاربر گرفته ایم
                self.entrylistdata=[]
                self.entrylistname=[]

                # Create another page to receive entries
                # ایجاد صفحه دیگری برای دریافت ورودی ها
                self.app=ctk.CTkToplevel(self,)
                self.app.title('new page')
                self.app.geometry('400,300')
                self.app.attributes('-topmost',True)

                # Lock the button and input of the first page
                # قفل کردن دکمه و ورودی صفحه اول
                self.entry.configure(state='disabled')
                self.butt.configure(state='disabled')
                

                self.frame=ctk.CTkFrame(self.app)
                self.frame.pack(pady=20)

                # Create an entry for the number of numbers taken from the user
                # ایجاد ورودی به تعداد عدد گرفته شده از کاربر
                for i in range(self.sum):
                    self.entrydata=ctk.CTkEntry(self.frame,placeholder_text=f'Enter data{i+1}')
                    self.entrydata.grid(row=i,column=0)
                    self.entrylistdata.append(self.entrydata)

                    self.entryname=ctk.CTkEntry(self.frame,placeholder_text=f'Enter data name {i+1}')
                    self.entryname.grid(row=i,column=1)
                    self.entrylistname.append(self.entryname)

                self.buttaddtolist=ctk.CTkButton(self.app,text='add data to list',command=self.add_to_list)
                self.buttaddtolist.pack(pady=20)
            else:    
                msg.showerror('Error','Please Enter a Num beetwen 2 and 10') 
                self.entry.delete(0,'end')
                
        except:
            msg.showerror('Error','Please Enter a Num ')
            self.entry.delete(0,'end')
        
    
    
    def add_to_list(self):
        self.a=[]
        self.b=[]
        try:
            # Store decimal data
            # ذخیره داده های اعشاره
            for entry1 in self.entrylistdata:
                self.a.append(float(entry1.get()))

            # Store decimal data names
            # ذخیره نام داده های اعشاری
            for entry2 in self.entrylistname:
                self.b.append(entry2.get())

            self.creatplotbut=ctk.CTkButton(self.app,text='Creat plot',command=self.creat)
            self.creatplotbut.pack(pady=20)
        except ValueError:
            self.app.attributes('-topmost',False)
            msg.showerror('Error','Please Enter a digit')
            entry1.delete(0,'end')
    # Build the chart
    # ساختن نمودار
    def creat(self):
        self.app.destroy()
        plt.pie(self.a,labels=self.b,autopct='%2.0f%%')
        plt.show()
        