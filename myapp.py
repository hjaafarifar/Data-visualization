from frames import Frame_One ,Frame_Two
import customtkinter as ctk

# تابع شروع مجدد برنامه
def res():
    app.destroy()
    main()


# The main program class
class My_App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Basic program settings
        ctk.set_appearance_mode('light')
        ctk.set_default_color_theme('blue')
        
        # Appearance settings of the program
        self.title('Data Visualization')
        self.geometry('800x500')
        self.resizable(width=False,height=False)
        self.attributes('-topmost',False)

        # Creating a frame with the help of the frame1 module that we wrote earlier
        self.frame1=Frame_One(self)
        self.frame1.pack(side='left',fill='both',expand=True)

        # Creating a frame with the help of the frame2 module that we wrote earlier
        self.frame2=Frame_Two(self)
        self.frame2.pack(side='right',fill='both',expand=True)
        
        # Create a button in frame1 to restart the program
        self.butt=ctk.CTkButton(self.frame1,text='reset',command=res)
        self.butt.grid(row=2,pady=20,padx=30)


# Basic program settings
def main():
    global app
    app=My_App()
    app.mainloop()  
    
if __name__=='__main__':
    main()
    