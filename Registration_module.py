def email_verification(username):
    if(username.rfind('.')-username.rfind('@')>=2 and((ord(username[0])>=97 and ord(username[0])<=122)) or (ord(username[0])>=65 and ord(username[0])<=90) and username.rfind('@')>=4):
        return True
    return False
def password_verification(password):
    upper,lower,special,digit=0,0,0,0
    if(len(password)>=5 and len(password)<=16):
        for i in password:
            if(ord(i)>=65 and ord(i)<=90):
                upper+=1
            elif(ord(i)>=97 and ord(i)<=122):
                lower+=1
            elif(ord(i)>=48 and ord(i)<=57):
                digit+=1
            else:
                special+=1
        if(upper>=1 and lower>=1 and digit>=1 and special>=1):
            return True
    return False
def register():
    username=input("Enter username :")
    password1=input("Enter password :")
    password2=input("Confirm password :")
    if(email_verification(username) ):
        if(password_verification(password1) and password_verification(password2)):
            if(password1==password2):
                if(check_email(username)):
                    print("Username already existed!\n")
                    print("Do you want to login\n")
                    choice=input("Type yes or no")
                    if(choice=="yes" or choice=="Yes"):
                        login()
                    else:
                        register()
                else:
                    print("Registration successful\nLogin with the credentials")
                    file=open("file.txt","a")
                    file.write(username)
                    file.write(" ")
                    file.write(password1)
                    file.write("\n")
                    file.close()
                    login()
            else:
                print("Password mismatched")
        else:
            print("Password Invalid")
    else:
        print("Email Invalid")
def login():
    username=input("Enter username :")
    password=input("Enter password :")
    if(email_verification(username) ):
        if(password_verification(password)):
            if(check_email(username)):
                if(check_password(password)):
                    print("*******Login Succesful******")
                else:
                    print("password wrong")
            else:
                print("username wrong")
        else:
            print("Password Invalid")
    else:
        print("Email Invalid")
def forgot_password():
    username=input("Enter username :")
    if(email_verification(username)):
        if(check_email(username)):
            password1=input("Enter password :")
            password2=input("Confirm password :")
            if(password_verification(password1) and password_verification(password2)):
                if(password1==password2):
                    update_password(username,password1)
                    print("***Password updated****")
                    login()
                else:
                    print("Password mismatched")
            else:
                print("Password Invalid")
        else:
            print("Not registered!Kindly check the username")
    else:
        print("Email Invalid")
def check_email(username):
    file=open("file.txt","r")
    for i in file:
        word=i.split()
        if(word[0]==username):
              return True
    return False
def check_password(password):
    file=open("file.txt","r")
    for i in file:
        word=i.split()
        if(word[1]==password):
            file.close()
            return True
    file.close()
    return False
def update_password(username,password):
    c=0
    file=open("file.txt","r")
    for i in file:
        word=i.split()
        if(word[0]==username):
              break
        c+=1
    file.close()
    data=open("file.txt","r").readlines()
    s=username+" "+password+"\n"
    data[c]=s
    with open('file.txt', 'w') as file:
        file.writelines( data )
    file.close()
    
while(True):
    print("******************\n1.Register\n2.Login\n3.Forgot Password\n4.exit\n******************")
    choice=int(input("Enter your choice :"))
    if(choice==1):
        register()
    elif(choice==2):
        login()
    elif(choice==3):
        forgot_password()
    elif(choice==4):
        exit(0)
    else:
        print("Invalid choice! Try again")






