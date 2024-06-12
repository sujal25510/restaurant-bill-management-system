from tkinter import*
import tkinter as tk
from tkinter import ttk
from time import strftime


import random
ran=("S000"+str(random.randint(1,100)))

root = Tk()
root.title("KFC")

root.geometry("1600x1200")





Var=IntVar()  #for radiobuttom



#for orders
bill=StringVar()
bill.set(ran)

pizza=StringVar()
burger=StringVar()
icecream=StringVar()
drinks=StringVar()
cost=StringVar()
subtotal=StringVar()
tax=StringVar()
service=StringVar()
tot=StringVar()



pizza.set("0")
burger.set("0")
icecream.set("0")
drinks.set("0")


#for feedback
name=StringVar()
email=StringVar()
rate=IntVar()
comment=StringVar()





def reset():
    ran=("S000"+str(random.randint(1,100)))
    bill.set(ran)
    pizza.set("0")
    burger.set("0")
    icecream.set("0")
    drinks.set("0")
    cost.set("0")
    subtotal.set("0")
    tax.set("0")
    service.set("0")
    tot.set("0")
    
    
    
def total():
    global n1
    global n2
    global n3
    global n4
    n1=int(pizza.get())
    n2=int(burger.get())
    n3=int(icecream.get())
    n4=int(drinks.get())
    
    totalpcost=250*n1
    totalbcost=50*n2
    totalicost=30*n3
    totaldcost=60*n4
    
    total1=totalpcost+totalbcost+totalicost+totaldcost
    cost.set(str(total1))
    subtotal.set(str(total1))
    
    total2=0.18*total1
    tax.set(total2)
    ser=0.02*total1
    service.set(ser)
    total3=total1+total2+ser
    tot.set(total3)
    
def data():
    
    n5=cost.get()
    n6=subtotal.get()
    n7=tax.get()
    n8=service.get()
    n9=tot.get()
    n10=bill.get()
    
    import sqlite3 as s

    con=s.connect('order.db')
    with con:
        
        cur=con.cursor()
        cur.execute("create table if not exists customer(BillNo text,Pizza text,Burger text,Icecream text,Drinks text,Cost text,Subtotal text,Tax text,Service text,Total text)")
        cur.execute("insert into customer(BillNo,Pizza,Burger,Icecream,Drinks,Cost,Subtotal,Tax,Service,tot) VALUES(?,?,?,?,?,?,?,?,?,?)",(n10,n1,n2,n3,n4,n5,n6,n7,n8,n9))
    con.commit()

#def delete():
    import sqlite3 as s
    con=s.connect('order.db')
    con.execute("Delete from customer where BillNo=n")
    con.commit()
    con.close()


def menu():
    card=Tk()
    card.title("MENU")
    card.geometry("500x400")
    
    m1=Label(card,text='Pizza',fg='black',font=('regular',22,'bold'),width=10,height=2)
    m1.place(x=20,y=30)
    p1=Label(card,text='250/-',fg='black',font=('regular',22,'bold'),width=8,height=2)
    p1.place(x=300,y=30)
    
    m2=Label(card,text='Burger',fg='black',font=('regular',22,'bold'),width=10,height=2)
    m2.place(x=20,y=110)
    p2=Label(card,text='250/-',fg='black',font=('regular',22,'bold'),width=8,height=2)
    p2.place(x=300,y=110)
    
    m3=Label(card,text='Icecream',fg='black',font=('regular',22,'bold'),width=10,height=2)
    m3.place(x=20,y=190)
    p3=Label(card,text='250/-',fg='black',font=('regular',22,'bold'),width=8,height=2)
    p3.place(x=300,y=190)
    
    m4=Label(card,text='Drinks',fg='black',font=('regular',22,'bold'),width=10,height=2)
    m4.place(x=20,y=270)
    p4=Label(card,text='250/-',fg='black',font=('regular',22,'bold'),width=8,height=2)
    p4.place(x=300,y=270)



#def datafeed():
    d1=name.get()
    d2=email.get()
    d3=rate.get()
    d4=comment.get()
    
    if var==1:
        d3="Excellent"
    elif var==2:
        d3="Good"
    elif var==3:
        d3="Average"
    elif var==4:
        d3="Poor"
    print(d1,d2,d3,d4)
    
    import sqlite3 as s

    con=s.connect('feedback.db')
    with con:
        
        cur=con.cursor()
        cur.execute("create table if not exists customers(Name text,Email text,rate text,Comments text)")
        cur.execute("insert into customers(Name,Email,text,Comments) VALUES(?,?,?,?)",(d1,d2,d3,d4))
    con.commit()




