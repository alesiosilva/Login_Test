# Bibliotecas importadas
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import Database 

# Janela
#logo = PhotoImage(file='logo.png')
jan = Tk()
jan.title('Login Screen - Ale Torres!')
jan.geometry('800x600')
jan.configure(background='white')
jan.resizable(width=False, height=False)
jan.attributes('-alpha', 0.98)

# Widgets
LeftFrame = Frame(jan, width=200, height=600, bg='MIDNIGHTBLUE', relief='raise')
LeftFrame.pack(side=LEFT)
RightFrame = Frame(jan, width=595, height=600, bg='WHITE', relief='raise')
RightFrame.pack(side=RIGHT)
'''
LogoLabel = Label(LeftFrame, image=logo, bg='MIDNIGHTBLUE')
LogoLabel.place(x=50, y=100)'''

# Botões
def Register():
    LoginButton.place(x=1000)
    RegisterButton.place(x=1000)

    NomeLabel = Label(RightFrame, text='Fullname: ', font=('Century Gothic', 18), bg='WHITE', fg='BLACK')
    NomeLabel.place(x=5, y=10)
    NomeEntry = Entry(RightFrame, width=50)
    NomeEntry.place(x=150, y=25)

    EmailLabel = Label(RightFrame, text='Email: ', font=('Century Gothic', 18), bg='WHITE', fg='BLACK')
    EmailLabel.place(x=5, y=55)
    EmailEntry = Entry(RightFrame, width=50)
    EmailEntry.place(x=150, y=70)

    def RegisterToDatabase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if (Name =='' or Email =='' or User =='' or Pass ==''):
            messagebox.showerror(title='Register Error!', message='Fill all fields.')
        else:
            Database.cursor.execute('''
                INSERT INTO UserLogins(Name, Email, User, Password) VALUES(?, ?, ?, ?)                
            ''', (Name, Email, User, Pass))
            Database.conn.commit()
            messagebox.showinfo(title='Register Info', message='Register Sucessfull!')

    Register = Button(RightFrame, text='Sign in', width=15, command=RegisterToDatabase)
    Register.place(x=150, y=200)

    def BackToLogin():
        NomeLabel.place(x=1000)
        NomeEntry.place(x=1000)
        EmailLabel.place(x=1000)
        EmailEntry.place(x=1000)
        Register.place(x=1000)
        BackButton.place(x=1000)
        LoginButton.place(x=150)
        RegisterButton.place(x=150)

    BackButton = Button(RightFrame, text='Back', width=15, command=BackToLogin)
    BackButton.place(x=150, y=230)


UserLabel = Label(RightFrame, text='Username: ', font=('Century Gothic', 18), bg='WHITE', fg='BLACK' )
UserLabel.place(x=5, y=100)
UserEntry = Entry(RightFrame, width=50)
UserEntry.place(x=150, y=115)

PassLabel = Label(RightFrame, text='Password: ', font=('Century gothic', 18), bg='WHITE', fg='BLACK')
PassLabel.place(x=5, y=145)
PassEntry = Entry(RightFrame, width=50, show='*')
PassEntry.place(x=150, y=160)

  

def Login():
    UserLogin = UserEntry.get()
    PassLogin = PassEntry.get()

    Database.cursor.execute('''
        SELECT User, Password FROM UserLogins
        WHERE User=? AND Password=?
    
    ''',(UserLogin, PassLogin))

    VerifyLogin = Database.cursor.fetchone()

    try:
        if (UserLogin in VerifyLogin and PassLogin in VerifyLogin):
            messagebox.showinfo(title='Login Info', message='Login Sucessfull')
    except:
        messagebox.showerror(title='Login Info', message='Access Denied!')

LoginButton = Button(RightFrame, text='Enter', width=15, command=Login)
LoginButton.place(x=150, y=200)
RegisterButton = Button(RightFrame, text='Register', width=15, command=Register)
RegisterButton.place(x=150, y=230)



jan.mainloop()