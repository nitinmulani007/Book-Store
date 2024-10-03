import pickle
import os

class library():
    def __init__(self):
        self.Serial_no=0
        self.Book_Name=""
        self.Book_Type=""
        self.Writter=""
        self.Book_Publisher=""
        self.Rating=""
        self.year=0
        self.Issue_Date=0
        self.Duration=0
        self.PNo=0
        self.Qty=0
    def getname(self):
        print "Hindi Writers","English Writers"
   
        print "1.Munshi Premchand"," "*50,"11.Plato"
        print "2.A P J Abdul Kalam"," "*50,"12.Issac Newton"
        print "3.Dr. S Radhakrishan"," "*50,"13.Helen Keller"
        print "4.Yashpal"," "*50,"14.Adolf Hitler"
        print "5.Surdas"," "*50,"15.J K Rowling"c=int(raw_input("Enter the writer code="))
        
        if a==1:
            return "Munshi Premchand"
        elif a==2:
           a
                        
        
    def inputdata(self):
        self.Serial_no=int(raw_input("enter the serial no"))
        self.Book_Name=raw_input("Enter the name")
        self.Book_Type=raw_input("Enter the book type")
        self.Writter=raw_input("Enter the  Writter name")
        self.Book_Publisher=raw_input("Enter the Publisher name")
        self.Rating=int(raw_input("Enter the rating"))
        self.Year=int(raw_input("Enter the year"))
        self.Issue_Date=raw_input("Enter the Issuing date ") 
        self.Duration=raw_input("Enter the Duration")
        self.PNo=int(raw_input("Enter the Phone number"))
        self.Qty=int(raw_input("Enter the quantity"))
    def showdata(self):
        print self.Serial_no,"="
        print self.Book_Name,"="
        print self.Book_Type,"="
        print self.Writter,"="
        print self.Book_Publisher,"="
        print self.Rating,"="
        print self.Year,"="
        print self.Issue_Date,"="
        print self.Duration,"="
        print self.PNo,"="
        print self.Qty,"="
a=library()
a1=library()

def add():
      file=open("library.dat","ab")
      a.inputdata()
      pickle.dump(a,file)
      file.close()

def display():
     try:
        file=open("library.dat","rb")
        print("Information related to the Library")
        while True:
             a=pickle.load(file)
             a.showdata()
     except EOFError:
         pass
         file.close()
     except IOError:
         print"File does not exist"

def delete():
      try:
         file1=open("library.dat","rb")
         file2=open("temp.dat","wb")
         r=int(raw_input("Enter the serial number "))
         while True:
           a=pickle.load(file1)
           if a.Serial_no!=r:
              pickle.dump(a,file2)
      except EOFError:
         pass
         file1.close()
         file2.close()
         os.remove("library.dat")
         os.rename("temp.dat","library.dat")
      except IOError:
        print "File does not exist"

def modify():
      try:
         file1=open("library.dat","rb")
         file2=open("temp.dat","wb")
         print "Enter the details for the library that you want to modify"
         a1.inputdata()
         while True:
             a=pickle.load(file1)
             if a1.serial_no==a.serial_no:
                 pickle.dump(a1,file2)
             else:
                 pickle.dump(a.file2)
      except EOFError:
          pass
          file1.close()
          file2.close()
          os.remove("library.dat")
          os.rename("temp.dat","library")
      except IOError:
          print "File does not exist"

def search():
      try:
         file=open("library","rb")
         x=raw_input("Enter the serial number to be searched:")
         found=0
         while True:
             a=pickle.load(file)
             if a.PNo==x:
                 a.Output()
                 found=1
      except EOFError:
         if found==0:
             print "serial number not find"
         pass
         file.close()
      except IOError:
         print "File does not exist"

