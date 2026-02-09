#1
import datetime
now=datetime.datetime.now()
print("Current date and time: ", now)
#2
first=input("Enter your first name: ")
last=input("Enter your last name:")
print(last,first)
#3
n=int(input("Enter a number: "))
result=n+int(str(n)*2)+int(str(n)*3)
print("The result is n+nn+nnn",result)
#4
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a==b==c:
    print("3*(a+b+c):",3*(a+b+c))
else:
    print("a+b+c:",a+b+c)
#5
x=int(input("Enter the first number: "))
y=int(input("Enter the second number: "))
r=(x+y)**2
print("The result is (x+y)**2:",r)
#6
amt=float(input("Enter principal amount: "))
rate=float(input("Enter rate of interest: "))
years=float(input("Enter time in years: "))
future_value=amt*(1+rate/100)**years
print("The future value is:",round(future_value,2))
 #7
s=input("Enter a string:")
if '.'in s:
    print(float(s))
else:
    print(int(s))
#8
numb=int(input("Enter a number:"))
sum_n=numb*(numb+1)//2
print("The sum of first",numb,"natural numbers is:",sum_n)
#9
num=input("Enter a number")
sum_digits=0
for i in num:
    sum_digits+=int(i)
print("Sum of digits:",sum_digits)
#10
ch=input("Enter a character:")
print("ASCII value:",ord(ch))
11
m=input("Enter a string:")
if m.isnumeric():
    print("The string is numeric")
else:
    print("The string is not numeric")
12
print("Rectangle pattern with 5 rows and 3 cols of stars:")
for _ in range(5):
    for p in range(3):
        print("*", end=" ")
    print()
#13
print("num which is divisible by 7 and not multiple of 5 b/w 2000-3200")
for d in range(2000,3201):
    if d%7==0 and d%5!=0:
        print(d,end=",")
# 14
import math
C=50
H=30
values=input("Enter comma separated numbers:").split(',')
res=[]
for D in values:
    Q=math.sqrt((2*C*int(D))/H)
    res.append(str(round(Q)))
print(",".join(res))
#15
rows=5
CH=65
for i in range(rows-1,-1,-1):
    for j in range(i+1):
        print(chr(CH), end=" ")
        CH+=1
    print()