age=int(input("enter your age?"))
if age <5:
    print("Free ticket!")
elif age>=5 and age<=17:
    print("Child ticket: $10")
elif age>=18 and age<=64:
    print("Adult ticket: $20")
else:
    print ("Senior ticket: $15")

