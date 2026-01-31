print("Dear Student,Kinldy enter following details:")
name=input("Student ID:")
id=input("Email ID:")
num=input("Password:")
age=input("Referral Code:")
if(name[0:3]!='CSE-'or len(name)!=7 or name[4:6].isdigit()!=True ):
  print("Invalid details!")

else:
  print("valid")