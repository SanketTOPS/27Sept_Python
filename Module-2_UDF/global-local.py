# global
a=43
b=90

def production():
    # local
    a=43
    b=90
    print("Mul:",a*b)

production()
print("Sum:",a+b)

