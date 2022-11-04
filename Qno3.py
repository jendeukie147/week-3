password=input("Enter a password:")
if((len(password)>=8) and (len(password)<=12)):
    password2=input("Enter password again:")
    if password==password2:
        print("Password set")
    else:
        print("Sorry password wrong try again.")
else:
    print("Sorry you entered less than 8 characters or more than 12 characters")