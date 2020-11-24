# This is a Library Management System embedded within,
# a GUI made with a Python Supported Library Tkinter.
# The interface is quite simple and easy to understand, we basically have
# a login first, pretty simple you register if not and login if you had already.
# Once logged in it just gives you a bunch of options to perform different functions.
# These functions consists all of the ones necessary to run a library,
# which certainly are :- 
#
# Adding Books to the Library
# Removing Books from the Library
# Viewing all the Books of the Library 
# Searching a book in the Library  
# Issueing a book to a student

 

from tkinter import *
from tkinter import messagebox


def home():


    root = Tk()
    root.geometry("500x400")
    root.title("Library")

    Canvas1 = Canvas(root,bg="#FFF7EE",height=600,width=600)
    Canvas1.pack()

    #========================== Buttons
    
    regbtn = Button(Canvas1,text="Register",bg="black",fg="white",command=register)
    logbtn = Button(Canvas1,text="Login",bg="black",fg="white",command=login)
    quitbtn = Button(Canvas1,text="Close",bg="black",fg="white",command=root.destroy)

    regbtn.place(relx=0.33,rely=0.34,relwidth=0.29,relheight=0.11)
    logbtn.place(relx=0.33,rely=0.45,relwidth=0.29,relheight=0.11)
    quitbtn.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.075)

    #=========================== Label & Label Frame
    homeframe = Frame(Canvas1,height=70,width=250,bg="#0B0321")
    homeframe.place(relx=0.22,rely=0.02)

    homelabel = Label(homeframe,text="Hello, User")
    homelabel.place(relx=0.04,rely=0.1,height=55,width=230)


    root.mainloop()



def register():
    
    global root1

    root1 = Tk()
    root1.geometry("600x500")
    root1.title("Register")

    Canvas2 = Canvas(root1,bg="#FFF7EE",height=600,width=600)
    Canvas2.pack()
    
    #==========================Entry Fields & Entry Frame

    entryframe = Frame(Canvas2,height=150,width=400,bg="#000825")
    entryframe.place(relx=0.2,rely=0.3)

    #For making use in whole code
    global fname_entry,lname_entry,password_entry

    
    fname_entry = Entry(entryframe,width=44)
    lname_entry = Entry(entryframe,width=44)
    password_entry = Entry(entryframe,width=44)
    password_entry.config(show="•")

    fname_lb = Label(entryframe,text="First Name",height=2,width=9,bg="#000825",fg="white")
    lname_lb = Label(entryframe,text="Last Name",height=2,width=9,bg="#000825",fg="white")
    password_lb = Label(entryframe,text="Password",height=2,width=9,bg="#000825",fg="white")
    
    #---------------------------------------

    fname_lb.place(relx=0.01,rely=0.1)
    lname_lb.place(relx=0.01,rely=0.3)
    password_lb.place(relx=0.01,rely=0.5)

    fname_entry.place(relx=0.3,rely=0.15)
    lname_entry.place(relx=0.3,rely=0.35)
    password_entry.place(relx=0.3,rely=0.57)
    
    #==========================Label & Label Frame
    
    regframe = Frame(Canvas2,height=70,width=250,bg="#0B0321")
    regframe.place(relx=0.32,rely=0.02)

    reglabel = Label(regframe,text="Please Register")
    reglabel.place(relx=0.04,rely=0.1,height=55,width=230)

    #==========================Buttons

    regbtn = Button(root1,text="Submit",command=save_reg,bg="black",fg="white")
    regbtn.place(relx=0.37,rely=0.8,relwidth=0.29,relheight=0.11)

    root1.mainloop()


def save_reg():
    details = fname_entry.get() + " " + lname_entry.get() + " " + password_entry.get()
    acc = open("accounts.txt","a+")
    acc.write(details+"\n")
    root1.destroy()


