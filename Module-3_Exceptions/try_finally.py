try:
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print("Sum:",a+b)
except Exception as er:
    print(er)
finally:
    print("This is Finally Block.")