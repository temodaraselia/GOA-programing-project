

name="Temo"
Lastname="Daraselia"
password=1023

print("-------------------------------------------------------------------")
name1=input("enter your name:")
Lastname1=input("enter your Lastname:")
password1=int(input("enter your Password:"))

print("-------------------------------------------------------------------")
if name=="Temo" and Lastname=="Daraselia":
  while  password1!=password :
    if password>password1:
     password1+=1
     print(password1)
    elif password1>password:
     password1-=1
     print(password1)
    if password1==password:
        print(password,True,"You have successfully logged in.")
    elif name!="Temo" or Lastname!="Daraselia":
       print("სახელი ან გვარი არასწორია")
print("-------------------------------------------------------------------")


