from tkinter import*
import random
import os
from tkinter import messagebox

# ============main============================
class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x800+0+0")
        self.root.title("Billing System")
        bg_color = "#135d66"
        title = Label(self.root, text="Billing System", font=('times new roman', 30, 'bold'), pady=2, bd=12, bg="#135d66", fg="#fff", relief=GROOVE)
        title.pack(fill=X)
        # ============grocery==============================
        self.milk = IntVar()
        self.oreo = IntVar()
        self.yoghurt = IntVar()
        self.cadbury = IntVar()
        self.coffee = IntVar()
        self.tea = IntVar()
        # ============grocery==============================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.daal = IntVar()
        self.flour = IntVar()
        self.maggi = IntVar()
        #=============coldDtinks=============================
        self.sprite = IntVar()
        self.water = IntVar()
        self.mazza = IntVar()
        self.coke = IntVar()
        self.fanta = IntVar()
        self.mountain_dew = IntVar()
    # ==============Total product price================
        self.medical_price = StringVar()
        self.grocery_price = StringVar()
        self.cold_drinks_price = StringVar()
    # ==============Customer==========================
        self.c_name = StringVar()
        self.c_phone = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.search_bill = StringVar()
    # ===============Tax================================
        self.medical_tax = StringVar()
        self.grocery_tax = StringVar()
        self.cold_drinks_tax = StringVar()
    # =============customer retail details======================
        F1 = LabelFrame(self.root, text="Customer Details", font=('times new roman', 15, 'bold'), bd=10, fg="#fff", bg="#135d66")
        F1.place(x=0, y=80, relwidth=1)
        cname_lbl = Label(F1, text="Customer Name:", bg=bg_color, font=('times new roman', 15, 'bold'))
        cname_lbl.grid(row=0, column=0, padx=20, pady=5)
        cname_txt = Entry(F1, width=15, textvariable=self.c_name, font='arial 15', bd=7, relief=GROOVE)
        cname_txt.grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone:", bg="#135d66", font=('times new roman', 15, 'bold'))
        cphn_lbl.grid(row=0, column=2, padx=20, pady=5)
        cphn_txt = Entry(F1, width=15, textvariable=self.c_phone, font='arial 15', bd=7, relief=GROOVE)
        cphn_txt.grid(row=0, column=3, pady=5, padx=10)

        c_bill_lbl = Label(F1, text="Bill Number:", bg="#135d66", font=('times new roman', 15, 'bold'))
        c_bill_lbl.grid(row=0, column=4, padx=20, pady=5)
        c_bill_txt = Entry(F1, width=15, textvariable=self.search_bill, font='arial 15', bd=7, relief=GROOVE)
        c_bill_txt.grid(row=0, column=5, pady=5, padx=10)

        bil_btn = Button(F1, text="Search", command=self.find_bill, width=10, bd=7, font=('arial', 12, 'bold'), relief=GROOVE)
        bil_btn.grid(row=0, column=6, pady=5, padx=10)

     # ==========GroceryItems=========================
        F2 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="#fff", bg="#135d66")
        F2.place(x=0, y=180, width=325, height=380)

        milk_lbl = Label(F2, text="Milk", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        milk_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        milk_txt = Entry(F2, width=10, textvariable=self.milk, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        milk_txt.grid(row=0, column=1, padx=10, pady=10)

        oreo_lbl = Label(F2, text="Oreo", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        oreo_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        oreo_txt = Entry(F2, width=10, textvariable=self.oreo, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        oreo_txt.grid(row=1, column=1, padx=10, pady=10)

        yoghurt_lbl = Label(F2, text="Yoghurt", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        yoghurt_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        yoghurt_txt = Entry(F2, width=10, textvariable=self.yoghurt, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        yoghurt_txt.grid(row=2, column=1, padx=10, pady=10)

        cadbury_lbl = Label(F2, text="Cadbury", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        cadbury_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        cadbury_txt = Entry(F2, width=10, textvariable=self.cadbury, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        cadbury_txt.grid(row=3, column=1, padx=10, pady=10)

        coffee_lbl = Label(F2, text="Coffee", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        coffee_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        coffee_txt = Entry(F2, width=10, textvariable=self.coffee, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coffee_txt.grid(row=4, column=1, padx=10, pady=10)

        tea_lbl = Label(F2, text="Tea", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        tea_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        tea_txt = Entry(F2, width=10, textvariable=self.tea, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        tea_txt.grid(row=5, column=1, padx=10, pady=10)

    # ==========GroceryItems=========================
        F3 = LabelFrame(self.root, text="Grocery Items", font=('times new roman', 15, 'bold'), bd=10, fg="#fff", bg="#135d66")
        F3.place(x=335, y=180, width=325, height=380)

        rice_lbl = Label(F3, text="Rice", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        rice_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        rice_txt = Entry(F3, width=10, textvariable=self.rice, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        rice_txt.grid(row=0, column=1, padx=10, pady=10)

        food_oil_lbl = Label(F3, text="Food Oil", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        food_oil_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        food_oil_txt = Entry(F3, width=10, textvariable=self.food_oil, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        food_oil_txt.grid(row=1, column=1, padx=10, pady=10)

        wheat_lbl = Label(F3, text="Wheat", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        wheat_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        wheat_txt = Entry(F3, width=10, textvariable=self.wheat, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        wheat_txt.grid(row=2, column=1, padx=10, pady=10)

        daal_lbl = Label(F3, text="Daal", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        daal_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        daal_txt = Entry(F3, width=10, textvariable=self.daal, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        daal_txt.grid(row=3, column=1, padx=10, pady=10)

        flour_lbl = Label(F3, text="Flour", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        flour_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        flour_txt = Entry(F3, width=10, textvariable=self.flour, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        flour_txt.grid(row=4, column=1, padx=10, pady=10)

        maggi_lbl = Label(F3, text="Maggi", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        maggi_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        maggi_txt = Entry(F3, width=10, textvariable=self.maggi, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        maggi_txt.grid(row=5, column=1, padx=10, pady=10)

    # ===========ColdDrinks================================
        F4 = LabelFrame(self.root, text="Cold Drinks", font=('times new roman', 15, 'bold'), bd=10, fg="#fff", bg="#135d66")
        F4.place(x=670, y=180, width=325, height=380)

        sprite_lbl = Label(F4, text="Sprite", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        sprite_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='W')
        sprite_txt = Entry(F4, width=10, textvariable=self.sprite, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        sprite_txt.grid(row=0, column=1, padx=10, pady=10)

        water_lbl = Label(F4, text="Water", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        water_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='W')
        water_txt = Entry(F4, width=10, textvariable=self.water, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        water_txt.grid(row=1, column=1, padx=10, pady=10)

        mazza_lbl = Label(F4, text="Mazza", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        mazza_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='W')
        mazza_txt = Entry(F4, width=10, textvariable=self.mazza, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mazza_txt.grid(row=2, column=1, padx=10, pady=10)

        coke_lbl = Label(F4, text="Coke", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        coke_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='W')
        coke_txt = Entry(F4, width=10, textvariable=self.coke, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        coke_txt.grid(row=3, column=1, padx=10, pady=10)

        fanta_lbl = Label(F4, text="Fanta", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        fanta_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='W')
        fanta_txt = Entry(F4, width=10, textvariable=self.fanta, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        fanta_txt.grid(row=4, column=1, padx=10, pady=10)

        mountain_dew_lbl = Label(F4, text="Mountain Dew", font=('times new roman', 16, 'bold'), bg="#135d66", fg="#fff")
        mountain_dew_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='W')
        mountain_dew_txt = Entry(F4, width=10, textvariable=self.mountain_dew, font=('times new roman', 16, 'bold'), bd=5, relief=GROOVE)
        mountain_dew_txt.grid(row=5, column=1, padx=10, pady=10)

    # =================BillArea======================
        F5 = Frame(self.root, bd=10, relief=GROOVE)
        F5.place(x=1010, y=180, width=350, height=380)

        bill_title = Label(F5, text="Bill Area", font='arial 15 bold', bd=7, relief=GROOVE)
        bill_title.pack(fill=X)
        scroll_y = Scrollbar(F5, orient=VERTICAL)
        self.txtarea = Text(F5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)

    # =======================ButtonFrame=============
        F6 = LabelFrame(self.root, text="Bill Area", font=('times new roman', 14, 'bold'), bd=10, fg="#fff", bg="#135d66")
        F6.place(x=0, y=580, relwidth=1, height=140)

        m2_lbl = Label(F6, text="Total Grocery Price", font=('times new roman', 14, 'bold'), bg="#135d66", fg="#fff")
        m2_lbl.grid(row=1, column=0, padx=20, pady=1, sticky='W')
        m2_txt = Entry(F6, width=18, textvariable=self.grocery_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m2_txt.grid(row=1, column=1, padx=18, pady=1)

        m3_lbl = Label(F6, text="Total Cold Drinks Price", font=('times new roman', 14, 'bold'), bg="#135d66", fg="#fff")
        m3_lbl.grid(row=2, column=0, padx=20, pady=1, sticky='W')
        m3_txt = Entry(F6, width=18, textvariable=self.cold_drinks_price, font='arial 10 bold', bd=7, relief=GROOVE)
        m3_txt.grid(row=2, column=1, padx=18, pady=1)

        m5_lbl = Label(F6, text="Grocery Tax", font=('times new roman', 14, 'bold'), bg="#135d66", fg="#fff")
        m5_lbl.grid(row=1, column=2, padx=20, pady=1, sticky='W')
        m5_txt = Entry(F6, width=18, textvariable=self.grocery_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m5_txt.grid(row=1, column=3, padx=18, pady=1)

        m6_lbl = Label(F6, text="Cold Drinks Tax", font=('times new roman', 14, 'bold'), bg="#135d66", fg="#fff")
        m6_lbl.grid(row=2, column=2, padx=20, pady=1, sticky='W')
        m6_txt = Entry(F6, width=18, textvariable=self.cold_drinks_tax, font='arial 10 bold', bd=7, relief=GROOVE)
        m6_txt.grid(row=2, column=3, padx=18, pady=1)

    # =======Buttons-======================================
        btn_f = Frame(F6, bd=7, relief=GROOVE)
        btn_f.place(x=760, width=580, height=105)

        total_btn = Button(btn_f, command=self.total, text="Total", bg="#0c0c0c", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        total_btn.grid(row=0, column=0, padx=5, pady=15)

        generateBill_btn = Button(btn_f, command=self.bill_area, text="Generate Bill", bd=2, bg="#535C68", fg="black", pady=12, width=12, font='arial 13 bold')
        generateBill_btn.grid(row=0, column=1, padx=5, pady=5)

        clear_btn = Button(btn_f, command=self.clear_data, text="Clear", bg="#535C68", bd=2, fg="black", pady=15, width=12, font='arial 13 bold')
        clear_btn.grid(row=0, column=2, padx=5, pady=5)

        exit_btn = Button(btn_f, command=self.exit_app, text="Exit", bd=2, bg="#535C68", fg="black", pady=15, width=12, font='arial 13 bold')
        exit_btn.grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

#================totalBill==========================
    def total(self):

        self.milk_p = self.milk.get()*25
        self.o_p = self.oreo.get()*10
        self.y_p = self.yoghurt.get()*20
        self.cad_p = self.cadbury.get()*40
        self.coffee_p = self.coffee.get()*5
        self.tea_p = self.tea.get()*5

        self.g_r_p = self.rice.get()*75
        self.g_f_o_p = self.food_oil.get()*100
        self.g_w_p = self.wheat.get()*60
        self.g_d_p = self.daal.get()*65
        self.g_f_p = self.flour.get()*80
        self.g_m_p = self.maggi.get()*12
        self.total_grocery_price = float(self.g_r_p+self.g_f_o_p+self.g_w_p+self.g_d_p+self.g_f_p+self.g_m_p+self.milk_p+self.o_p+self.y_p+self.cad_p+self.coffee_p+self.tea_p)

        self.grocery_price.set("Rs. " + str(self.total_grocery_price))
        self.g_tax = round((self.total_grocery_price*0.5), 2)
        self.grocery_tax.set("Rs. " + str(self.g_tax))

        self.c_d_s_p = self.sprite.get()*10
        self.c_d_l_p = self.water.get()*10
        self.c_d_m_p = self.mazza.get()*10
        self.c_d_c_p = self.coke.get()*10
        self.c_d_f_p = self.fanta.get()*10
        self.c_m_d = self.mountain_duo.get()*10
        self.total_cold_drinks_price = float(self.c_d_s_p+self.c_d_l_p+self.c_d_m_p+self.c_d_c_p+self.c_d_f_p+self.c_m_d)

        self.cold_drinks_price.set("Rs. "+str(self.total_cold_drinks_price))
        self.c_d_tax = round((self.total_cold_drinks_price * 0.1), 2)
        self.cold_drinks_tax.set("Rs. "+str(self.c_d_tax))

        self.total_bill = float(self.total_grocery_price+self.total_cold_drinks_price+self.c_tax+self.g_tax+self.c_d_tax)

#==============welcome-bill==============================
    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END, "\tWelcome to BB Retail Shop")
        self.txtarea.insert(END, f"\n Bill Number:{self.bill_no.get()}")
        self.txtarea.insert(END, f"\nCustomer Name:{self.c_name.get()}")
        self.txtarea.insert(END, f"\nPhone Number{self.c_phone.get()}")
        self.txtarea.insert(END, f"\n================================")
        self.txtarea.insert(END, f"\nProducts\t\tQTY\t\tPrice")

#=========billArea=================================================
    def bill_area(self):
        if self.c_name.get() == " " or self.c_phone.get() == " ":
            messagebox.showerror("Error", "Customer Details Are Must")
        elif self.medical_price.get() == "Rs. 0.0" and self.grocery_price.get() == "Rs. 0.0" and self.cold_drinks_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Purchased")
        else:
            self.welcome_bill()

    # ==============Grocery============================
        if self.milk.get() != 0:
            self.txtarea.insert(END, f"\n Milk\t\t{self.milk.get()}\t\t{self.milk_p}")
        if self.oreo.get() != 0:
            self.txtarea.insert(END, f"\n Oreo\t\t{self.oreo.get()}\t\t{self.o_p}")
        if self.yoghurt.get() != 0:
            self.txtarea.insert(END, f"\n Yoghurt\t\t{self.yoghurt.get()}\t\t{self.y_p}")
        if self.cadbury.get() != 0:
            self.txtarea.insert(END, f"\n Cadbury\t\t{self.cadbury.get()}\t\t{self.cad_p}")
        if self.coffee.get() != 0:
            self.txtarea.insert(END, f"\n Coffee\t\t{self.coffee.get()}\t\t{self.coffee_p}")
        if self.tea.get() != 0:
            self.txtarea.insert(END, f"\n Tea\t\t{self.tea.get()}\t\t{self.tea_p}")
    # ==============Grocery============================
        if self.rice.get() != 0:
            self.txtarea.insert(END, f"\n Rice\t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_f_o_p}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n Wheat\t\t{self.wheat.get()}\t\t{self.g_w_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n Daal\t\t{self.daal.get()}\t\t{self.g_d_p}")
        if self.flour.get() != 0:
            self.txtarea.insert(END, f"\n Flour\t\t{self.flour.get()}\t\t{self.g_f_p}")
        if self.maggi.get() != 0:
            self.txtarea.insert(END, f"\n Maggi\t\t{self.maggi.get()}\t\t{self.g_m_p}")
        #================ColdDrinks==========================
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n Sprite\t\t{self.sprite.get()}\t\t{self.c_d_s_p}")
        if self.water.get() != 0:
            self.txtarea.insert(END, f"\n Sanitizer\t\t{self.limka.get()}\t\t{self.c_d_l_p}")
        if self.mazza.get() != 0:
            self.txtarea.insert(END, f"\n Mazza\t\t{self.mazza.get()}\t\t{self.c_d_m_p}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n Dettol\t\t{self.coke.get()}\t\t{self.c_d_c_p}")
        if self.fanta.get() != 0:
            self.txtarea.insert(END, f"\n Fanta\t\t{self.newsprin.get()}\t\t{self.c_d_f_p}")
        if self.mountain_duo.get() != 0:
            self.txtarea.insert(END, f"\n Mountain Duo\t\t{self.sanitizer.get()}\t\t{self.c_m_d}")
            self.txtarea.insert(END, f"\n--------------------------------")
        # ===============taxes==============================
        if self.grocery_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Grocery Tax\t\t\t{self.grocery_tax.get()}")
        if self.cold_drinks_tax.get() != '0.0':
            self.txtarea.insert(END, f"\n Cold Drinks Tax\t\t\t{self.cold_drinks_tax.get()}")

        self.txtarea.insert(END, f"\n Total Bil:\t\t\t Rs.{self.total_bill}")
        self.txtarea.insert(END, f"\n--------------------------------")
        self.save_bill()

    #=========savebill============================
    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op > 0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("Billing System\\bills"+str(self.bill_no.get())+".txt", "x")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved", f"Bill no:{self.bill_no.get()} Saved Successfully")
        else:
           return

    # ===================find_bill================================
    def find_bill(self):
        present = "no"
        for i in os.listdir("Billing System\\bills"):
            if i.split('.')[0] == self.search_bill.get():
                f1 = open(f"Billing System\\bills{i}", "r")
                self.txtarea.delete("1.0", END)
                for d in f1:
                    self.txtarea.insert(END, d)
                    f1.close()
                present = "yes"
        if present == "no":
            messagebox.showerror("Error", "Invalid Bill No")

    # ======================clear-bill======================
    def clear_data(self):
        op = messagebox.askyesno("Clear", "Do you really want to Clear?")
        if op > 0:
    # ============grocery==============================
            self.milk.set(0)
            self.oreo.set(0)
            self.yoghurt.set(0)
            self.cadbury.set(0)
            self.coffee.set(0)
            self.tea.set(0)
    # ============grocery==============================
            self.rice.set(0)
            self.food_oil.set(0)
            self.wheat.set(0)
            self.daal.set(0)
            self.flour.set(0)
            self.maggi.set(0)
    # =============coldDrinks=============================
            self.sprite.set(0)
            self.water.set(0)
            self.mazza.set(0)
            self.coke.set(0)
            self.fanta.set(0)
            self.mountain_duo.set(0)
    # ====================taxes================================
            self.grocery_price.set("")
            self.cold_drinks_price.set("")

            self.grocery_tax.set("")
            self.cold_drinks_tax.set("")

            self.c_name.set("")
            self.c_phone.set("")

            self.bill_no.set("")
            x = random.randint(1000, 9999)
            self.bill_no.set(str(x))

            self.search_bill.set("")
            self.welcome_bill()

    # ===========exit=======================
    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op > 0:
            self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()