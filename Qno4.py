BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password=input("Enter a password:")
if ((len(password)>=8)and (len(password)<=12)):
    password2=input("Enter password again:")
    if password==password2:
        if password not in BAD_PASSWORDS and password2 not in BAD_PASSWORDS:
            print("password set")
        else:
            print("bad password")
    else:
        print("error")
else:
     print("sorry you entered less than 8 characters or more than 12 characters.")