def feed():
    global Var
    Var=IntVar()
    
    
    root=Tk()
    root.title("feedback")
    root.geometry("800x650")
    root.minsize(800,650)
    root.maxsize(800,650)
    

    
    a1=Label(root,text="Thanks for Visiting!",fg='black',width=30,font=("regular",25,'bold'))
    a1.place(x=80,y=5)
    
    a2=Label(root,text="We'r glad you choose us! Please tell us how it was!",fg='black',font=("regular",18))
    a2.place(x=100,y=50)
    
    a3=Label(root,text="Name:-",fg='black',font=("regular",18))
    a3.place(x=20,y=120)
    
    e3=Entry(root,font=("Regular",16),width=25,bd=5)
    e3.place(x=20,y=160)
    
    a4=Label(root,text="Email:-",fg='black',font=("regular",18))
    a4.place(x=400,y=120)
   
    e4=Entry(root,font=("Regular",16),width=25,bd=5)
    e4.place(x=400,y=160)
    
    
    a5=Label(root,text="How would you rate us?",fg='black',font=("regular",18))
    a5.place(x=20,y=220)
    
    r1=Radiobutton(root,text="Excellent",font=("regular",15),variable=Var,value=1)
    r1.place(x=20,y=260)
    
    r2=Radiobutton(root,text="Good",font=("regular",15),variable=Var,value=2)
    r2.place(x=200,y=260)
    
    r3=Radiobutton(root,text="Average",font=("regular",15),variable=Var,value=3)
    r3.place(x=380,y=260)
    
    r4=Radiobutton(root,text="Poor",font=("regular",15),variable=Var,value=4)
    r4.place(x=560,y=260)
    
    
    a6=Label(root,text="Comment:-",font=('regular',18),fg='black')
    a6.place(x=20,y=320)
    txt=Text(root,width=50,height=6,font=('regular',15))
    txt.place(x=20,y=360)
    
    
    
    def datafeed():
            global Var
            d1=e3.get()
            d2=e4.get()
            d4=txt.get(1.0,END)
            d5=Var.get()
            d3=""
            if d5==1:
                d3="Excellent"
            elif d5==2:
                d3="Good"
            elif d5==3:
                d3="Average"
            elif d5==4:
                d3="Poor"
            print(d1,d2,d4,d5,d3)
            
            # import sqlite3 as s
        
            # con=s.connect('feedback.db')
            # with con:
                
            #     cur=con.cursor()
            #     cur.execute("create table if not exists customers(Name text,Email text,rate text,Comments text)")
            #     cur.execute("insert into customers(Name,Email,text,Comments) VALUES(?,?,?,?)",(d1,d2,d3,d4))
            # con.commit()
    
    
    
    
    B1=Button(root,text="Submit",fg='black',bg='red',font=("Regular",25),width=10,border=5,activebackground='dark red',command=datafeed)
    B1.place(x=100,y=540)
    
    B2=Button(root,text="Cancel",fg='white',bg='dark blue',font=("Regular",25),width=10,border=5,activebackground='sky blue',command=root.destroy)
    B2.place(x=500,y=540)
    

    
          

l = Label(root,text="Restaurant Management System",bg='dark blue',width=47,height=1,fg='white',font=('regular',42,'bold'))
l.place(x=1,y=1)


l1= Label(root,text="Bill No",fg='black',width=10,font=('Regular',15),bd=4)
l1.place(x=15,y=240)

e1= Entry(root,width=10,font=('Regular',15),bd=4,textvariable=bill)
e1.place(x=150,y=240)


l2= Label(root,text="Pizza",fg='black',width=10,font=('Regular',15),bd=4)
l2.place(x=15,y=290)

e2= Entry(root,width=10,font=('Regular',15),bd=4,textvariable=pizza)
e2.place(x=150,y=290)


l3= Label(root,text="Burger",fg='black',width=10,font=('Regular',15),bd=4)
l3.place(x=15,y=340)

e3= Entry(root,width=10,font=('Regular',15),bd=4,textvariable=burger)
e3.place(x=150,y=340)


l4= Label(root,text="Ice Cream",fg='black',width=10,font=('Regular',15),bd=4)
l4.place(x=15,y=390)

e4= Entry(root,width=10,font=('Regular',15),bd=4,textvariable=icecream)
e4.place(x=150,y=390)

l5= Label(root,text="Drinks",fg='black',width=10,font=('Regular',15),bd=4)
l5.place(x=15,y=440)

e5= Entry(root,width=10,font=('Regular',15),bd=4,textvariable=drinks)
e5.place(x=150,y=440)


l6= Label(root,text="Cost",fg='black',width=10,font=('Regular',15),bd=4)
l6.place(x=320,y=240)

