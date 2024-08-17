a=0
while a==0:
    password=input("Enter your password:")
    valid=False
    if len(password)>=7:
        if not password.isalnum():
            for i in password:
                if i.isupper():
                    valid=True
                    break
    if valid:
        print("valid")
        a=1
    else:
        print("invalid")
