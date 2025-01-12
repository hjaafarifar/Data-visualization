import customtkinter as ctk
from tab import Tab1,Tab2

# Create a frame class
# ایجاد یک کلاس frame
class Frame_Two(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=600,fg_color='light gray')
        

        # Create a tabview
        # ایجاد یک tabview
        self.tabveiw=ctk.CTkTabview(self,width=600,height=500,fg_color='light gray',anchor='nw')
        self.tabveiw.pack()
       
        # Using the Tab1 module
        # استفاده از ماژول Tab1
        self.tabone=self.tabveiw.add('Pie Chart')
        Tab1(self.tabone).pack(fill='both',expand=True)#در اینجا برنامه تب های برنامه از ماژول Tab1 استفاده میکنند
        
        # Using the Tab2 module
        # استفاده از ماژول Tab2
        self.tabtwo=self.tabveiw.add('bar chart')
        Tab2(self.tabtwo).pack(fill='both',expand=True)