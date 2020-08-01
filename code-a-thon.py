import csv


#save the record
def save(data):
    f=open("codeathon1.csv","a+")
    f.write(data[0]+','+data[1]+','+data[2]+','+data[3]+','+data[4]+','+data[5]+','+data[6]+'\n')
    f.close

#get record
def getrecord(ID):
    with open("codeathon1.csv","r")as f:
        for line in f:
            line=line.rstrip()
            emp_name,emp_no,emp_add,street,city,state,pincode=line.split(",")
            if(ID==emp_no):
                return line

#add record
def AddEmployee():
    employee=[]
    emp_name=input("Enter Name:")
    emp_no=(input("Enter empno:"))
    emp_add=input("Enter AddressName:")
    street=input("Enter StreetName:")
    city=input("Enter city:")
    state=input("Enter State:")
    pincode=(input("Enter Pincode:"))
    employee.append(emp_no),employee.append(emp_name),employee.append(emp_add),employee.append(street),employee.append(city),employee.append(state),employee.append(pincode)
    save(employee)
    print("Employee added Successfully")

while True:
    print(""" Select Your choice
1.Insert
2.View""")
    ch=int(input("enter your choice:"))
  
    if ch==1:
        AddEmployee()
    elif ch==2:
        ID=int(input("Enter EmpNo:"))
        getrecord(ID)
        