while True:
    print "Welcome to the  Library"
    print "1. Customer"
    print "2. Billing";
    c=int(raw_input("Enter your choice"))
    if c==1:
        print "Book_Type"
        print "1. Add "
        print "2. Display "
        print "3. Delete "
        print "4. Modify "
        print "5. Search "
        ch=int(raw_input("enter your choice= "))
        if ch==1:
            add()
        elif ch==2:
            display()
        elif ch==3:
            delete()
        elif ch==4:
            modify()
        elif ch==5:
            search()
        elif c==2:
             exit()
   
        print "A. TYPE OF BOOK "
        print "B. Writter Name "
        y=raw_input("enter your choice ")
        if y=="A":
            print "TYPE OF BOOK "
            print " 1. Autobiography"
            print " 2. Biography"
            print " 3. Literature"
            print " 4. Chemistry"
            print " 5. Physics"
            print " 6. Electronics"
            print " 7. Maths"
            print " 8. Histoy"
            print " 9. Civics"
            print "10. Geography"
            print "11. Adventure"
            print "12. Tails"
            print "13. Computer Science"
            print "14. Business Studies"
            print "15. Economics"
            print "16. Accountacy"
            print "17. Novels"
            print "18. Magzine"
            print "19. Grammar"
            print "20. Astrology"
            print "21. Atlas"
            print "22. Epics"
            print "23. Gerenal Knowledge"
            print "24. Phsical Education"
            print "25. G Book O "
            
        elif y=="B":
            print "Writter Name"
            print " 1. Helen Keller"
            print " 2. J K Rowling"
            print " 3. Dean Koontz"
            print " 4. Pt. Jahawarlal Nehru"
            print " 5. Dr. A P J Abdul Kalam"
            print " 7. Mike Roggeds"
            print " 8. Munshi Premchand"
            print " 9. Ved Vyas"
            print "10. Sir Rabindranath Tagore "
            print "11. Sir Albert Einstein"
            print "12. ADOLF HITLER"
            print "13. A. L. BASHAM"
            print "14. ARISTOTLE"
            print "15. Sir SACHIN TENDULKAR"
            print "16. SURDAS"
            print "17. KULDIP NAYAR"
            print "18. INDRA GANDHI"
            print "19. PLATO"
            print "20. LEO TOLSTOY"
            print "21. MAO-TSE TUNG"
            print "22. MAXIM GORKY"
            print "23. DANTE"
            print "24. GUNNAR MYRDAL"
            print "25. Sir ISSAC NEWTON"
            print "26. DR. S RADHAKRISHAN"
            print "27. YASHPAL"
            print "28. SARJINI NAIDU"
        else:
            exit()

    elif c==2:
        print "1. Add "
        print "2. Display "
        print "3. Delete "
        print "4. Modify "
        print "5. Search "
        ch=int(raw_input("enter your choice "))
        if ch==1:
            add()
        elif ch==2:
            display()
        elif ch==3:
            delete()
        elif ch==4:
            modify()
        elif ch==5:
            search()
        elif c==2:
             exit()
                

class billing():
    def __init__(self):
        self.Billno=000
        self.Bill_date=""
        self.Customer_Name=""
        self.Address=""
        self.Phone_No=""
        self.b_name=00
        self.SP=00
        self.Qty=00
        self.Total=00
        self.Tax=00
        self.NetAmount=00
    def billingdata(self):
        self.Billno=int(raw_input("Enter the bill number"))
        self.Bill_date=raw_input("Enter the billing date")
        self.Customer_Name=raw_input("Enter the customer name")
        self.Address=raw_input("Enter the address")
        self.Phone_No=int(raw_input("Enter the phone number"))
        self.p_name=raw_input("Enter the product number")
        self.SP=int(raw_input("enter the sp"))
        self.Qty=int(raw_input("Enter the quantity"))
        self.Total=self.SP*self.Qty
        self.Tax=self.Total*0.10
        self.NetAmount=self.Total+self.Tax
    def printdata(self):
        print "-"*130
        print "%7s" % ("|"+str(self.Bill_no)).ljust(7),
        print "%10s" % ("|"+str(self.Bill_date)).ljust(10),
        print "%15s" % ("|"+str(self.Customer_Name)).ljust(15),
        print "%20s" % ("|"+str(self.Address)).ljust(20),
        print "%12s" % ("|"+str(self.Phone_No)).ljust(12),
        print "%5s" % ("|"+str(self.PNo)).ljust(5),
        print "%10s" % ("|"+str(self.SP)).ljust(10),
        print "%10s" % ("|"+str(self.Qty)).ljust(10),
        print "%10s" % ("|"+str(self.Total)).ljust(10),
        print "%10s" % ("|"+str(self.Tax)).ljust(10), 
        print "%10s" % ("|"+str(self.NetAmount)).ljust(10),
        print "|"
        print "<<<have a good day>>>"
