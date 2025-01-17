from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter
import datetime
from distutils.core import setup

class librarymanagementsystem:
    def __init__(self,root) :
        self.root=root
        self.root.title("Library management system")
        self.root.geometry("1550x800+0+0")
        
        #===================================Variable==========================================
        
        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.adress1_var=StringVar()
        self.adress2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.author_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()
        
        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="lightblue",fg="black",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)
        
        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="lightblue")
        frame.place(x=0,y=130,width=1530,height=400)
        #===================================Data Frame Left==========================================
        DataFrameLeft=LabelFrame(frame, text="Library member information", bg="lightblue", fg="black",bd=12, relief=RIDGE, font=("times new roman",13,"bold"))
        DataFrameLeft.place(x=0, y=5,width=900,height=350)
        
        lblMemebr=Label(DataFrameLeft,bg="lightblue", text="Member type", font=("times new roman", 13, "bold"), padx=2, pady=6)
        lblMemebr.grid(row=0, column=0, sticky=W,)
        
        comMember=ttk.Combobox(DataFrameLeft, font=("times new roman", 13, "bold"), width=27, state="readonly", textvariable=self.member_var)
        comMember["value"]=("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1)
        
        lblPRN_NO=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="PRN_NO:", padx=2, bg="light blue")
        lblPRN_NO.grid(row=1, column=0, sticky=W)
        txtPRN_NO=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable =self.prn_var)
        txtPRN_NO.grid(row=1, column=1)
        
        lblTitle=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="ID No.", padx=2, pady=6, bg="light blue")
        lblTitle.grid(row=2, column=0, sticky=W)
        txtTitle=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29)
        txtTitle.grid(row=2, column=1)
        
        lblFirstName=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="First Name", padx=2, pady=6, bg="light blue")
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.firstname_var)
        txtFirstName.grid(row=3, column=1)
        
        lblLastName=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Last Name", padx=2, pady=6, bg="light blue")
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.lastname_var)
        txtLastName.grid(row=4, column=1)
        
        lblAdress1=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Adress1", padx=2, pady=6, bg="light blue")
        lblAdress1.grid(row=5, column=0, sticky=W)
        txtAdress1=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.adress1_var)
        txtAdress1.grid(row=5, column=1)
        
        lblAdress2=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Adress2", padx=2, pady=6, bg="light blue")
        lblAdress2.grid(row=6, column=0, sticky=W)
        txtAdress2=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), textvariable=self.adress2_var, width=29)
        txtAdress2.grid(row=6, column=1)
        
        lblPostCode=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Post Code", padx=2, pady=6, bg="light blue")
        lblPostCode.grid(row=7, column=0, sticky=W)
        txtPostCode=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.postcode_var)
        txtPostCode.grid(row=7, column=1)
        
        lblMobile=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Mobile", padx=2, pady=6, bg="light blue")
        lblMobile.grid(row=8, column=0, sticky=W)
        txtMobile=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), textvariable=self.mobile_var, width=29)
        txtMobile.grid(row=8, column=1)
        
        lblBookID=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Book ID:", padx=2, pady=6, bg="light blue")
        lblBookID.grid(row=0, column=2, sticky=W)
        txtBookID=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.bookid_var)
        txtBookID.grid(row=0, column=3)
        
        lblBookTitle=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Book Title:", padx=2, pady=6, bg="light blue")
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.booktitle_var)
        txtBookTitle.grid(row=1, column=3)
        
        lblAuthor=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Author Name:", padx=2, pady=6, bg="light blue")
        lblAuthor.grid(row=2, column=2, sticky=W)
        txtAuthor=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.author_var)
        txtAuthor.grid(row=2, column=3)
        
        lblDateBorrowed=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Date Borrowed:", padx=2, pady=6, bg="light blue")
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.dateborrowed_var)
        txtDateBorrowed.grid(row=3, column=3)
        
        lblDateDue=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Date Due:", padx=2, pady=6, bg="light blue")
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.datedue_var)
        txtDateDue.grid(row=4, column=3)
        
        lblDaysOnBook=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Days On Book:", padx=2, pady=6, bg="light blue")
        lblDaysOnBook.grid(row=5, column=2, sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.daysonbook_var)
        txtDaysOnBook.grid(row=5, column=3)
        
        lblLateReturnFile=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Late Return Fine:", padx=2, pady=6, bg="light blue")
        lblLateReturnFile.grid(row=6, column=2, sticky=W)
        txtLateReturnFine=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.lateratefine_var)
        txtLateReturnFine.grid(row=6, column=3)
        
        lblDateOverDue=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Data Over Due:", padx=2, pady=6, bg="light blue")
        lblDateOverDue.grid(row=7, column=2, sticky=W)
        txtDateOverDue=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.dateoverdue_var)
        txtDateOverDue.grid(row=7, column=3)
        
        lblActualPrice=Label(DataFrameLeft, font=("times new roman", 13, "bold"), text="Actual Price:", padx=2, pady=6, bg="light blue")
        lblActualPrice.grid(row=8, column=2, sticky=W)
        txtActualPrice=Entry(DataFrameLeft, font=("times new roman", 13, "bold"), width=29, textvariable=self.finalprice_var)
        txtActualPrice.grid(row=8, column=3)
        
        #===================================Data Frame Right==========================================
        
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="lightblue",fg="black",bd=12,relief=RIDGE,font=("times new roman",13,"bold"))
        DataFrameRight.place(x=910, y=5,width=540,height=350)
        
        self.txtbox=Text(DataFrameRight, font=("times new roman",12,"bold"), width=32, height=16, padx=2, pady=6)
        self.txtbox.grid(row=0, column=2)
        
        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")
        
        listBooks=["Machine Learning", "Advance Python", "My SQL", "Machine Python", "Intro to Machine learning", 
                   "My Python", "Python Coursebook", "Intro to Python", "Data Science", "Data Analytics", 
                   "Data Management", "Problem Solving Using C", "Fundamentals of Computer Organization.",
                   "Programming using C#", "Operating System", "OOPS using C++", "Computer Graphics", "Software Engineering",
                   "Object-Oriented Modeling and Design Patterns", "Advance Java Programming", "Analysis & Design of Algorithm"]
        
        def SelectBook(event=""):
            value=str(listBox.get(listBox.curselection())) 
            x=value

            if (x=="Machine Learning"): 
                self.bookid_var.set("BKID5454") 
                self.booktitle_var.set("Machine Learning") 
                self.author_var.set("Paul Berry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 788")
                
            elif (x=="Advance Python"): 
                self.bookid_var.set("BKID5400") 
                self.booktitle_var.set("Advace Programming") 
                self.author_var.set("Phil Dumphey")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 587")
        
         
                
            elif (x=="My SQL"): 
                self.bookid_var.set("BKID4896") 
                self.booktitle_var.set("My SQL") 
                self.author_var.set("Barney Stinson")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 489")
                
            elif (x=="Machine Python"): 
                self.bookid_var.set("BKID5898") 
                self.booktitle_var.set("Machine Learning") 
                self.author_var.set("Joey Tribbyani")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 635") 
                
            elif (x=="Intro to Machine learning"): 
                self.bookid_var.set("BKID7896") 
                self.booktitle_var.set("Intro to Machine learning") 
                self.author_var.set("Rachel Green")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 269")
                
            elif (x=="My Python"): 
                self.bookid_var.set("BK8489") 
                self.booktitle_var.set("My Python") 
                self.author_var.set("Amy Santiago")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 357")
                
            elif (x=="Python Coursebook"): 
                self.bookid_var.set("BK7193") 
                self.booktitle_var.set("Python Coursebook") 
                self.author_var.set("Ross Geller")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs. 719")
                
            elif (x=="Data Sciece"): 
                self.bookid_var.set("BK7892") 
                self.booktitle_var.set("Data Sciece") 
                self.author_var.set("Clay Jensen")
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1-d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("No")
                self.finalprice_var.set("Rs.598")
                
                
        listBox=Listbox(DataFrameRight, font=("times new roman", 13, "bold"), width=20, height=16)
        listBox.bind("<<ListboxSelect>>", SelectBook)  
        listBox.grid(row=0, column=0, padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END, item)
     
        #===================================Button Frame==========================================
        framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=22, bg="lightblue")
        framebutton.place(x=0, y=530, width=1530, height=60)

        btnAddData = Button(framebutton, command=self.add_data, text="Add Data", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnAddData.grid(row=0, column=0)

        btnShowData = Button(framebutton, command=self.ShowData,text="Show Data", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate = Button(framebutton, command=self.update, text="Update", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(framebutton, command= self.delete, text="Delete", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnDelete.grid(row=0, column=3)

        btnReset = Button(framebutton, command=self.reset, text="Reset", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnReset.grid(row=0, column=4)

        btnExit = Button(framebutton, command=self.iExit, text="Exit", font=("Times New Roman", 13, "bold"), width=23, bg="Black", fg="white")
        btnExit.grid(row=0, column=5)

        
        #===================================Information Frame=====================================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="lightblue")
        FrameDetails.place(x=0,y=590,width=1530,height=200)

        Table_frame= Frame(FrameDetails, bd=6, relief=RIDGE,bg="light blue")
        Table_frame.place(x=0, y=2, width=1460, height=172)
        
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table=ttk.Treeview(Table_frame,column=("memebertype", "prnno", "title","firstname", "lastname","adress1", 
                                                   "adress2", "postid", "mobile", "bookid", "booktitle","author", 
                                                   "dateborrowed", "datedue", "days", "latereturnfine", "dateoverdue", 
                                                   "finalprice"), xscrollcommand=xscroll.set,  yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("memebertype", text="Member Type")
        self.library_table.heading("prnno", text="PRN_NO")
        self.library_table.heading("title", text="Title")
        self.library_table.heading("firstname", text="First Name")  
        self.library_table.heading("lastname", text="Last Name")
        self.library_table.heading("adress1", text="Adress1")
        self.library_table.heading("adress2", text="Adress2")
        self.library_table.heading("postid", text="Post Code")  
        self.library_table.heading("mobile", text="Mobile")
        self.library_table.heading("bookid", text="Book ID")
        self.library_table.heading("booktitle", text="Book Title")
        self.library_table.heading("author", text="Author")  
        self.library_table.heading("dateborrowed", text="Date Borrowed")
        self.library_table.heading("datedue", text="Date Due")
        self.library_table.heading("days", text="Days On Book")
        self.library_table.heading("latereturnfine", text="Late Return Fine")
        self.library_table.heading("dateoverdue", text="Date Over Due")
        self.library_table.heading("finalprice", text="Actual Price")



        self.library_table["show"]="headings" 
        self.library_table.pack(fill=BOTH, expand=1)
        
        self.library_table.column("memebertype", width=100)
        self.library_table.column("prnno", width=100)
        self.library_table.column("title", width=100) 
        self.library_table.column("firstname", width=100)
        self.library_table.column("lastname", width=100) 
        self.library_table.column("adress1", width=100)
        self.library_table.column("adress2", width=100) 
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile", width=106)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle", width=100)
        self.library_table.column("author", width=100)
        self.library_table.column("dateborrowed", width=180) 
        self.library_table.column("datedue", width=100)
        self.library_table.column("days", width=100)
        self.library_table.column("latereturnfine", width=100)
        self.library_table.column("dateoverdue", width=100) 
        self.library_table.column("finalprice", width=100)
        
        self.fetch_data()
        self.library_table.bind("<<TreeviewSelect>>", self.get_cursor)

        
    def add_data(self):
        try:
            # Establish a connection to the MySQL database
            conn = mysql.connector.connect(
                host="127.0.0.1", 
                user="root", 
                password="Asdfghjklp0!", 
                database="anuj_project")
            
            my_cursor = conn.cursor()

            # Construct the INSERT INTO SQL statement
            my_cursor.execute("INSERT INTO library VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                self.member_var.get(),
                self.prn_var.get(),
                self.id_var.get(),
                self.firstname_var.get(),
                self.lastname_var.get(),
                self.adress1_var.get(),
                self.adress2_var.get(),
                self.postcode_var.get(),
                self.mobile_var.get(),
                self.bookid_var.get(),
                self.booktitle_var.get(),
                self.author_var.get(),
                self.dateborrowed_var.get(),
                self.datedue_var.get(),
                self.daysonbook_var.get(),
                self.lateratefine_var.get(),
                self.dateoverdue_var.get(),
                self.finalprice_var.get(),
            ))

        
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Member has been inserted successfully")

        except Exception as e:
            messagebox.showerror("Error", f"Error: {e}")

        finally:
            conn.close()
                
    def update(self):
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Asdfghjklp0!",
            database="anuj_project")

        my_cursor = conn.cursor()

        # In the update function
        update_query = """UPDATE library SET MemberType=%s, PRN_NO=%s, ID=%s, FirstName=%s, LastName=%s, 
                        Adress1=%s, Adress2=%s, PostCode=%s, Mobile=%s, BookID=%s, BookTitle=%s, 
                        Author=%s, DateBorrowed=%s, DateDue=%s, Days=%s, LateReturnFine=%s, 
                        DateOverDue=%s, ActualPrice=%s WHERE PRN_NO=%s"""


        values = (
            self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.adress1_var.get(),
            self.adress2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.author_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get(),
        )

        my_cursor.execute(update_query, values)
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
    
        
        
        messagebox.showinfo("Success", "Member has been updated")

            
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="127.0.0.1", 
            user="root", 
            password="Asdfghjklp0!", 
            database="anuj_project")
            
        my_cursor = conn.cursor()
        my_cursor.execute("select*from library")
        rows=my_cursor.fetchall()
            
        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    def get_cursor(self, event=""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]), 
        self.id_var.set(row[2]), 
        self.firstname_var.set(row[3]), 
        self.lastname_var.set(row[4]),
        self.adress1_var.set(row[5]), 
        self.adress2_var.set(row[6]), 
        self.postcode_var.set(row[7]), 
        self.mobile_var.set(row[8]), 
        self.bookid_var.set(row[9]), 
        self.booktitle_var.set(row[10]), 
        self.author_var.set(row[11]), 
        self.dateborrowed_var.set(row[12]), 
        self.datedue_var.set(row[13]), 
        self.daysonbook_var.set(row[14]), 
        self.lateratefine_var.set(row[15]), 
        self.dateoverdue_var.set(row[16]), 
        self.finalprice_var.set(row[17])

    
    def ShowData(self):
        self.txtbox.delete(1.0, END)
        self.txtbox.insert(END, "Member Type:\t\t" + str(self.member_var.get()) + "\n")
        self.txtbox.insert(END, "PRN No:\t\t" + str(self.prn_var.get()) + "\n") 
        self.txtbox.insert(END, "ID No:\t\t" + str(self.id_var.get()) + "\n")
        self.txtbox.insert(END, "FirstName:\t\t" + str(self.firstname_var.get()) + "\n") 
        self.txtbox.insert(END, "LastName:\t\t" + str(self.lastname_var.get()) + "\n")
        self.txtbox.insert(END, "Address1:\t\t" + str(self.adress1_var.get()) + "\n")
        self.txtbox.insert(END, "Address2: \t\t" + str(self.adress2_var.get()) + "\n")
        self.txtbox.insert(END, "Post Code:\t\t" + str(self.postcode_var.get()) + "\n")
        self.txtbox.insert(END, "Mobile No:\t\t" + str(self.mobile_var.get()) + "\n") 
        self.txtbox.insert(END, "Book ID:\t\t" + str(self.bookid_var.get()) + "\n")
        self.txtbox.insert(END, "Book Title:\t\t" + str(self.booktitle_var.get()) + "\n") 
        self.txtbox.insert(END, "Author:\t\t" + str(self.author_var.get()) + "\n")
        self.txtbox.insert(END, "Date Borrowed:\t\t" + str(self.dateborrowed_var.get()) + "\n") 
        self.txtbox.insert(END, "Date Due:\t\t" + str(self.datedue_var.get()) + "\n") 
        self.txtbox.insert(END, "Days On Book: \t\t" + str(self.daysonbook_var.get()) + "\n")
        self.txtbox.insert(END, "Late Return Fine:\t\t" + str(self.lateratefine_var.get()) + "\n")
        self.txtbox.insert(END, "Date Over Due: \t\t" + str(self.dateoverdue_var.get()) + "\n")
        self.txtbox.insert(END, "Final Price:\t\t" + str(self.finalprice_var.get()) + "\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.adress1_var.set("")
        self.adress2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.author_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtbox.delete("1.0", END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Libray Management System", "Do you want to Exit")
        if iExit>0:
            self.root.destroy()     
        return
    
    def delete(self):
        selected_prn = self.prn_var.get()
        if not selected_prn:
            messagebox.showerror("Error", "Please select a member to delete.")
        else:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this member?")
            if confirmation:
                try:
                    conn = mysql.connector.connect(
                        host="127.0.0.1",
                        user="root",
                        password="Asdfghjklp0!",
                        database="anuj_project"
                    )

                    my_cursor = conn.cursor()
                    query = "DELETE FROM library WHERE PRN_no = %s"
                    value = (selected_prn,)
                    my_cursor.execute(query, value)

                    conn.commit()
                    self.fetch_data()
                    self.reset()
                    conn.close()

                    messagebox.showinfo("Success", "Member has been deleted")
                except Exception as e:
                    messagebox.showerror("Error", f"Error deleting member: {str(e)}")

    
    
if __name__== "__main__":
    root=Tk()
    obj=librarymanagementsystem(root)
    root.mainloop()