import customtkinter as ctk

# Create the frame class
# ایجاد کلاس frame
class Frame_One(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,width=200,fg_color='dark gray')

        
        # Create a label to display the text related to the switcher
        # ایجاد یک لیبل برای نمایش متنی مربوط به switcher
        self.label=ctk.CTkLabel(self,text='chenge mode...')
        self.label.grid(row=0,padx=20)
        
        # Create a switcher to change the program theme mode
        # ایجاد یک switcher  برای تغیر مود تم برنامه
        self.switchvar=ctk.StringVar(value='light')
        self.switcher=ctk.CTkSwitch(self,text=self.switchvar.get(),variable=self.switchvar,onvalue='light',offvalue='dark',command=self.switch)
        self.switcher.grid(row=1,padx=30)
    
    # The function that is connected to the switcher
    # تابعی که به switcher متصل است
    def switch(self):
        ctk.set_appearance_mode(self.switcher.get())
        self.switcher.configure(text=self.switcher.get())

   
    