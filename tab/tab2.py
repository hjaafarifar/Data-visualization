import customtkinter as ctk
from tkinter import messagebox as msg
import matplotlib.pylab as plt


# ایجاد یک کلاس tab
class Tab2(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
         

        self.lable=ctk.CTkLabel(self,text='bar chart')
        self.lable.pack(pady=20)

        # گرفتن تعداد داده ها
        self.entry=ctk.CTkEntry(self,placeholder_text='Enter sum of date')
        self.entry.pack(pady=20)
        
        # دکمه ای برای انجام تابع و ساختن ورودی ها
        self.butt=ctk.CTkButton(self,text='Next',command=self.constract)
        self.butt.pack(pady=10)

    def constract(self):
        try:
            self.sum=int(self.entry.get())
            if 2<=self.sum<=10:

                self.Primar_data_list=[]
                self.Secondary_data_list=[]

                # ایجاد صفحه دیگری برای دریافت ورودی ها
                self.app=ctk.CTkToplevel(self,)
                self.app.title('new page')
                self.app.geometry('400,300')
                self.app.attributes('-topmost',True)

                # قفل کردن دکمه و ورودی صفحه اول
                self.entry.configure(state='disabled')
                self.butt.configure(state='disabled')
                
                self.frame=ctk.CTkFrame(self.app)
                self.frame.pack(pady=20)
               
                for i in range(self.sum):
                    self.entrydata1=ctk.CTkEntry(self.frame,placeholder_text=f'Primar data{i+1}')
                    self.entrydata1.grid(row=i,column=0)
                    self.Primar_data_list.append(self.entrydata1)

                    self.entrydata2=ctk.CTkEntry(self.frame,placeholder_text=f'Secondary data{i+1}')
                    self.entrydata2.grid(row=i,column=1)
                    self.Secondary_data_list.append(self.entrydata2)
            
                self.buttaddtolist=ctk.CTkButton(self.app,text='add data to list',command=self.add_to_list)
                self.buttaddtolist.pack(pady=20)
            
            else:
                # self.app.attributes('-topmost',False)#پیغام خطا را جلو تر تز صفحتات دیکر نمایش میدهد
                msg.showerror('Error','Please Enter a Num beetwen 2 and 10') 
                self.entry.delete(0,'end')

        except:
            # self.app.attributes('-topmost',False)
            msg.showerror('Error','Please Enter a Num ')
            self.entry.delete(0,'end')

    def add_to_list(self):
        self.a=[]
        self.b=[]

        try:

            for entry1 in self.Primar_data_list:
                self.a.append(float(entry1.get()))
    
            for entry2 in self.Secondary_data_list:
                self.b.append(entry2.get())

            self.creatplotbut=ctk.CTkButton(self.app,text='Creat plot',command=self.creat)
            self.creatplotbut.pack(pady=20)

        except ValueError:
            self.app.attributes('-topmost',False)
            msg.showerror('Error','Please Enter a digit')
            entry1.delete(0,'end')

       


    def creat(self):
        self.app.destroy()
        plt.bar(self.b,self.a,)
        plt.show()