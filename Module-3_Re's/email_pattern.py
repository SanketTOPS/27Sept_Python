import re

#sanketchauhan@gmail.com
email=input("Enter an email:")

email_pattern="^[a-z._]+@+[a-z]+[.\]+[a-z]"

x=re.findall(email_pattern,email)

if x:
    print("Valid Email!")
else:
    print("Error!Invalid Email")