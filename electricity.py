unit=int(input("Enter the units comsumed:"))
r=5*unit
print("Rs comsumed on units is :",r)
if r>1000:
    r=r-(r*0.1)
    print("Rs after 10% discount is :",r)
else:
    print("No discount")