b=billing()
b1=billing()

def badd():
    file=open("billing.dat","ab")
    b.billingdata()
    pickle.dump(b,file)
    file.close()

def bdisplay():
    try:
        file=open("billing.dat","rb")
        print("Information related to the Billing")
        print "-"*130
        print                             "<<<Welcome to Library>>>"
        print "%15s" % "|BILL no",self.Billno.ljust(15)
        print "%15s" % "|Bill date",self.Bill_date.ljust(15)
        print "%15s" % "|Customer name",self.Customer_Name.ljust(15)         
        print "%15s" % "|Address",self.Address.ljust(15)                   
        print "%15s" % "|p_name",self.p_name.ljust(15)
        print "%15s" % "|SP",self.SP.ljust(15)          
        print "%15s" % "|Qty",self.Qty.ljust(15)
        print "%15s" % "|Total",self.Total.ljust(15)         
        print "%15s" % "|Tax",self.Tax.ljust(15)          
        print "%15s" % "|NetAmount",self.NetAmount.ljust(15)

        while True:
            b=pickle.load(file)
            b.printdata()
    except EOFError:
            pass
            file.close
    except IOError:
            print"File does not exist"

def bdelete():
    try:
        file1=open("billing.dat","rb")
        file2=open("temp.dat","wb")
        r=int(raw_input("Enter the product number "))
        while True:
            b=pickle.load(file1)
            if b.b_name!=r:
                pickle.dump(b,file2)
    except EOFError:
        pass
        file1.close()
        file2.close()
        os.remove("billing.dat")
        os.rename("temp.dat","billing")
    except IOError:
        print "File does not exist"

def bmodify():
    try:
        file1=open("billing.dat","rb")
        file2=open("temp.dat","wb")
        print "Enter the details for the billing that you want to modify"
        b1.billingdata()
        while True:
            b=pickle.load(file1)
            if b1.b_name==b.b_name:
                pickle.dump(1,file2)
            else:
                pickle.dump(b,file2)
    except EOFError:
        pass
        file1.close()
        file2.close()
        os.remove("billing.dat")
        os.rename("temp.dat","billing")
    except IOError:
        print "File does not exist"

def bsearch():
    try:
        file=open("billing","rb")
        x=int(raw_input("Enter the BOOK to be searched:"))
        found=0
        while True:
            b=pickle.load(file)
            if b.b_name==x:
                b.printdata()
                found=1
    except EOFError:
        if found==0:
            print "Product number not find"
        pass
        file.close()
    except IOError:
        print "File does not exist"

class issue():
    def __init__(self):
        self.Registration_no=0
        self.Registration_Date
        self.Customer_Name=""
        self.Address=""
        self.Phone_No=""
        self.Serial_no=0
        self.Qty=0
        self.Issuing_date=0
        self.Duration=0
        
    def inputdata(self):
        self.Registration_no=int(raw_input("Enter the Registration number"))
        self.Registration_date=int(raw_input("Enter the Registration date"))
        self.Customer_Name=raw_input("Enter the customer name")
        self.Address=raw_input("Enter the address")
        self.Phone_No=int(raw_input("Enter the phone number"))
        self.Serial_no=int(raw_input("Enter the Serial number"))
        self.Qty=int(raw_input("Enter the quantity"))
        self.Issuing_Date=int(raw_input("Enter the issuing date"))
        self.Duration=int(raw_input("Enter the Duration time"))
        
    def showdata(self):
        print self.Registration_no
        print self.Registration_date
        print self.Customer_Name
        print self.Address
        print self.Phone_No
        print self.Serial_no
        print self.Qty    
        print self.Issuing_Date
        print self.Duration
i=issue()
i1=issue()
    
