from tkinter import *
from variable import *
from tkinter import ttk
from tkinter import messagebox
import json
window = Tk()
window.geometry("960x540")
window.state('zoomed')
window.resizable(False,False)
#---------------------------------------------------------------------------------------------------
sing_up=PhotoImage(file='img/sing_up.gif')
backphoto=PhotoImage(file='img/back.gif')
loginn=PhotoImage(file='img/login.gif')
user_edit=PhotoImage(file='img/user_edit.gif')
user_remove=PhotoImage(file='img/user_remove.gif')
user_new=PhotoImage(file='img/user_new.gif')
users=PhotoImage(file='img/users.gif')
login_arkafon=PhotoImage(file='img/login_arka fon.gif')
next=PhotoImage(file='img/next.gif')
admin_login=PhotoImage(file='img/admin_login arkafon.gif')
sol_frame=PhotoImage(file='img/sol_frame.gif')
new_worker_frame=PhotoImage(file='img/new_worker_frame.gif')
all_worker_frame=PhotoImage(file='img/all_worker_frame.gif')
edit_worker_frame=PhotoImage(file='img/edit_worker_frame.gif')
remove_worker_frame=PhotoImage(file='img/remove_worker_frame.gif')
main_frame=PhotoImage(file='img/main_frame.gif')
show_frame=PhotoImage(file='img/eyes.gif')
show_open_frame=PhotoImage(file='img/eyes_open.gif')
#---------------------------------------------------------------------------------------------------
def singup():
    sing_up_frame = Frame()
    sing_up_frame.pack(expand=True, fill=BOTH)
    # Admin Frame-nin Arxa Fon seklinin Labeli
    Label(sing_up_frame, image=admin_login).place(relx=0, rely=0, relheight=1, relwidth=1)

    # Geriye Cixma Buttonunun Funksiyasi
    def back():
        sing_up_frame.forget()
    def yoxlama():
        if len(username.get())>=3 and username.get().strip().isalpha():
            if len(usersurname.get())>=3 and usersurname.get().strip().isalpha():
                if len(userfather.get())>=3 and userfather.get().strip().isalpha():
                    if x.get() in gunler and y.get() in aylar and z.get() in iller:
                        if cinsiyyet.get()=='Kisi'or cinsiyyet.get()=='Qadin':
                            if confirmpassword.get()==password.get() and len(password.get())>=6:
                                adminuser={
                                    'Ad': f'{username.get().strip().capitalize()}',
                                    'Soyad': f'{usersurname.get().strip().capitalize()}',
                                    'Ata Adi': f'{userfather.get().strip().capitalize()}',
                                    'Dogum Tarixi': f'{x.get()}.{y.get()}.{z.get()} ',
                                    'Password':f'{password.get()}'
                                }
                                with open('admins.txt', 'r') as file:
                                    data = file.readlines()
                                    for i in data:
                                        dict__ = eval(i)
                                        if adminuser['Ad'] == dict__['Ad'] and adminuser['Soyad'] == dict__['Soyad'] and \
                                                adminuser['Ata Adi'] == dict__['Ata Adi'] and adminuser['Dogum Tarixi'] == \
                                                dict__['Dogum Tarixi']:
                                            messagebox.showinfo('Error',f'Sirketde {username.get()}{ usersurname.get()} adinda Admin movcuddur')
                                            allwalker.clear()
                                            sing_up_frame.forget()
                                            break
                                    else:
                                        with open('admins.txt', 'a+') as file:
                                            json.dump(adminuser, file)
                                            file.write('\n')
                                        messagebox.showinfo('Successful Surgery', 'Admin Ugurla Elave Edildi')
                                        sing_up_frame.forget()
                            else:
                                messagebox.showwarning('Warning', 'Wrong Password')
                        else:
                            messagebox.showwarning('Warning', 'Wrong Gender')
                    else:
                        messagebox.showwarning('Warning', 'Wrong Birthday')
                else:
                    messagebox.showwarning('Warning', 'Wrong Father Name')
            else:
                messagebox.showwarning('Warning', 'Wrong Surname')
        else:
            messagebox.showwarning('Warning', 'Wrong Name')
    username = Entry(sing_up_frame)
    username.place(relx=0.28, rely=0.1)
    Label(sing_up_frame, text='Ad :').place(relx=0.25, rely=0.1)
    usersurname = Entry(sing_up_frame)
    usersurname.place(relx=0.44, rely=0.1)
    Label(sing_up_frame, text='Soyad :').place(relx=0.4, rely=0.1)
    userfather = Entry(sing_up_frame)
    userfather.place(relx=0.6, rely=0.1)
    Label(sing_up_frame, text='Ata Adi :').place(relx=0.55, rely=0.1)
    cinsiyyet = StringVar()
    kisi = Radiobutton(sing_up_frame, text='Kisi', value='Kisi', variable=cinsiyyet).place(relx=0.68, rely=0.15)
    qadin = Radiobutton(sing_up_frame, text='Qadin', value='Qadin', variable=cinsiyyet).place(relx=0.73, rely=0.15)
    Label(sing_up_frame, text='Cinsiyyet:').place(relx=0.63, rely=0.15)
    x = StringVar()
    y = StringVar()
    z = StringVar()
    gun = ttk.Combobox(sing_up_frame, values=gunler, textvariable=x,state='readonly')
    gun.place(relx=0.32, rely=0.15, relwidth=0.05)
    gun.set('Gun')
    ay = ttk.Combobox(sing_up_frame, values=aylar, textvariable=y, state='readonly')
    ay.place(relx=0.4, rely=0.15, relwidth=0.09)
    ay.set('Ay')
    il = ttk.Combobox(sing_up_frame, values=iller, textvariable=z, state='readonly')
    il.place(relx=0.54, rely=0.15, relwidth=0.06)
    il.set('Il')

    Label(sing_up_frame, text='Dogum Tarixi').place(relx=0.25, rely=0.15)


    password=Entry(sing_up_frame)
    password.place(relx=0.42, rely=0.24)
    Label(sing_up_frame, text='Password').place(relx=0.34, rely=0.24)

    confirmpassword = Entry(sing_up_frame)
    confirmpassword.place(relx=0.42, rely=0.33)
    Label(sing_up_frame, text='Confirm Password').place(relx=0.34, rely=0.33)

    login = Button(sing_up_frame, font=(20), command=yoxlama, padx=5, pady=5, image=loginn)
    login.place(relx=0.45, rely=0.55)
    # Back Button-u
    backbtn = Button(sing_up_frame, image=backphoto, command=back)
    backbtn.place(relx=0.02, rely=0.03, )