def login():

    global root2

    root2 = Tk()
    root2.title("Login")
    root2.geometry("600x500")

    Canvas3 = Canvas(root2,bg="#FFF7EE",height=600,width=600)
    Canvas3.pack()
    
    #=============================Entry Fields & Entry Frame
    
    logframe = Frame(Canvas3,height=150,width=400,bg="#000825")
    logframe.place(relx=0.2,rely=0.3)

    #For using to login
    global logfname,loglname,logpass

    logfname = Entry(logframe,width=44)
    loglname = Entry(logframe,width=44)
    logpass = Entry(logframe,width=44)
    logpass.config(show="•")

    logfname_lb = Label(logframe,text="First Name",height=2,width=9,bg="#000825",fg="white")
    loglname_lb = Label(logframe,text="Last Name",height=2,width=9,bg="#000825",fg="white")
    logpass_lb = Label(logframe,text="Password",height=2,width=9,bg="#000825",fg="white")

    #------------------------------------------
    
    logfname.place(relx=0.3,rely=0.15)
    loglname.place(relx=0.3,rely=0.35)
    logpass.place(relx=0.3,rely=0.57)

    logfname_lb.place(relx=0.01,rely=0.1)
    loglname_lb.place(relx=0.01,rely=0.3)
    logpass_lb.place(relx=0.01,rely=0.5)

    #=======================================Lablel & Label Frame
    
    logframe = Frame(Canvas3,height=70,width=250,bg="#0B0321")
    logframe.place(relx=0.32,rely=0.02)

    loglabel = Label(logframe,text="Fill Details")
    loglabel.place(relx=0.04,rely=0.1,height=55,width=230)

    #=====================================Button and Main Login
    

    #==========================================================
    #==========================================================   


    def libmenu():

    
        root2.destroy()
        
        root3 = Tk()
        root3.title("Library Menu")
        root3.geometry("500x600")

        Canvas4 = Canvas(root3,bg="#FFF7EE",height=600,width=600)
        Canvas4.pack()
    
    #===============================Buttons & Button Frame
    
        def addbook():
        
            root4 = Tk()
            root4.geometry("600x500")
            root4.title("Add Book")
            Canvas5 = Canvas(root4,bg="#FFF7EE",height=600,width=600)
            Canvas5.pack()

            adframe =  Frame(Canvas5,height=70,width=250,bg="#0B0321")
            adframe.place(relx=0.3,rely=0.02)
            adlabel = Label(adframe,text="Please Fill in Details")
            adlabel.place(relx=0.04,rely=0.1,height=55,width=230)

            bookframe = Frame(Canvas5,bg="#0B0321",height=300,width=450)
            bookframe.place(relx=0.13,rely=0.235,relwidth=0.76)

            #----------------------------------
    
            isbnlabel = Label(bookframe,text="ISBN(13 digits)",height=3,width=10,bg="#0B0321",fg="white")
            bknamelabel = Label(bookframe,text="Book Name",height=3,width=9,bg="#0B0321",fg="white")
            authlabel = Label(bookframe,text="Author",height=3,width=9,bg="#0B0321",fg="white")
            pricelabel = Label(bookframe,text="Price",height=3,width=9,bg="#0B0321",fg="white")

            isbn_entry = Entry(bookframe,width=50)
            bkname_entry = Entry(bookframe,width=50)
            auth_entry = Entry(bookframe,width=50)
            price_entry = Entry(bookframe,width=50)

            isbnlabel.grid(row=0,column=0,sticky=W)
            bknamelabel.grid(row=1,column=0,sticky=W)
            authlabel.grid(row=2,column=0,sticky=W)
            pricelabel.grid(row=3,column=0,sticky=W)

            isbn_entry.place(relx=0.3,rely=0.06)
            bkname_entry.place(relx=0.3,rely=0.3)
            auth_entry.place(relx=0.3,rely=0.56)
            price_entry.place(relx=0.3,rely=0.8 )
    
            #----------------------------------

            def addbook_main():
                
                isbn = isbn_entry.get()
                bkname = bkname_entry.get()
                author = auth_entry.get()
                price = price_entry.get()

                lib = open("books.txt","a+")

                bkdetail = isbn + " "  + bkname + " " + author + " " + price
                lib.write(bkdetail+"\n")
                root4.destroy()

            subbtn = Button(Canvas5,text="Submit",command=addbook_main,bg="black",fg="white")
            quitbtn2 = Button(Canvas5,text="Close",command=root4.destroy,bg="black",fg="white")
            subbtn.place(relx=0.25,rely=0.9,relwidth=0.25,relheight=0.075)
            quitbtn2.place(relx=0.55,rely=0.9,relwidth=0.25,relheight=0.075)
        
            root4.mainloop()


        def delbook():
    
            root5 = Tk()
            root5.title("Delete Book")
            root5.geometry("600x400")

            Canvas6 = Canvas(root5,bg="#FFF7EE",height=600,width=600)
            Canvas6.pack()

            delframe = Frame(Canvas6,height=70,width=250,bg="#0B0321")
            delframe.place(relx=0.3,rely=0.02)
            dellabel = Label(delframe,text="Please Type ISBN")
            dellabel.place(relx=0.04,rely=0.1,height=55,width=230)
            #--------------------------------------------------
        
            ISBNframe = Frame(Canvas6,bg="#0B0321",height=150,width=450)
            ISBNframe.place(relx=0.13,rely=0.335,relwidth=0.76)
        
            ISBNlabel = Label(ISBNframe,text="ISBN",bg="#0B0321",fg="white")
            ISBN_entry = Entry(ISBNframe,width=44)
            ISBNlabel.place(relx=0.05,rely=0.43)
            ISBN_entry.place(relx=0.3,rely=0.43)

            def del_main():
    
                allbooks = open("books.txt")
                bookdetails = allbooks.readlines()

                clear = open("books.txt","w").close()

                ISBN = ISBN_entry.get()

                
                if ISBN.isdigit() == True:
                    for i in bookdetails:
                        if ISBN in i:
                            bookdetails.remove(i)
            

                newbooks = open("books.txt","a+")
                newbooks.writelines(bookdetails)
                root5.destroy()
                

            delbtn = Button(Canvas6,text="Delete",command=del_main,bg="black",fg="white")
            delbtn.place(relx=0.37,rely=0.8,relwidth=0.29,relheight=0.11)
            root5.mainloop()


        def viewbook():
            v_book = open("books.txt")
            v_info = v_book.readlines()
            v_details = []

            for i in v_info:
                con1 = i.split("\n")
                v_details.append(con1)

            vf_info = []

            for i in range(len(v_details)):
                kon1 = v_details[i][0]
                vf_info.append(kon1)

            temp = []
            for i in vf_info:
                j = i.split(" ")
                temp.append(j)

            def viewbooks():
                print("     Isbn","   |","Name","|","Author","|","Price","|")
                print("-"*42) 
                for i in range(len(vf_info)):
                    print(temp[i][0]+ "   " + temp[i][1]+ "    " +temp[i][2]+ "      " +temp[i][3]+"\n",end="")
                    print()
            viewbooks()


        def searchbook():
        
            root7 = Tk()
            root7.title("Search Book")
            root7.geometry("600x400")
            
            Canvas8 = Canvas(root7,bg="#FFF7EE",height=600,width=600)
            Canvas8.pack()

            #-------------------------

            searchframe = Frame(Canvas8,height=70,width=250,bg="#0B0321")
            searchframe.place(relx=0.3,rely=0.02)
            searchlabel = Label(searchframe,text="Please Type Search Details")
            searchlabel.place(relx=0.04,rely=0.1,height=55,width=230)

            #-----------------------------

            infoframe = Frame(Canvas8,bg="#0B0321",height=150,width=450)
            infoframe.place(relx=0.13,rely=0.335,relwidth=0.76)

            isbn2label = Label(infoframe,text="ISBN",bg="#0B0321",fg="white")
            isbn2_entry = Entry(infoframe,width=44)
            isbn2label.place(relx=0.05,rely=0.2)
            isbn2_entry.place(relx=0.3,rely=0.2)

            bklabel = Label(infoframe,text="Book Name",bg="#0B0321",fg="white")
            bk_entry = Entry(infoframe,width=44)
            bklabel.place(relx=0.05,rely=0.6)
            bk_entry.place(relx=0.3,rely=0.6)

            def search_main():
            
                isbn = isbn2_entry.get()
                bkname = bk_entry.get()

                bksearch = open("books.txt")
                searchdetails = bksearch.readlines()

                for i in searchdetails:
                    if isbn in i and bkname in i:
                        print("Your Search is : ",i)
                root7.destroy()

 
            searchbtn = Button(Canvas8,text="Search",command=search_main,bg="black",fg="white")
            searchbtn.place(relx=0.37,rely=0.8,relwidth=0.29,relheight=0.11)
        
            root7.mainloop()
            
        def issue():
            
            root6 = Tk()
            root6.title("Issue Book")
            root6.geometry("600x500")

            Canvas7 = Canvas(root6,bg="#FFF7EE",height=600,width=600)
            Canvas7.pack()

            #----------------------------

            issueframe = Frame(Canvas7,height=70,width=250,bg="#0B0321")
            issueframe.place(relx=0.3,rely=0.02)
            issuelabel = Label(issueframe,text="Please Type Issue Details")
            issuelabel.place(relx=0.04,rely=0.1,height=55,width=230)

            #------------------------------

            infoframe_issue = Frame(Canvas7,bg="#0B0321",height=150,width=450)
            infoframe_issue.place(relx=0.13,rely=0.335,relwidth=0.76)


            isbn3label = Label(infoframe_issue,text="ISBN",bg="#0B0321",fg="white")
            isbn3_entry = Entry(infoframe_issue,width=48)
            isbn3label.place(relx=0.05,rely=0.15)
            isbn3_entry.place(relx=0.3,rely=0.15)

            bklabel = Label(infoframe_issue,text="Book Name",bg="#0B0321",fg="white")
            bk_entry = Entry(infoframe_issue,width=48)
            bklabel.place(relx=0.05,rely=0.42)
            bk_entry.place(relx=0.3,rely=0.42)

            stulabel = Label(infoframe_issue,text="Name Of Student",bg="#0B0321",fg="white")
            stu_entry = Entry(infoframe_issue,width=48)
            stulabel.place(relx=0.05,rely=0.7)
            stu_entry.place(relx=0.3,rely=0.7)


            def issue_main():

                issuefile = open("books_issued.txt","a+")

                issue_isbn = isbn3_entry.get()
                issue_bk = bk_entry.get()
                name = stu_entry.get()

                
                var = issue_isbn + " " + issue_bk + " " + name

                issuefile.write(var+"\n")
                root6.destroy()

            searchbtn = Button(Canvas7,text="Issue",command=issue_main,bg="black",fg="white")
            searchbtn.place(relx=0.37,rely=0.8,relwidth=0.29,relheight=0.11)

            root6.mainloop()


        libframe0 = Frame(Canvas4,height=70,width=250,bg="#0B0321")
        libframe0.place(relx=0.22,rely=0.02)
        liblabel = Label(libframe0,text="Please Choose from Below")
        liblabel.place(relx=0.04,rely=0.1,height=55,width=230)


        libframe = Frame(Canvas4,height=350,width=230,bg="#000825")
        libframe.place(relx=0.26,rely=0.28,relheight=0.5)

        addbk = Button(libframe,text="Add Books",command=addbook,bg="black",fg="white")
        delbk = Button(libframe,text="Delete Books",command=delbook,bg="black",fg="white")
        viewbk = Button(libframe,text="View Books",command=viewbook,bg="black",fg="white")
        searchbk = Button(libframe,text="Search Books",command=searchbook,bg="black",fg="white")
        issuebk = Button(libframe,text="Issue Book to Student ",command=issue,bg="black",fg="white")
        quitbtn = Button(Canvas4,text="Close",command=root3.destroy,bg="black",fg="white")

        addbk.place(relx=0.004,rely=0.003,relwidth=0.99,relheight=0.2)
        delbk.place(relx=0.004,rely=0.2,relwidth=0.99,relheight=0.2)
        viewbk.place(relx=0.004,rely=0.4,relwidth=0.99,relheight=0.2)
        searchbk.place(relx=0.004,rely=0.6,relwidth=0.99,relheight=0.2)
        issuebk.place(relx=0.004,rely=0.8,relwidth=0.99,relheight=0.2)
        quitbtn.place(relx=0.35,rely=0.9,relwidth=0.25,relheight=0.075)

    
        root3.mainloop()

    def errormessage():
        root2.destroy()
        messagebox.showinfo("Error", "You are not registered")

    #===========================================================
    #===========================================================



    def login_main():
        acc = open("accounts.txt")
        info = acc.readlines()
        details = []
        for i in info:
            con = i.split("\n")
            details.append(con)

        fin_info = []

        for i in range(len(details)):
            kon = details[i][0]
            fin_info.append(kon)

        tempstring = logfname.get() + " " + loglname.get() + " " + logpass.get()
        
        ctr = 0
        for i in fin_info:
            if tempstring == i:
                ctr += 1
            else:
                ctr = ctr
        
        if ctr == 1:
            libmenu()
        else:
            errormessage()
        

    logbtn = Button(root2,text="Submit",command=login_main,bg="black",fg="white")
    logbtn.place(relx=0.37,rely=0.8,relwidth=0.29,relheight=0.11)




    root2.mainloop()

home()