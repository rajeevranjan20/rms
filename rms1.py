from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
from tkinter import messagebox
import sys

def main():
    win=Tk()
    app=LoginPage(win)
    win.mainloop()

class LoginPage:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0")
        self.win.title("Restaurent Management System")

        self.title_label=Label(self.win,text="Restaurant Management System",font=('Aerial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)

        self.main_frame=Frame(self.win,bg="lightgrey",bd=6,relief=GROOVE)
        self.main_frame.place(x=300,y=175,width=700,height=400)

        self.login_lbl=Label(self.main_frame,text="Login",bd=6,relief=GROOVE,anchor=CENTER,bg="lightgrey",font=('sans -serif',25,'bold'))
        self.login_lbl.pack(side=TOP,fill=X)

        self.entry_frame=LabelFrame(self.main_frame,text="Enter Details:",bd=6,relief=GROOVE,bg="lightgrey",font=('sans-serif,18'))
        self.entry_frame.pack(fill=BOTH,expand=TRUE)

        self.entus_lbl=Label(self.entry_frame,text="Enter Username:",bg="lightgrey",font=('sans-serif',15))
        self.entus_lbl.grid(row=0,column=0,padx=2,pady=2)

        username=StringVar()
        password=StringVar()

        self.entus_ent=Entry(self.entry_frame,font=('sans-serif,15'),bd=6,textvariable=username)
        self.entus_ent.grid(row=0,column=1,padx=2,pady=2)

        

        self.entpass_lbl=Label(self.entry_frame,text="Enter Password:",bg="lightgrey",font=('sans-serif',15))
        self.entpass_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.entpass_ent=Entry(self.entry_frame,font=('sans-serif,15'),bd=6,textvariable=password,show="*")
        self.entpass_ent.grid(row=1,column=1,padx=2,pady=2)

        def check_login():
            if username.get()=="Rajeev" and password.get()=="1234":
                self.billing_btn.config(state="normal")
            else:
                pass

            
            

        def reset():
            username.set("")
            password.set("")
            pass
        def billing_sect() :
            self.newWindow=Toplevel(self.win)
            self.app=Window2(self.newWindow)
        
                   
        
        self.button_frame=LabelFrame(self.entry_frame,text="Option",font=('aerial',15),bg="lightgrey",bd=7,relief=GROOVE)
        self.button_frame.place(x=20,y=100,width=730,height=85)

        self.login_btn=Button(self.button_frame,text="Login",font=('Aerial',15),bd=5,width=15,command=check_login)
        self.login_btn.grid(row=0,column=0,padx=20,pady=2)

        self.billing_btn=Button(self.button_frame,text="Billing",font=('Aerial',15),bd=5,width=15,command=billing_sect)
        self.billing_btn.grid(row=0,column=1,padx=20,pady=2)
        self.billing_btn.config(state="disabled")

        self.reset_btn=Button(self.button_frame,text="Reset",font=('Aerial',15),bd=5,width=15,command=reset)
        self.reset_btn.grid(row=0,column=2,padx=20,pady=2)


class Window2:
    def __init__(self,win):
        self.win=win
        self.win.geometry("1350x750+0+0") 
        self.win.title("Restaurent Management System")


        self.title_label=Label(self.win,text="Restaurant Management System",font=('Aerial',35,'bold'),bg="lightgrey",bd=8,relief=GROOVE)
        self.title_label.pack(side=TOP,fill=X)
        self.win.resizable(0,0)

        #######variable#######

        bill_no=random.randint(100,9999)
        bill_no_tk=IntVar()
        bill_no_tk.set(bill_no)

        calc_var=StringVar()

        cust_nm=StringVar()
        cust_cot=StringVar()
        date_pr=StringVar()
        item_pur=StringVar()
        item_qty=StringVar()
        cone=StringVar()

        date_pr.set(datetime.now())
        total_list=[]
        self.grd_total=0


        #######entry#########


        self.entry_frame=LabelFrame(self.win,text="Enter Details:",bg="lightgrey",font=('Aerial',20),bd=7,relief=GROOVE)
        self.entry_frame.place(x=20,y=95,width=500,height=650)

        self.bill_no_lbl=Label(self.entry_frame,text="Bill number",font=('Aerial',15),bg="lightgrey")
        self.bill_no_lbl.grid(row=0,column=0,padx=2,pady=2)

        self.bill_no_ent=Entry(self.entry_frame,bd=5,textvariable=bill_no_tk,font=('Aerial',15))
        self.bill_no_ent.grid(row=0,column=1,padx=2,pady=2)
        self.bill_no_ent.config(state="disabled")

        self.bill_cust_nm_lbl=Label(self.entry_frame,text="Customer Name",font=('Aerial',15),bg="lightgrey")
        self.bill_cust_nm_lbl.grid(row=1,column=0,padx=2,pady=2)

        self.bill_cust_nm_ent=Entry(self.entry_frame,bd=5,textvariable=cust_nm,font=('Aerial',15))
        self.bill_cust_nm_ent.grid(row=1,column=1,padx=2,pady=2)

        self.cust_cot_lbl=Label(self.entry_frame,text="Customer Contact",font=('Aerial',15),bg="lightgrey")
        self.cust_cot_lbl.grid(row=2,column=0,padx=2,pady=2)

        self.cust_cot_ent=Entry(self.entry_frame,bd=5,textvariable=cust_cot,font=('Aerial',15))
        self.cust_cot_ent.grid(row=2,column=1,padx=2,pady=2)

        self.date_lbl=Label(self.entry_frame,text="Date",font=('Aerial',15),bg="lightgrey")
        self.date_lbl.grid(row=3,column=0,padx=2,pady=2)

        self.date_ent=Entry(self.entry_frame,bd=5,textvariable=date_pr,font=('Aerial',15))
        self.date_ent.grid(row=3,column=1,padx=2,pady=2)


        self.item_pur_lbl=Label(self.entry_frame,text="Iteam Purchased",font=('Aerial',15),bg="lightgrey")
        self.item_pur_lbl.grid(row=4,column=0,padx=2,pady=2)

        self.item_pur_ent=Entry(self.entry_frame,bd=5,textvariable=item_pur,font=('Aerial',15))
        self.item_pur_ent.grid(row=4,column=1,padx=2,pady=2)

        self.item_qyt_lbl=Label(self.entry_frame,text="Iteam Quantity ",font=('Aerial',15),bg="lightgrey")
        self.item_qyt_lbl.grid(row=5,column=0,padx=2,pady=2)

        self.item_qyt_ent=Entry(self.entry_frame,bd=5,textvariable=item_qty,font=('Aerial',15))
        self.item_qyt_ent.grid(row=5,column=1,padx=2,pady=2)

        self.cost_one_lbl=Label(self.entry_frame,text="Cost of one",font=('Aerial',15),bg="lightgrey")
        self.cost_one_lbl.grid(row=6,column=0,padx=2,pady=2)

        self.cost_one_ent=Entry(self.entry_frame,bd=5,textvariable=cone,font=('Aerial',15))
        self.cost_one_ent.grid(row=6,column=1,padx=2,pady=2)

        ###fun

        def default_bill():
            self.bill_text.insert(END,"\t\t\t\tMehta Food Court")
            self.bill_text.insert(END,"\n\t\t\t  Daihar Chouparan Hazaribagh")
            self.bill_text.insert(END,"\n\t\t\t\tContact-7256964624")
            self.bill_text.insert(END,"\n****************************************************************************")
            self.bill_text.insert(END,f"\nBill Number {bill_no_tk.get()}")

        def genbill():
            

                    
            self.bill_text.insert(END,f"\nCustomer Name : {cust_nm.get()}")
            self.bill_text.insert(END,f"\nCustomer Contact: {cust_cot.get()}")
            self.bill_text.insert(END,f"\nDate: {date_pr.get()}")
            self.bill_text.insert(END,"\n****************************************************************************")
            self.bill_text.insert(END,f"\nProduct Name\t\tQuantity\t\tPer Cost\t\tTotal")
            self.bill_text.insert(END,"\n****************************************************************************")

            self.add_btn.config(state="normal")
            self.total_btn.config(state="normal")
            self.save_btn.config(state="normal")
         


        def clear_fun():
            cust_nm.set("")
            cust_cot.set("")
            item_pur.set("")
            item_qty.set("")           
            cone.set("")


        def add_pur():
            pass
    
        def reset_fun():
            self.grd_total=0
            self.add_btn.config(state="disabled")
            self.total_btn.config(state="disabled")
            self.save_btn.config(state="disabled")
            self.bill_text.delete("1.0",END)
            default_bill()

        def add_func():
            if item_pur.get()=="" or item_qty.get=="":
                messagebox.showerror("Error!","Please enter all the fields correctly.",parent=self.win)
            else:
                qty=int(item_qty.get())
                cones=int(cone.get())
                total=qty * cones
                total_list.append(total)
                self.bill_text.insert(END,f"\n{item_pur.get()}\t\t{item_qty.get()}\t\tRs:{cone.get()}\t\tRs:{total}")

        def total_func():
            for item in total_list:
                self.grd_total=self.grd_total +item
            self.bill_text.insert(END,"\n****************************************************************************")
            self.bill_text.insert(END,f"\n\t\t\t\t\tGrand Total : {self.grd_total}")
            self.bill_text.insert(END,"\n****************************************************************************")    

        def save_func():
            user_choice=messagebox.askyesno("Confirm?",f"D you want to save the bill{bill_no_tk.get()}",parent=self.win)
            if user_choice>0:
                self.bill_content=self.bill_text.get("1.0",END)
                try:

                    
                    con=open(f"{sys.path[0]}/bill/"+str(bill_no_tk.get())+".txt","w")
                except Exception as e:
                    messagebox.showerror("Error!",f"Error dueto{e}",parent=self.win)    
                con.write(self.bill_content)
                con.close()
                messagebox.showinfo("Success!",f"Bill{bill_no_tk.get()}has been saved successfully!",parent=self.win)
            else:
                return        
        
        #############button

        self.button_frame=LabelFrame(self.entry_frame,bd=5,text="Options:",font=("Aerial",15))
        self.button_frame.place(x=20,y=300,width=390,height=300)

        self.add_btn=Button(self.button_frame,bd=2,text="Add",font=('Aerial',12),width=12,height=3,command=add_func)
        self.add_btn.grid(row=0,column=0,padx=4,pady=2)

        self.generate_btn=Button(self.button_frame,bd=2,text="Generate",font=('Aerial',12),width=12,height=3,command=genbill)
        self.generate_btn.grid(row=0,column=1,padx=4,pady=2)

        self.clear_btn=Button(self.button_frame,bd=2,text="Clear",font=('Aerial',12),width=12,height=3,command=clear_fun)
        self.clear_btn.grid(row=0,column=2,padx=4,pady=2)

        self.total_btn=Button(self.button_frame,bd=2,text="Total",font=('Aerial',12),width=12,height=3,command=total_func)
        self.total_btn.grid(row=1,column=0,padx=4,pady=2)

        self.reset_btn=Button(self.button_frame,bd=2,text="Rest",font=('Aerial',12),width=12,height=3,command=reset_fun)
        self.reset_btn.grid(row=1,column=1,padx=4,pady=2)

        self.save_btn=Button(self.button_frame,bd=2,text="Save",font=('Aerial',12),width=12,height=3,command=save_func)
        self.save_btn.grid(row=1,column=2,padx=4,pady=2)
        
        self.add_btn.config(state="disabled")
        self.total_btn.config(state="disabled")
        self.save_btn.config(state="disabled")

    


        

        ###############calculator##########

        self.calc_frame=Frame(self.win,bd=8,background="lightgrey",relief=GROOVE)
        self.calc_frame.place(x=570,y=110,width=720,height=295)


        self.num_ent=Entry(self.calc_frame,bd=15,background="lightgrey",textvariable=calc_var,font=('Aerial',15),width=61,justify='right')
        self.num_ent.grid(column=0,row=0,columnspan=11)

        def press_btn(event):
            text=event.widget.cget("text")
            if text=="=":
                if calc_var.get().isdigit():
                    value=int(calc_var.get())
                else:
                    try:
                        value=eval(self.num_ent.get())
                    except:
                        print("Error")
                calc_var.set(value)
                self.num_ent.update()
            elif text=="C":
                pass
            else:
                calc_var.set(calc_var.get() + text)
                self.num_ent.update()                    

        self.btn7=Button(self.calc_frame,bg="lightgrey",text="7",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn7.grid(row=1,column=0,padx=1,pady=2)
        self.btn7.bind("<Button-1>",press_btn)

        self.btn8=Button(self.calc_frame,bg="lightgrey",text="8",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn8.grid(row=1,column=1,padx=1,pady=2)
        self.btn8.bind("<Button-1>",press_btn)

        self.btn9=Button(self.calc_frame,bg="lightgrey",text="9",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn9.grid(row=1,column=2,padx=1,pady=2)
        self.btn9.bind("<Button-1>",press_btn)

        
        self.btnadd=Button(self.calc_frame,bg="lightgrey",text="+",bd=8,width=11,height=1,font=('Aerial',15))
        self.btnadd.grid(row=1,column=3,padx=1,pady=2)
        self.btnadd.bind("<Button-1>",press_btn)

        self.btn6=Button(self.calc_frame,bg="lightgrey",text="6",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn6.grid(row=2,column=0,padx=1,pady=2)
        self.btn6.bind("<Button-1>",press_btn)

        self.btn5=Button(self.calc_frame,bg="lightgrey",text="5",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn5.grid(row=2,column=1,padx=1,pady=2)
        self.btn5.bind("<Button-1>",press_btn)

        self.btn4=Button(self.calc_frame,bg="lightgrey",text="4",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn4.grid(row=2,column=2,padx=1,pady=2)
        self.btn4.bind("<Button-1>",press_btn)

        self.btnsub=Button(self.calc_frame,bg="lightgrey",text="-",bd=8,width=11,height=1,font=('Aerial',15))
        self.btnsub.grid(row=2,column=3,padx=1,pady=2)
        self.btnsub.bind("<Button-1>",press_btn)

        

        self.btn1=Button(self.calc_frame,bg="lightgrey",text="1",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn1.grid(row=3,column=0,padx=1,pady=2)
        self.btn1.bind("<Button-1>",press_btn)

        self.btn2=Button(self.calc_frame,bg="lightgrey",text="2",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn2.grid(row=3,column=1,padx=1,pady=2)
        self.btn2.bind("<Button-1>",press_btn)

        self.btn3=Button(self.calc_frame,bg="lightgrey",text="3",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn3.grid(row=3,column=2,padx=1,pady=2)
        self.btn3.bind("<Button-1>",press_btn)

        

        self.btnmult=Button(self.calc_frame,bg="lightgrey",text="*",bd=8,width=11,height=1,font=('Aerial',15))
        self.btnmult.grid(row=3,column=3,padx=1,pady=2)
        self.btnmult.bind("<Button-1>",press_btn)

        

        self.btn0=Button(self.calc_frame,bg="lightgrey",text="0",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn0.grid(row=4,column=0,padx=1,pady=2)
        self.btn0.bind("<Button-1>",press_btn)

        

        self.btnpoint=Button(self.calc_frame,bg="lightgrey",text=".",bd=8,width=11,height=1,font=('Aerial',15))
        self.btnpoint.grid(row=4,column=1,padx=1,pady=2)
        self.btnpoint.bind("<Button-1>",press_btn)

        self.btn_clear=Button(self.calc_frame,bg="lightgrey",text="=",bd=8,width=11,height=1,font=('Aerial',15))
        self.btn_clear.grid(row=4,column=2,padx=1,pady=2)
        self.btn_clear.bind("<Button-1>",press_btn)

        self.btndiv=Button(self.calc_frame,bg="lightgrey",text="/",bd=8,width=11,height=1,font=('Aerial',15))
        self.btndiv.grid(row=4,column=3,padx=1,pady=2)
        self.btndiv.bind("<Button-1>",press_btn)

        #################
        ##############Bill Frame##############
        self.bill_fraame=LabelFrame(self.win,text="Bill Area",font=('Aerial',18),background="lightgrey",bd=8,relief=GROOVE)
        self.bill_fraame.place(x=585,y=420,width=650,height=276)

        self.y_scroll=Scrollbar(self.bill_fraame,orient="vertical")

        self.bill_text=Text(self.bill_fraame,bg="white",yscrollcommand=self.y_scroll.set)
        self.y_scroll.config(command=self.bill_text.yview)
        self.y_scroll.pack(side=RIGHT,fill=Y)

        self.bill_text.pack(fill=BOTH,expand=True)

        default_bill()

if __name__=="__main__":
    main()