def adminlogin():
    adminloginframe=Frame(bg='grey')
    adminloginframe.pack(expand=True, fill=BOTH)
    # Admin Frame-nin Arxa Fon seklinin Labeli
    Label(adminloginframe,image=admin_login).place(relx=0,rely=0,relheight=1,relwidth=1)
    # Geriye Cixma Buttonunun Funksiyasi
    def back():
        adminloginframe.forget()
    # Login Buttonunun Funksiyasi
    def yoxlama():
        if username.get().strip()!='':
            if userpassword.get().strip()!='':
                with open('admins.txt', 'r') as file:
                    data = file.readlines()
                    for i in data:
                        dict_=eval(i)
                        if username.get().strip().capitalize()==dict_['Ad'] and userpassword.get()==dict_['Password']:
                            messagebox.showinfo('Info',f'Welcome {username.get()} {dict_['Soyad']}')
                            adminloginframe.forget()
                            login_form()
                            break
                    else:
                        messagebox.showinfo('Info','Wrong Username or Password')
            else:
                messagebox.showinfo('Info','Password Daxil Edin. ')
        else:
            messagebox.showinfo('Info','Username Daxil Edin. ')
    username = Entry(adminloginframe,bg='black',fg='white',font=(20))
    username.place(relx=0.5, rely=0.19, relwidth=0.2, relheight=0.1)
    Label(adminloginframe, text='Admin Name:', bg='grey', font=(20)).place(relx=0.3, rely=0.19, relwidth=0.2, relheight=0.1)
    # Password alma
    userpassword = Entry(adminloginframe,bg='black',fg='white',font=(20),show='*')
    userpassword.place(relx=0.5, rely=0.35, relwidth=0.2, relheight=0.1)
    Label(adminloginframe, text='Admin Password:', bg='grey', font=(20)).place(relx=0.3, rely=0.35, relwidth=0.2, relheight=0.1)
    # Login Button-u
    login = Button(adminloginframe,font=(20),command=yoxlama,padx=5,pady=5,image=loginn)
    login.place(relx=0.45, rely=0.55)
    show_sum = 0
    def show():
        nonlocal show_sum
        if show_sum==0:
            userpassword.config(show='')
            showbtn.config(image=show_open_frame)
            show_sum=1
        else:
            userpassword.config(show='*')
            showbtn.config(image=show_frame)
            show_sum=0
    # Back Button-u
    backbtn = Button(adminloginframe, image=backphoto, command=back)
    backbtn.place(relx=0.02, rely=0.03, )
    showbtn = Button(adminloginframe, image=show_frame, command=show)
    showbtn.place(relx=0.75, rely=0.35, )
