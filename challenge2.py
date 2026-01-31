print("Dear Student, Kindly enter following details:")
id=input("Student ID:")
email=input("Email ID:")
pasw=input("Password:")
code=input("Referral Code:")
num=pasw.count("0")+pasw.count("1")+pasw.count("2")+pasw.count("3")+pasw.count("4")+pasw.count("5")+pasw.count("6")+pasw.count("7")+pasw.count("8")+pasw.count("9")

if(id[0:4]!='CSE-'or len(id)!=7 or id[-3:].isdigit()!=True ):
    print("REJECTED")
elif(email.count("@")==0 or email.count(".")==0 or email[0]=="@" or email[-1]=="@" or email[-4:]!=".edu"):
    print("REJECTED")
elif(len(pasw)<8 or pasw.title()[0]!=pasw[0] or num==0):
    print("REJECTED")
elif(code[0:4]=="REF" or code[-1]!="@" or len(code)!=6 or code[-3:-1].isdigit()!=True ):
    print("REJECTED")
else:
    print("APPROVED")