#calc.py

import arithmetic
num1=eval(input("enter first number :"))
num2=eval(input("enter second number :"))
ope=input("enter operation (+ or - or * or /)")
if ope=="+":
    r=arithmetic.add(num1,num2)
    print(f"{num1} + {num2} = {r}")
elif ope=="-":
    r=arithmetic.sub(num1,num2)
    print(f"{num1} - {num2} = {r}")
elif ope=="*":
    r=arithmetic.mul(num1,num2)
    print(f"{num1} + {num2} = {r}")
elif ope=="/":
    r=arithmetic.div(num1,num2)
    print(f"{num1} / {num2} = {r}")
else:
    print ("invalid operater")