e6= Entry(root,width=15,font=('Regular',15),bd=4,textvariable=cost)
e6.place(x=460,y=240)

l7= Label(root,text="Subtotal",fg='black',width=10,font=('Regular',15),bd=4)
l7.place(x=320,y=290)

e7= Entry(root,width=15,font=('Regular',15),bd=4,textvariable=subtotal)
e7.place(x=460,y=290)


l8= Label(root,text="Tax",fg='black',width=10,font=('Regular',15),bd=4)
l8.place(x=320,y=340)

e8= Entry(root,width=15,font=('Regular',15),bd=4,textvariable=tax)
e8.place(x=460,y=340)


l9= Label(root,text="Service",fg='black',width=10,font=('Regular',15),bd=4)
l9.place(x=320,y=390)

e9= Entry(root,width=15,font=('Regular',15),bd=4,textvariable=service) 
e9.place(x=460,y=390)


l10= Label(root,text="Total",fg='black',width=10,font=('Regular',15),bd=4)
l10.place(x=320,y=440)

e10= Entry(root,width=15,font=('Regular',15),bd=4,textvariable=tot)
e10.place(x=460,y=440)



b1=Button(root,text='Feedback Form',bg='green',fg='white',font=('regular',18),width=13,activebackground='dark green',command=feed)
b1.place(x=15,y=130)

b2=Button(root,text='Menu Card',bg='green',fg='white',font=('regular',18),width=13,activebackground='dark green',command=menu)
b2.place(x=1320,y=130)

b3=Button(root,text='Total',bg='green',fg='white',font=('regular',18),width=10,activebackground='dark green',command=total)
b3.place(x=15,y=520)

b4=Button(root,text='Reset',bg='green',fg='white',font=('regular',18),width=10,activebackground='dark green',command=reset)
b4.place(x=220,y=520)

b5=Button(root,text='Exit The System',bg='green',fg='white',font=('regular',18),width=15,activebackground='dark green',command=root.destroy)
b5.place(x=420,y=520)

b6=Button(root,text='Add Record',bg='green',fg='white',font=('regular',18),width=13,activebackground='dark green',command=data)
b6.place(x=1100,y=340)

b7=Button(root,text='Delete Record',bg='green',fg='white',font=('regular',18),width=13,activebackground='dark green')
b7.place(x=1320,y=340)



#for fixing frame
rightframe=Frame(root,width=700,height=400)
rightframe.place(x=500,y=500)


#for creating table
def table():
    my_tree = ttk.Treeview(root)
    my_tree['columns'] = ("ordno","piz","bur","ice","dr","ct","sb","tax","sr","tot")
    
    horizontal_bar=ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X,side=BOTTOM)
    
    vertical_bar=ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y,side=RIGHT)
    
    
    #defining column for table
    my_tree.column("#0",width=0,minwidth=0)
    my_tree.column("ordno",anchor=CENTER,width=80,minwidth=25)
    my_tree.column("piz",anchor=CENTER,width=60,minwidth=25)
    my_tree.column("bur",anchor=CENTER,width=50,minwidth=25)
    my_tree.column("ice",anchor=CENTER,width=80,minwidth=25)
    my_tree.column("dr",anchor=CENTER,width=50,minwidth=25)
    my_tree.column("ct",anchor=CENTER,width=50,minwidth=25)
    my_tree.column("sb",anchor=CENTER,width=100,minwidth=25)
    my_tree.column("tax",anchor=CENTER,width=50,minwidth=25)
    my_tree.column("sr",anchor=CENTER,width=100,minwidth=25)
    my_tree.column("tot",anchor=CENTER,width=50,minwidth=25)


    #defining headings for table
    my_tree.heading("ordno",text="Order No",anchor=CENTER)
    my_tree.heading("piz",text="Pizza",anchor=CENTER)
    my_tree.heading("bur",text="Burger",anchor=CENTER)
    my_tree.heading("ice",text="Ice cream",anchor=CENTER)
    my_tree.heading("dr",text="Drinks",anchor=CENTER)
    my_tree.heading("ct",text="Cost",anchor=CENTER)
    my_tree.heading("sb",text="Subtotal",anchor=CENTER)
    my_tree.heading("tax",text="Tax",anchor=CENTER)
    my_tree.heading("sr",text="Service",anchor=CENTER)
    my_tree.heading("tot",text="Total",anchor=CENTER)

    my_tree.pack()
table()


def time():
    time_string=strftime('%Y-%B-%d,%A,%H:%M:%S %p')
    l1.config(text=time_string)
    l1.after(1000, time)
my_font=('time',28,'bold')
l1=tk.Label(root,font=my_font,bg='yellow')
l1.place(x=10,y=650)
time()

root.mainloop()