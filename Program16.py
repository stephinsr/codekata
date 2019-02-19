
h=int(input("Enter any number: "))
a=list(map(int,str(h)))
b=list(map(lambda x:x**3,a))
if(sum(b)==h):
    print("The number is an armstrong number. ")
else:
    print("The number isn't an arsmtrong number. ")
