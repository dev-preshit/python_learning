# WAP in python to create a calculator
a=float(input("Enter first value"))
b=float(input("Enter second value"))
n=str(input("Enter an operator value"))

if n == '+' :
    print("ANS: ",a+b)
elif n == '-':
    print("ANS: ",a-b)
elif n == '*':
    print("ANS: ",a*b)
elif n == '/':
    print("ANS: ",a/b)
elif n == '%':
    print("ANS: ",a%b)
elif n == '**':
    print("ANS: ",a**b)
elif n == '//':
    print("ANS: ",a//b)
else:
    print("WRONG CODE")

