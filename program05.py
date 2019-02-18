input=raw_input()
a,b,c=input.split()
if(a>c) and (b>c):
    print(a)
elif(c>a) and (a>c):
        print(b)
else:
      print(c)