def login_form():
    login_frame = Frame( bg="blue").pack(expand=True, fill=BOTH)
    framesol = Frame(login_frame, bg="red").place(relx=0, rely=0, relwidth=0.2, relheight=1)
    Label(framesol,image=sol_frame).place(relx=0,rely=0,relwidth=0.2,relheight=1)
    framesag = Frame(login_frame, ).place(relx=0.2, rely=0, relwidth=1, relheight=1)
    Label(framesag,image=main_frame).place(relx=0.2,rely=0,relheight=1,relwidth=1)
    # Yeni isci eklemek
    def newworker():
        newworker = Frame(framesag, bg="green")
        newworker.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        Label(newworker, image=new_worker_frame).place(relx=0, rely=0)

        def register():
            if len(username.get())>=3 and username.get().strip().isalpha():
                if len(usersurname.get())>=3 and usersurname.get().strip().isalpha():
                    if len(userfather.get())>=3 and userfather.get().strip().isalpha():
                        if x.get() in gunler and y.get() in aylar and z.get() in iller:
                            if vezife_var.get() in vezifeler:
                                if cinsiyyet.get()=='Kisi'or cinsiyyet.get()=='Qadin':
                                    if tecrube_var.get() in iscitecrubesi:
                                        if seher_var.get() in azerbaycan_sheherleri:
                                            if unvan_var.get().strip()!='':
                                                allwalker= { 'Ad': f'{username.get().strip().capitalize()}',
                                                             'Soyad': f'{usersurname.get().strip().capitalize()}',
                                                             'Ata Adi': f'{userfather.get().strip().capitalize()}',
                                                             'Dogum Tarixi': f'{x.get()}.{y.get()}.{z.get()} ',
                                                             'Iscinin Vezifesi': f'{vezife_var.get()}',
                                                             'Cinsiyyet':f'{cinsiyyet.get()}',
                                                             'Iscinin Tecrubesi': f'{tecrube_var.get()}',
                                                             'Seher': f'{seher_var.get()}',
                                                             'Unvan': f'{unvan_var.get()}',
                                                             'About':f'{about.get(0.0,END)}'}
                                                with open('workers.txt', 'r') as file:
                                                    data=file.readlines()
                                                    for i in data:
                                                        dict__=eval(i)
                                                        if allwalker['Ad']==dict__['Ad'] and allwalker['Soyad']==dict__['Soyad'] and\
                                                            allwalker['Ata Adi']==dict__['Ata Adi'] and allwalker['Dogum Tarixi']==dict__['Dogum Tarixi']:
                                                            messagebox.showinfo('Error',f'Sirketde {username.get(), usersurname.get()} adinda isci movcuddur')
                                                            allwalker.clear()
                                                            break
                                                    else:
                                                        with open('workers.txt', 'a+') as file:
                                                            json.dump(allwalker, file)
                                                            file.write('\n')
                                                        allwalker.clear()
                                                        messagebox.showinfo('Successful Surgery','Isci Ugurla Elave Edildi')
                                                        Label(framesag, image=main_frame).place(relx=0.2, rely=0,relheight=1,relwidth=1)
                                            else:
                                                messagebox.showwarning('Warning', 'Unvan Daxil Edin')
                                        else:
                                            messagebox.showwarning('Warning', 'Seher Daxil Edin')
                                    else:
                                        messagebox.showwarning('Warning', 'Tecrube Daxil Edin')
                                else:
                                    messagebox.showwarning('Warning', 'Cinsiyyet Daxil Edin')
                            else:
                                messagebox.showwarning('Warning', 'Vezife Daxil Edin')
                        else:
                            messagebox.showwarning('Warning', 'Dogum Tarixi Daxil Edin')
                    else:
                        messagebox.showwarning('Warning', 'Ata Adi Daxil Edin')
                else:
                    messagebox.showwarning('Warning', 'Soyad Daxil Edin')
            else:
                messagebox.showwarning('Warning','Ad Daxil Edin')
        username = Entry(newworker)
        username.place(relx=0.13, rely=0.01)
        Label(newworker, text='Ad :').place(relx=0.1, rely=0.01)
        usersurname = Entry(newworker)
        usersurname.place(relx=0.29, rely=0.01)
        Label(newworker, text='Soyad :').place(relx=0.25, rely=0.01)
        userfather = Entry(newworker)
        userfather.place(relx=0.45, rely=0.01)
        Label(newworker, text='Ata Adi :').place(relx=0.4, rely=0.01)
        cinsiyyet=StringVar()
        kisi = Radiobutton(newworker,text='Kisi',value='Kisi',variable=cinsiyyet).place(relx=0.53,rely=0.11)
        qadin = Radiobutton(newworker,text='Qadin',value='Qadin',variable=cinsiyyet).place(relx=0.58,rely=0.11)
        Label(newworker, text='Cinsiyyet:').place(relx=0.48, rely=0.11)
        x = StringVar()
        y = StringVar()
        z = StringVar()
        gun = ttk.Combobox(newworker,values=gunler, textvariable=x,state='readonly')
        gun.place(relx=0.17, rely=0.06, relwidth=0.05)
        gun.set('Gun')
        ay = ttk.Combobox(newworker, values=aylar, textvariable=y,state='readonly')
        ay.place(relx=0.25, rely=0.06, relwidth=0.09)
        ay.set('Ay')
        il = ttk.Combobox(newworker, values=iller, textvariable=z,state='readonly')
        il.place(relx=0.39, rely=0.06, relwidth=0.06)
        il.set('Il')

        Label(newworker, text='Dogum Tarixi').place(relx=0.1, rely=0.06)


        vezife_var=StringVar()
        vezife=ttk.Combobox(newworker,values=vezifeler,textvariable=vezife_var,state='readonly').place(relx=0.35,rely=0.11,relwidth=0.06)
        Label(newworker, text='Vezifeler').place(relx=0.29, rely=0.11)

        tecrube_var=StringVar()
        tecrube=ttk.Combobox(newworker, values=iscitecrubesi, textvariable=tecrube_var,state='readonly').place(relx=0.16,rely=0.11,relwidth=0.07)
        Label(newworker, text='Isci Tecrubesi').place(relx=0.1, rely=0.11)

        seher_var=StringVar()
        seher=ttk.Combobox(newworker,values=azerbaycan_sheherleri,textvariable=seher_var,state='readonly').place(relx=0.16,rely=0.16,relwidth=0.09)
        Label(newworker, text='Seherler').place(relx=0.1, rely=0.16)
        unvan_var=StringVar()
        unvan=Entry(newworker,textvariable=unvan_var).place(relx=0.35,rely=0.16,relwidth=0.09)
        Label(newworker, text='Unvan').place(relx=0.3, rely=0.16)

        about=Text(newworker,font=20)
        about.place(relx=0.1, rely=0.22)
        Label(newworker, text='About :').place(relx=0.05, rely=0.22)
        registr = Button(newworker, text='Register', command=register)
        registr.place(relx=0.3, rely=0.95)
    # Butun iscilere baxmaq
    def workers():
        allworkerframe = Frame(framesag, bg="black")
        allworkerframe.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        with open('workers.txt','r') as file:
            data=file.readlines()
            if data==[]:
                Label(allworkerframe, text='Sirketde Isci Yoxdur',font='Bland 20', bg='black', fg='white').place(relx=0.33, rely=0.48)
            else:
                Label(allworkerframe, text='Ad', bg='black', fg='white',font='Bland 15').place(relx=0.023, rely=0.03)
                Label(allworkerframe, text='Soyad', bg='black', fg='white',font='Bland 15').place(relx=0.161, rely=0.03)
                Label(allworkerframe, text='Ata Adi', bg='black', fg='white',font='Bland 15').place(relx=0.3, rely=0.03)
                short_var = StringVar()
                short_worker = ttk.Combobox(allworkerframe, values=short, textvariable=short_var,state='readonly')
                short_worker.place(relx=0.55,rely=0.03)
                short_btn = Button(allworkerframe, image=next, command=lambda :worker_print())
                short_btn.place(relx=0.67, rely=0.001)
                list = Listbox(allworkerframe, font=20)
                list.place(relx=0, rely=0.08, relwidth=0.8, relheight=0.92)
                scrollbar = Scrollbar(allworkerframe, orient="vertical", command=list.yview)
                scrollbar.pack(side=RIGHT, fill=Y)
                list.config(yscrollcommand=scrollbar.set)
                with open('workers.txt', 'r') as file:
                    list.delete(0, END)
                    data = file.readlines()
                    for dict in data:
                        dict_ = eval(dict)
                        text = f"{(' ' * 9) + dict_['Ad'] + ' ' * (50 - len(dict_['Ad']))}{dict_['Soyad'] + ' ' * (50 - len(dict_['Soyad']))}{dict_['Ata Adi'] + ' ' * (50 - len(dict_['Ata Adi']))}"
                        list.insert(0, text)
                def worker_print():

                    with open('workers.txt', 'r') as file:
                        if short_var.get() == 'Ceo':
                                list.delete(0,END)
                                data = file.readlines()
                                for dict in data:
                                    dict_ = eval(dict)
                                    if dict_["Iscinin Vezifesi"]=='CEO':
                                        text=f"{(' ' * 9) + dict_['Ad']+' '*(50-len(dict_['Ad']))}{dict_['Soyad']+' '*(50-len(dict_['Soyad']))}{dict_['Ata Adi']+' '*(50-len(dict_['Ata Adi']))}{dict_['Iscinin Vezifesi']+' '*(50-len(dict_['Iscinin Vezifesi']))}"
                                        list.insert(0,text)
                        elif short_var.get() == 'Mudur':
                                list.delete(0,END)
                                data = file.readlines()
                                for dict in data:
                                    dict_ = eval(dict)
                                    if dict_["Iscinin Vezifesi"]=='Mudur':
                                        text=f"{(' ' * 9) + dict_['Ad']+' '*(50-len(dict_['Ad']))}{dict_['Soyad']+' '*(50-len(dict_['Soyad']))}{dict_['Ata Adi']+' '*(50-len(dict_['Ata Adi']))}{dict_['Iscinin Vezifesi']+' '*(50-len(dict_['Iscinin Vezifesi']))}"
                                        list.insert(0,text)
                        elif short_var.get() == 'Direktor':
                                list.delete(0,END)
                                data = file.readlines()
                                for dict in data:
                                    dict_ = eval(dict)
                                    if dict_["Iscinin Vezifesi"]=='Direktor':
                                        text=f"{(' ' * 9) + dict_['Ad']+' '*(50-len(dict_['Ad']))}{dict_['Soyad']+' '*(50-len(dict_['Soyad']))}{dict_['Ata Adi']+' '*(50-len(dict_['Ata Adi']))}{dict_['Iscinin Vezifesi']+' '*(50-len(dict_['Iscinin Vezifesi']))}"
                                        list.insert(0,text)
                        elif short_var.get() == 'Isci':
                                list.delete(0,END)
                                data = file.readlines()
                                for dict in data:
                                    dict_ = eval(dict)
                                    if dict_["Iscinin Vezifesi"]=='Isci':
                                        text=f"{(' ' * 9) + dict_['Ad']+' '*(50-len(dict_['Ad']))}{dict_['Soyad']+' '*(50-len(dict_['Soyad']))}{dict_['Ata Adi']+' '*(50-len(dict_['Ata Adi']))}{dict_['Iscinin Vezifesi']+' '*(50-len(dict_['Iscinin Vezifesi']))}"
                                        list.insert(0,text)
                        elif short_var.get() == 'Xadimeci':
                                list.delete(0,END)
                                data = file.readlines()
                                for dict in data:
                                    dict_ = eval(dict)
                                    if dict_["Iscinin Vezifesi"]=='Xadimeci':
                                        text=f"{(' ' * 9) + dict_['Ad']+(' '*(50-len(dict_['Ad'])))}{dict_['Soyad']+' '*(50-len(dict_['Soyad']))}{dict_['Ata Adi']+' '*(50-len(dict_['Ata Adi']))}{dict_['Iscinin Vezifesi']+' '*(50-len(dict_['Iscinin Vezifesi']))}"
                                        list.insert(0,text)
                        else:
                            list.delete(0, END)
                            data = file.readlines()
                            for dict in data:
                                dict_ = eval(dict)
                                text = f"{(' ' * 9) + dict_['Ad'] + ' ' * (50 - len(dict_['Ad']))}{dict_['Soyad'] + ' ' * (50 - len(dict_['Soyad']))}{dict_['Ata Adi'] + ' ' * (50 - len(dict_['Ata Adi']))}"
                                list.insert(0, text)
    # Isci silmek
    def deletworkers():
        deletworkerframe = Frame(framesag, )
        deletworkerframe.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        with open('workers.txt', 'r') as file:
            data = file.readlines()
            if data == []:
                Label(deletworkerframe, bg="black").place(relx=0, rely=0, relheight=1, relwidth=1)
                Label(deletworkerframe, text='Sirketde Isci Yoxdur',font='Bland 20', bg='black', fg='white').place(relx=0.33, rely=0.48)
            else:
                Label(deletworkerframe, image=remove_worker_frame).place(relx=0, rely=0, relheight=1, relwidth=1)
                def deletworker():
                    if username.get().strip()!='':
                        if usersurname.get().strip()!='':
                            if userfather.get().strip()!='':
                                for dict in data:
                                    removelement = dict
                                    dict_ = eval(dict)
                                    if dict_['Ad'] == username.get().strip().capitalize() and dict_['Soyad'] == usersurname.get().strip().capitalize() and dict_['Ata Adi'] == userfather.get().strip().capitalize():
                                        cavab = messagebox.askyesno('Stop',f'{username.get()} Adli Iscini Silmek Isteyirsiz?')
                                        if cavab == True:
                                            with open('workers.txt', 'r') as file:
                                                info = file.readlines()
                                                info.remove(removelement)
                                            with open('workers.txt', 'w') as file:
                                                for i in info:
                                                    file.write(i)
                                            messagebox.showinfo('Stop', f'{username.get()} Adli Iscini Ugurla Silindi')
                                            Label(framesag, image=main_frame).place(relx=0.2, rely=0, relheight=1,
                                                                                    relwidth=1)
                                            break
                                        else:
                                            break
                                else:
                                    messagebox.showwarning('Info', f'Isci Tapilmadi')
                            else:
                                messagebox.showinfo('Info','Ata Adi Daxil Edin')
                        else:
                            messagebox.showinfo('Info', 'Soyad Daxil Edin')
                    else:
                        messagebox.showinfo('Info', 'Ad Daxil Edin')

                username = Entry(deletworkerframe
                                 )
                username.place(relx=0.08, rely=0.01)
                Label(deletworkerframe, text='Ad :').place(relx=0.04, rely=0.01)

                usersurname = Entry(deletworkerframe
                                 )
                usersurname.place(relx=0.08, rely=0.06)
                Label(deletworkerframe, text='Soyad :').place(relx=0.04, rely=0.06)

                userfather = Entry(deletworkerframe
                                 )
                userfather.place(relx=0.08, rely=0.11)
                Label(deletworkerframe, text='Ata Adi :').place(relx=0.04, rely=0.11)
                deletbutton = Button(deletworkerframe, text='Delet Worker',command=deletworker)
                deletbutton.place(relx=0.4, rely=0.95)
    # Iscinin edit elenmesi
    def editworkers():
        editworkersframe = Frame(framesag)
        editworkersframe.place(relx=0.2, rely=0, relwidth=1, relheight=1)
        with open('workers.txt', 'r') as file:
            data = file.readlines()
            if data==[]:
                Label(editworkersframe, bg="black").place(relx=0, rely=0, relheight=1, relwidth=1)
                Label(editworkersframe, text='Sirketde Isci Yoxdur',font='Bland 20', bg='black', fg='white').place(relx=0.33, rely=0.48)
            else:
                Label(editworkersframe, image=edit_worker_frame).place(relx=0, rely=0, relheight=1, relwidth=1)
                def searchrworker():
                    work=False
                    if username.get().strip()!='':
                        if usersurname.get().strip()!='':
                            if userfather.get().strip()!='':
                                for dictionary in data:
                                    dict = eval(dictionary)
                                    if dict['Ad'] == username.get().strip().capitalize() and dict['Soyad'] == usersurname.get().strip().capitalize() and dict['Ata Adi'] == userfather.get().strip().capitalize():
                                        work=True
                                        break
                                else:
                                    messagebox.showwarning('Warning', 'Istifadeci tapilmadi')
                            else:
                                messagebox.showwarning('Info', 'Ata Adi Daxil Edin')
                        else:
                            messagebox.showwarning('Info', 'Soyad Daxil Edin')
                    else:
                        messagebox.showwarning('Info','Ad Daxil Edin')
                    if work==True:
                        vezife_var = StringVar()
                        vezife = ttk.Combobox(editworkersframe, values=vezifeler, textvariable=vezife_var,state='readonly').place(relx=0.06, rely=0.21, relwidth=0.06)
                        Label(editworkersframe, text='Vezifeler').place(relx=0, rely=0.21)
                        tecrube_var = StringVar()
                        tecrube = ttk.Combobox(editworkersframe, values=iscitecrubesi, textvariable=tecrube_var,state='readonly').place(relx=0.26, rely=0.21, relwidth=0.07)
                        Label(editworkersframe, text='Isci Tecrubesi').place(relx=0.2, rely=0.21)
                        seher_var = StringVar()
                        seher = ttk.Combobox(editworkersframe, values=azerbaycan_sheherleri,textvariable=seher_var,state='readonly').place(relx=0.06, rely=0.26, relwidth=0.09)
                        Label(editworkersframe, text='Seherler').place(relx=0, rely=0.26)
                        unvan_var = StringVar()
                        unvan = Entry(editworkersframe, textvariable=unvan_var).place(relx=0.25, rely=0.26,relwidth=0.09)
                        Label(editworkersframe, text='Unvan').place(relx=0.2, rely=0.26)
                        editworker = Button(editworkersframe, text='Edit Worker', command=lambda: editworker())
                        editworker.place(relx=0.2, rely=0.95)
                        searchbtn.destroy()
                        username.config(state='disabled')
                        usersurname.config(state='disabled')
                        userfather.config(state='disabled')
                        def editworker():
                            if vezife_var.get() in vezifeler:
                                if tecrube_var.get() in iscitecrubesi:
                                    if seher_var.get() in azerbaycan_sheherleri:
                                        if unvan_var.get().strip() != '':
                                            cavab = messagebox.askyesno('Info', 'Iscini Edit Etmek isteyirsiz?')
                                            if cavab == True:
                                                edit_element = dict.copy()
                                                edit_element['Iscinin Vezifesi'] = vezife_var.get()
                                                edit_element['Iscinin Tecrubesi'] = tecrube_var.get()
                                                edit_element['Seher'] = seher_var.get()
                                                edit_element['Unvan'] = unvan_var.get()

                                                data.append(json.dumps(edit_element) + '\n')
                                                data.remove(dictionary)
                                                with open('workers.txt', 'w') as file:
                                                    for line in data:
                                                        if line.strip() == json.dumps(edit_element):
                                                            file.write(json.dumps(edit_element) + '\n')
                                                        else:
                                                            file.write(line)
                                                messagebox.showinfo('Info', 'Isci Ugurla Edit Edildi')
                                                Label(framesag, image=main_frame).place(relx=0.2, rely=0, relheight=1,relwidth=1)
                                        else:
                                            messagebox.showwarning('Warning', 'Unvan Daxil Edin')
                                    else:
                                        messagebox.showwarning('Warning', 'Seher Daxil Edin')
                                else:
                                    messagebox.showwarning('Warning', 'Tecrube Daxil Edin')
                            else:
                                messagebox.showwarning('Warning', 'Vezife Daxil Edin')
                username = Entry(editworkersframe
                                 )
                username.place(relx=0.08, rely=0.01)
                Label(editworkersframe, text='Ad :').place(relx=0.04, rely=0.01)

                usersurname = Entry(editworkersframe
                                    )
                usersurname.place(relx=0.08, rely=0.06)
                Label(editworkersframe, text='Soyad :').place(relx=0.04, rely=0.06)

                userfather = Entry(editworkersframe
                                   )
                userfather.place(relx=0.08, rely=0.11)
                Label(editworkersframe, text='Ata Adi :').place(relx=0.04, rely=0.11)
                searchbtn = Button(editworkersframe, text='Search Worker', command=searchrworker)
                searchbtn.place(relx=0.19, rely=0.11)
    # Isci eklemek Button-u
    newworker=Button(framesol,image=user_new,font=20,command=newworker)
    newworker.place(relx=0.045, rely=0.04, relwidth=0.08, relheight=0.13)
    # Butun isciler Button-u
    workers = Button(framesol, image=users,command=workers,font=20)
    workers.place(relx=0.045, rely=0.24, relwidth=0.08, relheight=0.13)
    # Isci silme Button-u
    deletworker = Button(framesol, image=user_remove,font=20,command=deletworkers)
    deletworker.place(relx=0.045, rely=0.44, relwidth=0.08, relheight=0.13)
    # Isci edit etme Buttonu-u
    editworker = Button(framesol, image=user_edit,font=20,command=editworkers)
    editworker.place(relx=0.045, rely=0.64, relwidth=0.08, relheight=0.13)
# Ilk yaradilan seyfenin arxa fon sekli eklemek ucun Label
Label(window,image=login_arkafon).place(relx=0,rely=0,relheight=1,relwidth=1)
# Login Button-u
btn_login=Button(window, activebackground='deepskyblue', image=loginn, command=adminlogin,padx=5,pady=5)
btn_login.place(relx=0.435, rely=0.65)
# Sing up Button-u
btn_singup=Button(window, image=sing_up, padx=5,pady=5,command=singup)
btn_singup.place(relx=0.435, rely=0.75, relwidth=0.13,relheight=0.07)

window.mainloop()